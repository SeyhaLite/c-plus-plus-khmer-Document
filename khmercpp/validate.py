"""Content validation for the Khmer documentation.

These checks are what makes "verified" mean something:

* a page that claims to be translated must really exist and really be Khmer,
* Khmer must never leak into inline code (syntax stays untouched),
* every ``literalinclude`` and relative link must resolve,
* banned terminology variants are rejected (one word per concept),
* every finished page cites at least one authoritative source.
"""

from __future__ import annotations

import dataclasses
import json
import pathlib
import re
from typing import Any

from . import inventory as inv_mod
from . import stats as stats_mod

TERMINOLOGY_PATH = inv_mod.REPO_ROOT / "data" / "terminology.json"

KHMER_RE = re.compile(r"[\u1780-\u17FF\u19E0-\u19FF]")
INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
FENCE_RE = re.compile(r"^[ \t]*(```+|~~~+)[ \t]*([^\s`]*)(?:[ \t]+.*)?$", re.MULTILINE)
LITERALINCLUDE_RE = re.compile(r"^```\{literalinclude\}\s+(\S+)", re.MULTILINE)
MD_LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
TRANSLATION_META_RE = re.compile(r"```\{translation-meta\}\s+([a-z0-9\-/]+)")
H1_RE = re.compile(r"\A#\s+(.+)")
ALLOWED_FENCE_LANGUAGES = {
    "cpp",
    "c",
    "bash",
    "bat",
    "console",
    "text",
    "json",
    "yaml",
    "cmake",
    "output",
}
MOJIBAKE_MARKERS = ("Ã", "â€", "ï¿½")


@dataclasses.dataclass(frozen=True)
class Problem:
    """A single finding from a validator."""

    level: str  # "error" or "warning"
    page_id: str
    message: str

    def format(self) -> str:
        location = self.page_id or "(គម្រោង)"
        return f"[{self.level}] {location}: {self.message}"


def load_terminology(path: pathlib.Path | None = None) -> dict[str, Any]:
    target = path or TERMINOLOGY_PATH
    with target.open(encoding="utf-8") as handle:
        return json.load(handle)


def _strip_fenced_blocks(text: str) -> str:
    """Return the prose only: fenced code is blanked out.

    Syntax inside a code fence is not Markdown, so links and inline code must
    only be checked outside fences.
    """
    kept: list[str] = []
    open_marker = ""
    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if match:
            ticks = match.group(1)
            if not open_marker:
                open_marker = ticks[0]
                kept.append("")
                continue
            if ticks[0] == open_marker and not match.group(2):
                open_marker = ""
                kept.append("")
                continue
        kept.append("" if open_marker else line)
    return "\n".join(kept)


def _check_fences(text: str, page_id: str) -> list[Problem]:
    """Check only opening code fences for a missing or unknown language."""
    problems: list[Problem] = []
    open_marker = ""
    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if not match:
            continue
        ticks, language = match.group(1), match.group(2)
        if open_marker:
            if ticks[0] == open_marker and not language:
                open_marker = ""
            continue
        open_marker = ticks[0]
        if language.startswith("{"):
            continue
        if not language:
            problems.append(Problem("warning", page_id, "code fence គ្មានឈ្មោះភាសា"))
        elif language not in ALLOWED_FENCE_LANGUAGES:
            problems.append(
                Problem("warning", page_id, f"ភាសា code fence មិនស្គាល់: {language}")
            )
    return problems


def check_page(
    page: dict[str, Any],
    terminology: dict[str, Any],
    inventory: dict[str, Any],
) -> list[Problem]:
    """Validate one page. Returns every problem found."""
    page_id = page["id"]
    path = inv_mod.page_file(page_id)
    problems: list[Problem] = []

    if not path.is_file():
        if page["status"] in inv_mod.DONE_STATUSES:
            problems.append(Problem("error", page_id, "ស្ថានភាពបានបកប្រែ ប៉ុន្តែឯកសារមិនមាន"))
        return problems

    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        problems.append(Problem("error", page_id, f"ឯកសារមិនមែន UTF-8 ត្រឹមត្រូវ: {error}"))
        return problems

    if "\ufffd" in text:
        problems.append(Problem("error", page_id, "មានតួអក្សរ U+FFFD (ខូច Unicode)"))
    for marker in MOJIBAKE_MARKERS:
        if marker in text:
            problems.append(Problem("error", page_id, f"សញ្ញាខូច encoding: {marker!r}"))

    heading = H1_RE.search(text)
    if not heading:
        problems.append(Problem("error", page_id, "ខ្វះចំណងជើង H1 (# ...)"))
    elif not KHMER_RE.search(heading.group(1)):
        problems.append(Problem("error", page_id, "ចំណងជើង H1 មិនមែនជាភាសាខ្មែរ"))

    meta = TRANSLATION_META_RE.search(text)
    if not meta:
        problems.append(Problem("error", page_id, "ខ្វះ directive {translation-meta}"))
    elif meta.group(1) != page_id:
        problems.append(
            Problem("error", page_id, f"translation-meta ចង្អុលទៅ {meta.group(1)} មិនត្រូវនឹង id")
        )

    prose = _strip_fenced_blocks(text)

    for span in INLINE_CODE_RE.finditer(prose):
        if KHMER_RE.search(span.group(0)):
            problems.append(
                Problem(
                    "error",
                    page_id,
                    f"មានអក្សរខ្មែរក្នុង inline code: {span.group(0)[:60]}",
                )
            )

    problems.extend(_check_fences(text, page_id))

    base = path.parent
    targets = [match.group(1) for match in MD_LINK_RE.finditer(prose)]
    targets += [match.group(1) for match in LITERALINCLUDE_RE.finditer(text)]
    for target in targets:
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        clean = target.split("#")[0].split("?")[0]
        if not clean:
            continue
        candidate = (base / clean).resolve()
        if not candidate.exists():
            problems.append(Problem("error", page_id, f"តំណខូច: {target}"))

    for term in terminology["terms"]:
        for banned in term.get("banned", []):
            if banned and banned in text:
                problems.append(
                    Problem(
                        "error",
                        page_id,
                        f"ពាក្យត្រូវហាម: {banned!r} — សូមប្រើ {term['km']!r}",
                    )
                )

    if page["status"] in inv_mod.DONE_STATUSES:
        if not page.get("sources"):
            problems.append(Problem("error", page_id, "ទំព័របកប្រែត្រូវមានប្រភពយោងយ៉ាងតិចមួយ"))
        chars = stats_mod.khmer_char_count(path)
        if chars < stats_mod.MIN_KHMER_CHARS:
            problems.append(
                Problem(
                    "error",
                    page_id,
                    f"អក្សរខ្មែរតែ {chars} តួ (ត្រូវការ ≥ {stats_mod.MIN_KHMER_CHARS})",
                )
            )
        for example in inv_mod.examples_for(inventory, page_id):
            example_path = inv_mod.REPO_ROOT / example
            if not example_path.is_file():
                problems.append(Problem("error", page_id, f"គំរូកូដមិនមាន: {example}"))

    return problems


def check_all(inventory: dict[str, Any] | None = None) -> list[Problem]:
    """Validate the whole project and return every finding."""
    inventory = inventory or inv_mod.load()
    terminology = load_terminology()
    problems: list[Problem] = []

    for url, pages in inv_mod.source_urls(inventory).items():
        if not url.startswith("https://"):
            problems.append(
                Problem("error", pages[0], f"ប្រភពយោងមិនមែន https: {url}")
            )

    for page in inventory["pages"]:
        problems.extend(check_page(page, terminology, inventory))

    # A source URL shared by several pages is expected (for example the
    # cppreference "function" page backs five topics), so this is information,
    # not a defect.
    duplicates = inv_mod.duplicate_sources(inventory)
    for url, count in duplicates.items():
        problems.append(
            Problem("info", "", f"ប្រភពយោងត្រូវបានប្រើ {count} ដង: {url}")
        )

    return problems


def errors(problems: list[Problem]) -> list[Problem]:
    return [problem for problem in problems if problem.level == "error"]
