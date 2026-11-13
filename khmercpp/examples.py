"""Compile and run the C++ programs used by the documentation.

Each example is a complete program under ``examples/`` with two machine
readable headers::

    // std: c++17
    /* EXPECT
    Hello, world!
    */

``std:`` selects ``-std=``, and the ``EXPECT`` block is compared with the
program's standard output so examples are executed, not merely compiled.
"""

from __future__ import annotations

import datetime as dt
import json
import pathlib
import re
import subprocess
import tempfile

from . import inventory as inv_mod

EXAMPLES_DIR = inv_mod.EXAMPLES_DIR
REPORT_PATH = inv_mod.REPO_ROOT / "data" / "examples-report.json"

STD_RE = re.compile(r"^\s*//\s*std:\s*(c\+\+\d+)", re.MULTILINE)
EXPECT_RE = re.compile(r"/\*\s*EXPECT\n(.*?)\*/", re.DOTALL)


def _normalise(text: str) -> str:
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


def example_files() -> list[pathlib.Path]:
    if not EXAMPLES_DIR.is_dir():
        return []
    return sorted(EXAMPLES_DIR.rglob("*.cpp"))


def check_example(path: pathlib.Path, compiler: str = "g++") -> dict[str, object]:
    """Compile one example and compare its output with the EXPECT block."""
    source = path.read_text(encoding="utf-8")
    match = STD_RE.search(source)
    standard = match.group(1) if match else "c++17"
    result: dict[str, object] = {
        "file": str(path.relative_to(inv_mod.REPO_ROOT)),
        "std": standard,
        "compiled": False,
        "ran": False,
        "passed": False,
        "error": "",
        "output": "",
    }

    with tempfile.TemporaryDirectory() as tmp:
        binary = pathlib.Path(tmp) / "example"
        compiled = subprocess.run(
            [
                compiler,
                f"-std={standard}",
                "-Wall",
                "-Wextra",
                "-pedantic",
                "-O1",
                str(path),
                "-o",
                str(binary),
            ],
            capture_output=True,
            text=True,
            timeout=180,
            check=False,
        )
        if compiled.returncode != 0:
            result["error"] = (compiled.stderr or compiled.stdout).strip()[:2000]
            return result
        result["compiled"] = True

        expect = EXPECT_RE.search(source)
        if not expect:
            result["error"] = "គ្មានប្លុក EXPECT សម្រាប់ផ្ទៀងផ្ទាត់លទ្ធផល"
            return result

        try:
            run = subprocess.run(
                [str(binary)], capture_output=True, text=True, timeout=30, check=False
            )
        except subprocess.TimeoutExpired:
            result["error"] = "កម្មវិធីដំណើរការលើស 30 វិនាទី"
            return result
        result["ran"] = True
        actual = _normalise(run.stdout)
        result["output"] = actual[:500]
        if run.returncode != 0:
            result["error"] = (
                f"កម្មវិធីបញ្ចប់ដោយលេខកូដ {run.returncode}: {run.stderr.strip()[:500]}"
            )
            return result
        expected = _normalise(expect.group(1))
        if actual != expected:
            result["error"] = (
                "លទ្ធផលមិនត្រូវនឹង EXPECT\n--- រំពឹង ---\n"
                f"{expected}\n--- ទទួលបាន ---\n{actual}"
            )
            return result
        result["passed"] = True
        return result


def run_all(compiler: str = "g++") -> dict[str, object]:
    """Check every example and write ``data/examples-report.json``."""
    results = [check_example(path, compiler) for path in example_files()]
    report: dict[str, object] = {
        "generated_at": dt.datetime.now(dt.UTC).strftime("%Y-%m-%d %H:%M UTC"),
        "compiler": compiler,
        "total": len(results),
        "compiled": len([item for item in results if item["compiled"]]),
        "ran": len([item for item in results if item["ran"]]),
        "passed": len([item for item in results if item["passed"]]),
        "failed": [item for item in results if not item["passed"]],
        "examples": results,
    }
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return report
