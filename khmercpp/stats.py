"""Statistics computed from the inventory and the real files on disk.

The Sphinx build, the command line pipeline and the progress page all call
:func:`compute`, so the published numbers cannot be fabricated: a page only
counts as translated when its file exists, is valid UTF-8 and contains a
substantial amount of Khmer text.
"""

from __future__ import annotations

import datetime as _dt
import json
import pathlib
import re
from typing import Any

from . import inventory as inv_mod

KHMER_RE = re.compile(r"[\u1780-\u17FF\u19E0-\u19FF]")
#: A page shorter than this is treated as a stub, not a translation.
MIN_KHMER_CHARS = 400


def khmer_char_count(path: pathlib.Path) -> int:
    """Count Khmer code points in a file, returning 0 when it is unreadable."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return 0
    return len(KHMER_RE.findall(text))


def _page_state(page: dict[str, Any], inventory: dict[str, Any]) -> dict[str, Any]:
    path = inv_mod.page_file(page["id"])
    chars = khmer_char_count(path) if path.is_file() else 0
    status = page["status"]
    problem = ""
    if status in inv_mod.DONE_STATUSES:
        if not path.is_file():
            problem = "file មិនមាន"
            status = "failed"
        elif chars < MIN_KHMER_CHARS:
            problem = f"ខ្លីពេក ({chars} តួអក្សរខ្មែរ)"
            status = "failed"
    return {
        "id": page["id"],
        "title_km": page["title_km"],
        "track": page["id"].split("/", 1)[0],
        "status": status,
        "declared_status": page["status"],
        "reviewed": bool(page.get("reviewed", False)),
        "since": page["since"],
        "file": str(path.relative_to(inv_mod.REPO_ROOT)),
        "exists": path.is_file(),
        "khmer_chars": chars,
        "sources": list(page.get("sources", [])),
        "examples": inv_mod.examples_for(inventory, page["id"]),
        "problem": problem,
    }


def _examples_report() -> dict[str, Any] | None:
    path = inv_mod.REPO_ROOT / "data" / "examples-report.json"
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def compute(inventory: dict[str, Any] | None = None) -> dict[str, Any]:
    """Compute the full statistics document."""
    inventory = inventory or inv_mod.load()
    pages = [_page_state(page, inventory) for page in inventory["pages"]]
    total = len(pages)
    translated = [p for p in pages if p["status"] in inv_mod.DONE_STATUSES]
    verified = [p for p in translated if p["reviewed"]]
    awaiting_review = [p for p in translated if not p["reviewed"]]
    in_progress = [p for p in pages if p["status"] == "in_progress"]
    pending = [p for p in pages if p["status"] == "pending"]
    failed = [p for p in pages if p["status"] == "failed"]

    tracks: list[dict[str, Any]] = []
    for track in inventory["tracks"]:
        track_rows = [p for p in pages if p["track"] == track["id"]]
        track_done = [p for p in track_rows if p["status"] in inv_mod.DONE_STATUSES]
        tracks.append(
            {
                "id": track["id"],
                "title_km": track["title_km"],
                "title_en": track["title_en"],
                "doc": track["doc"],
                "total": len(track_rows),
                "translated": len(track_done),
                "verified": len([p for p in track_done if p["reviewed"]]),
                "pending": len([p for p in track_rows if p["status"] == "pending"]),
                "completion_pct": round(len(track_done) / len(track_rows) * 100, 1)
                if track_rows
                else 0.0,
            }
        )

    urls = inv_mod.source_urls(inventory)
    examples = _examples_report()
    khmer_chars = sum(p["khmer_chars"] for p in pages)

    return {
        "generated_at": _dt.datetime.now(_dt.UTC).strftime("%Y-%m-%d %H:%M UTC"),
        "totals": {
            "required": total,
            "translated": len(translated),
            "verified": len(verified),
            "awaiting_review": len(awaiting_review),
            "in_progress": len(in_progress),
            "pending": len(pending),
            "failed": len(failed),
            "completion_pct": round(len(translated) / total * 100, 1) if total else 0.0,
            "verified_pct": round(len(verified) / total * 100, 1) if total else 0.0,
        },
        "sources": {
            "pages_with_sources": len([p for p in pages if p["sources"]]),
            "unique_urls": len(urls),
            "shared_urls": len([url for url, ids in urls.items() if len(ids) > 1]),
        },
        "khmer": {
            "characters": khmer_chars,
            "avg_chars_per_page": round(khmer_chars / len(pages), 1) if pages else 0.0,
            "min_chars_threshold": MIN_KHMER_CHARS,
        },
        "examples": examples
        or {"total": 0, "compiled": 0, "passed": 0, "report": "មិនទាន់ដំណើរការ"},
        "tracks": tracks,
        "pages": pages,
        "problems": [
            {"id": p["id"], "problem": p["problem"]} for p in pages if p["problem"]
        ],
        "pending_pages": [
            {"id": p["id"], "title_km": p["title_km"]} for p in pending + in_progress
        ],
    }


def write_snapshot(stats: dict[str, Any] | None = None) -> pathlib.Path:
    """Write ``data/progress.json`` (committed snapshot of live statistics)."""
    stats = stats or compute()
    target = inv_mod.REPO_ROOT / "data" / "progress.json"
    summary = {
        "generated_at": stats["generated_at"],
        "totals": stats["totals"],
        "sources": stats["sources"],
        "khmer": stats["khmer"],
        "examples": stats["examples"],
        "tracks": stats["tracks"],
    }
    target.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return target
