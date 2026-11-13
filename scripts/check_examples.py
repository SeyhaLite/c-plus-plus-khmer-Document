#!/usr/bin/env python3
"""CLI: compile and run every C++ example referenced by the documentation."""

from __future__ import annotations

import argparse
import pathlib
import shutil
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent))

from khmercpp import examples, inventory  # noqa: E402


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compile and run documentation examples")
    parser.add_argument("--strict", action="store_true", help="exit 1 on any failure")
    parser.add_argument("--compiler", default="g++")
    parser.add_argument("--filter", default="", help="only paths containing this text")
    args = parser.parse_args(argv)

    if shutil.which(args.compiler) is None:
        print(f"error: compiler not found: {args.compiler}", file=sys.stderr)
        return 1

    report = examples.run_all(args.compiler)
    for item in report["examples"]:  # type: ignore[index]
        if args.filter and args.filter not in str(item["file"]):
            continue
        mark = "PASS" if item["passed"] else "FAIL"
        print(f"{mark:4} {item['file']:56} {item['std']}")
        if not item["passed"] and item["error"]:
            print(f"     {item['error'][:1500]}")
    print(
        f"\n{report['passed']}/{report['total']} examples passed "
        f"({report['compiled']} compiled, {report['ran']} ran). "
        f"Report: {examples.REPORT_PATH.relative_to(inventory.REPO_ROOT)}"
    )
    if args.strict and report["passed"] != report["total"]:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
