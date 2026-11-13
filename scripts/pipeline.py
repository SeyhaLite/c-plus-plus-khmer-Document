#!/usr/bin/env python3
"""Translation pipeline for the Khmer C++ documentation.

Commands
--------
``status``     Show live statistics (optionally write data/progress.json).
``discover``   Verify every recorded source URL over HTTP and record the result.
``fetch``      Download one page's source text into data/.cache (never committed).
``translate``  Produce a Khmer draft with a configured provider, then validate.
``verify``     Run all checks for a page; with --accept, mark it verified.
``validate``   Run every project-wide check (used by CI and Read the Docs).
``new``        Scaffold an empty page and mark it in progress.

The pipeline never overwrites a non-empty page without ``--force`` and never
marks a page complete unless its file really exists and really contains Khmer.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request
from html.parser import HTMLParser

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from khmercpp import examples, inventory as inv_mod, providers  # noqa: E402
from khmercpp import stats as stats_mod, validate as validate_mod  # noqa: E402

CACHE_DIR = inv_mod.REPO_ROOT / "data" / ".cache"
DISCOVERY_PATH = CACHE_DIR / "discovery.json"
USER_AGENT = (
    "KhmerCppDocsBot/1.0 (+https://github.com/; documentation source verification)"
)
TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.DOTALL | re.IGNORECASE)


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def _today() -> str:
    return dt.date.today().isoformat()


def _fetch_url(url: str, timeout: int = 25) -> tuple[int, str, str]:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        body = response.read(600_000).decode("utf-8", "replace")
        return response.status, response.geturl(), body


class _TextExtractor(HTMLParser):
    """Very small HTML to text converter used only for translation context."""

    SKIP = {"script", "style", "noscript", "svg"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self._skip_depth += 1
        elif tag in {"p", "div", "li", "h1", "h2", "h3", "h4", "tr", "pre"}:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP and self._skip_depth:
            self._skip_depth -= 1

    def handle_data(self, data):
        if not self._skip_depth:
            self.parts.append(data)

    def text(self) -> str:
        raw = "".join(self.parts)
        lines = [re.sub(r"[ \t]+", " ", line).strip() for line in raw.splitlines()]
        return "\n".join(line for line in lines if line)


def _load_discovery() -> dict[str, dict[str, object]]:
    if DISCOVERY_PATH.is_file():
        try:
            return json.loads(DISCOVERY_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return {}
    return {}


def _save_discovery(data: dict[str, dict[str, object]]) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    DISCOVERY_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


# --------------------------------------------------------------------------
# commands
# --------------------------------------------------------------------------
def cmd_status(args: argparse.Namespace) -> int:
    stats = stats_mod.compute()
    if args.json:
        print(json.dumps(stats, ensure_ascii=False, indent=2))
    else:
        totals = stats["totals"]
        print(f"Required pages      : {totals['required']}")
        print(
            f"Translated          : {totals['translated']} "
            f"({totals['completion_pct']}% of required)"
        )
        print(f"  verified          : {totals['verified']}")
        print(f"  awaiting review   : {totals['awaiting_review']}")
        print(f"In progress         : {totals['in_progress']}")
        print(f"Pending             : {totals['pending']}")
        print(f"Failed / missing    : {totals['failed']}")
        print(
            f"Sources             : {stats['sources']['pages_with_sources']} pages, "
            f"{stats['sources']['unique_urls']} unique URLs"
        )
        print(
            f"Examples            : {stats['examples'].get('passed', 0)}/"
            f"{stats['examples'].get('total', 0)} passed"
        )
        print(f"Khmer characters    : {stats['khmer']['characters']:,}")
        if stats["problems"]:
            print(f"Problems            : {len(stats['problems'])}")
            for problem in stats["problems"]:
                print(f"  - {problem['id']}: {problem['problem']}")
    if args.write:
        path = stats_mod.write_snapshot(stats)
        print(f"\nSnapshot written to {path.relative_to(inv_mod.REPO_ROOT)}")
    return 0


def cmd_discover(args: argparse.Namespace) -> int:
    """Check that every recorded source URL really exists."""
    inventory = inv_mod.load()
    pages = [inv_mod.find_page(inventory, args.page)] if args.page else inventory["pages"]
    urls: list[tuple[str, str]] = []
    for page in pages:
        for url in page.get("sources", []):
            if url not in [item[0] for item in urls]:
                urls.append((url, page["id"]))
    if args.limit:
        urls = urls[: args.limit]

    discovery = _load_discovery()
    failures = 0
    for url, page_id in urls:
        entry: dict[str, object] = {"checked_at": _today(), "page": page_id}
        try:
            status, final_url, body = _fetch_url(url, timeout=args.timeout)
            entry.update(
                {
                    "status": status,
                    "final_url": final_url,
                    "title": html.unescape(TITLE_RE.search(body).group(1)).strip()
                    if TITLE_RE.search(body)
                    else "",
                    "bytes": len(body),
                    "error": "",
                }
            )
            print(f"OK   {status} {url}")
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, OSError) as error:
            failures += 1
            entry.update({"status": None, "error": str(error)[:300]})
            print(f"FAIL      {url} -> {error}")
        discovery[url] = entry
        if args.delay:
            time.sleep(args.delay)

    _save_discovery(discovery)
    print(f"\n{len(urls) - failures}/{len(urls)} sources reachable. Cache: {DISCOVERY_PATH}")
    return 1 if failures and args.strict else 0


def cmd_fetch(args: argparse.Namespace) -> int:
    inventory = inv_mod.load()
    page = inv_mod.find_page(inventory, args.page)
    if not page.get("sources"):
        print(f"error: {args.page} គ្មានប្រភពយោង", file=sys.stderr)
        return 1
    url = args.url or page["sources"][0]
    try:
        status, final_url, body = _fetch_url(url)
    except (urllib.error.URLError, OSError) as error:
        print(f"error: fetch failed: {error}", file=sys.stderr)
        return 1
    extractor = _TextExtractor()
    extractor.feed(body)
    text = extractor.text()
    target = CACHE_DIR / "pages" / f"{args.page.replace('/', '__')}.txt"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(f"# source: {final_url}\n# status: {status}\n\n{text}\n", encoding="utf-8")
    print(f"{len(text):,} characters from {final_url}\n-> {target}")
    return 0


def cmd_translate(args: argparse.Namespace) -> int:
    inventory = inv_mod.load()
    page = inv_mod.find_page(inventory, args.page)
    target = inv_mod.page_file(args.page)
    if target.is_file() and target.stat().st_size > 0 and not args.force:
        print(
            f"refusing to overwrite existing work: {target.relative_to(inv_mod.REPO_ROOT)} "
            "(use --force)",
            file=sys.stderr,
        )
        return 1

    provider = args.provider
    if provider == "auto":
        provider = "openai" if _has_key() else "manual"
    terminology = validate_mod.load_terminology()

    page["status"] = "in_progress"
    inv_mod.save(inventory)

    if provider == "manual":
        body = args.body_file
        if not body:
            print(
                "provider 'manual': សរសេរខ្លួនឯងនៅ docs/<id>.md ឬផ្ដល់ --body-file។ "
                "បន្ទាប់មករត់ `pipeline.py verify --page <id> --accept`។",
                file=sys.stderr,
            )
            return 1
        text = pathlib.Path(body).read_text(encoding="utf-8")
    else:
        source_path = CACHE_DIR / "pages" / f"{args.page.replace('/', '__')}.txt"
        if not source_path.is_file():
            print(
                f"error: គ្មានអត្ថបទប្រភពសម្រាប់បកប្រែ។ រត់ដំបូង៖ "
                f"pipeline.py fetch --page {args.page}",
                file=sys.stderr,
            )
            return 1
        try:
            text = providers.translate(
                source_path.read_text(encoding="utf-8"),
                page,
                terminology,
                provider=provider,
                model=args.model,
            )
        except providers.TranslationError as error:
            print(f"error: {error}", file=sys.stderr)
            return 1

    if re.match(r"^#\s", text):
        text = text.split("\n", 1)[1].lstrip("\n")
    composed = (
        f"# {page['title_km']}\n\n"
        f"```{{translation-meta}} {args.page}\n```\n\n"
        f"{text.strip()}\n"
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(composed, encoding="utf-8")
    page["status"] = "translated"
    page["reviewed"] = False
    page["updated_at"] = _today()
    inv_mod.save(inventory)
    print(f"draft written: {target.relative_to(inv_mod.REPO_ROOT)} (status: translated, unreviewed)")
    return 0


def _has_key() -> bool:
    import os

    return bool(
        os.environ.get("KHMER_TRANSLATE_API_KEY") or os.environ.get("OPENAI_API_KEY")
    )


def cmd_verify(args: argparse.Namespace) -> int:
    inventory = inv_mod.load()
    terminology = validate_mod.load_terminology()
    pages = [inv_mod.find_page(inventory, args.page)] if args.page else inventory["pages"]
    total_errors = 0
    total_warnings = 0
    verified_now: list[str] = []

    for page in pages:
        problems = validate_mod.check_page(page, terminology, inventory)
        example_results = [
            examples.check_example(inv_mod.REPO_ROOT / item, args.compiler)
            for item in inv_mod.examples_for(inventory, page["id"])
        ]
        for result in example_results:
            if not result["passed"]:
                problems.append(
                    validate_mod.Problem(
                        "error",
                        page["id"],
                        f"គំរូកូដបរាជ័យ ({result['file']}): {result['error']}",
                    )
                )
        errors = validate_mod.errors(problems)
        total_errors += len(errors)
        total_warnings += len(problems) - len(errors)
        if args.page:
            for problem in problems:
                print(problem.format())
            if not problems:
                print(f"[ok] {page['id']}: checks passed")
        elif errors:
            for problem in errors:
                print(problem.format())

        if not errors and page["status"] in inv_mod.DONE_STATUSES and args.accept:
            page["reviewed"] = True
            page["status"] = "verified"
            page["updated_at"] = _today()
            verified_now.append(page["id"])

    if verified_now:
        inv_mod.save(inventory)
        print(f"marked verified: {len(verified_now)} page(s)")
    stats_mod.write_snapshot(stats_mod.compute())
    print(f"\nerrors: {total_errors}, warnings: {total_warnings}")
    return 1 if total_errors else 0


def cmd_validate(args: argparse.Namespace) -> int:
    problems = validate_mod.check_all()
    errors = validate_mod.errors(problems)
    warnings = [problem for problem in problems if problem.level == "warning"]
    infos = [problem for problem in problems if problem.level == "info"]
    for problem in errors:
        print(problem.format())
    if args.verbose:
        for problem in warnings + infos:
            print(problem.format())
    print(
        f"\n{len(errors)} error(s), {len(warnings)} warning(s), "
        f"{len(infos)} info across {len(inv_mod.load()['pages'])} pages."
    )
    if (warnings or infos) and not args.verbose:
        print("run with --verbose to list warnings and info")
    if not errors:
        stats_mod.write_snapshot(stats_mod.compute())
    if args.strict and errors:
        return 1
    return 0


def cmd_new(args: argparse.Namespace) -> int:
    inventory = inv_mod.load()
    page = inv_mod.find_page(inventory, args.page)
    target = inv_mod.page_file(args.page)
    if target.is_file() and not args.force:
        print(f"error: {target} មានរួចហើយ (use --force)", file=sys.stderr)
        return 1
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        f"# {page['title_km']}\n\n"
        f"```{{translation-meta}} {args.page}\n```\n\n"
        ":::{admonition} កំពុងសរសេរ\n"
        "ទំព័រនេះមិនទាន់បកប្រែរួចទេ។\n"
        ":::\n",
        encoding="utf-8",
    )
    page["status"] = "in_progress"
    page["updated_at"] = _today()
    inv_mod.save(inventory)
    print(f"scaffolded {target.relative_to(inv_mod.REPO_ROOT)} (status: in_progress)")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    status = sub.add_parser("status", help="live translation statistics")
    status.add_argument("--json", action="store_true")
    status.add_argument("--write", action="store_true")
    status.set_defaults(func=cmd_status)

    discover = sub.add_parser("discover", help="verify source URLs over HTTP")
    discover.add_argument("--page")
    discover.add_argument("--limit", type=int, default=0)
    discover.add_argument("--delay", type=float, default=0.7)
    discover.add_argument("--timeout", type=int, default=25)
    discover.add_argument("--strict", action="store_true")
    discover.set_defaults(func=cmd_discover)

    fetch = sub.add_parser("fetch", help="download source text for translation")
    fetch.add_argument("--page", required=True)
    fetch.add_argument("--url")
    fetch.set_defaults(func=cmd_fetch)

    translate = sub.add_parser("translate", help="produce a Khmer draft")
    translate.add_argument("--page", required=True)
    translate.add_argument("--provider", default="auto", choices=["auto", "manual", "openai"])
    translate.add_argument("--model")
    translate.add_argument("--body-file")
    translate.add_argument("--force", action="store_true")
    translate.set_defaults(func=cmd_translate)

    verify = sub.add_parser("verify", help="run checks and optionally accept a page")
    verify.add_argument("--page")
    verify.add_argument("--accept", action="store_true")
    verify.add_argument("--compiler", default="g++")
    verify.set_defaults(func=cmd_verify)

    validate = sub.add_parser("validate", help="project-wide validation")
    validate.add_argument("--strict", action="store_true")
    validate.add_argument("--verbose", action="store_true")
    validate.set_defaults(func=cmd_validate)

    new = sub.add_parser("new", help="scaffold a page")
    new.add_argument("--page", required=True)
    new.add_argument("--force", action="store_true")
    new.set_defaults(func=cmd_new)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
