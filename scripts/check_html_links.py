#!/usr/bin/env python3
"""Fail when generated Sphinx pages contain duplicate .html.html links."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit


class HrefScanner(HTMLParser):
    """Collect local or external hrefs that accidentally repeat the HTML suffix."""

    def __init__(self, html_file: Path) -> None:
        super().__init__(convert_charrefs=True)
        self.html_file = html_file
        self.findings: list[tuple[int, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for name, value in attrs:
            if name.lower() != "href" or not value:
                continue
            path = urlsplit(value).path.lower()
            if path.endswith(".html.html"):
                self.findings.append((self.getpos()[0], value))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check generated HTML for duplicated .html.html links."
    )
    parser.add_argument(
        "html_dir",
        nargs="?",
        type=Path,
        default=Path("docs/_build/html"),
        help="Sphinx HTML output directory (default: docs/_build/html)",
    )
    args = parser.parse_args()

    if not args.html_dir.is_dir():
        parser.error(f"HTML directory does not exist: {args.html_dir}")

    files = sorted(args.html_dir.rglob("*.html"))
    if not files:
        parser.error(f"No generated HTML files found in: {args.html_dir}")

    total_findings = 0
    for html_file in files:
        scanner = HrefScanner(html_file)
        try:
            scanner.feed(html_file.read_text(encoding="utf-8"))
        except (OSError, UnicodeError) as error:
            print(f"ERROR {html_file}: cannot read HTML: {error}")
            return 2

        for line, href in scanner.findings:
            total_findings += 1
            print(f"FAIL {html_file}:{line}: duplicated HTML suffix: {href}")

    if total_findings:
        print(f"FAIL: found {total_findings} duplicated HTML link(s) in {len(files)} files.")
        return 1

    print(f"PASS: checked {len(files)} generated HTML files; no .html.html links found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
