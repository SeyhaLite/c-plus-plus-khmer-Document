"""Single source of truth for the documentation inventory.

Every statistic on the website is derived from ``data/inventory.json`` plus the
files that actually exist on disk.  Nothing is hard-coded: if a page is listed
as translated but its file is missing or empty, the statistics engine reports
it as missing instead of counting it as progress.
"""

from __future__ import annotations

import json
import pathlib
import re
from typing import Any

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
INVENTORY_PATH = REPO_ROOT / "data" / "inventory.json"
DOCS_DIR = REPO_ROOT / "docs"
EXAMPLES_DIR = REPO_ROOT / "examples"

#: Translation states, ordered from most to least complete.
STATUSES = ("verified", "translated", "in_progress", "pending", "failed")
DONE_STATUSES = frozenset({"verified", "translated"})

#: C++ standards we document, plus the human readable label used in the UI.
STANDARDS = ("cpp98", "cpp11", "cpp14", "cpp17", "cpp20", "cpp23", "cpp26")
STANDARD_LABELS = {
    "cpp98": "C++98/03",
    "cpp11": "C++11",
    "cpp14": "C++14",
    "cpp17": "C++17",
    "cpp20": "C++20",
    "cpp23": "C++23",
    "cpp26": "C++26 (ព្រាង)",
}
STANDARD_ORDER = {name: index for index, name in enumerate(STANDARDS)}

PAGE_ID_RE = re.compile(r"^[a-z0-9][a-z0-9-]*/[a-z0-9][a-z0-9-]*$")


class InventoryError(RuntimeError):
    """Raised when the inventory is structurally invalid."""


def load(path: pathlib.Path | None = None) -> dict[str, Any]:
    """Load and validate the inventory."""
    target = path or INVENTORY_PATH
    with target.open(encoding="utf-8") as handle:
        inventory = json.load(handle)
    validate(inventory)
    return inventory


def save(inventory: dict[str, Any], path: pathlib.Path | None = None) -> None:
    """Persist the inventory, keeping the file diff friendly."""
    target = path or INVENTORY_PATH
    validate(inventory)
    text = json.dumps(inventory, ensure_ascii=False, indent=2) + "\n"
    target.write_text(text, encoding="utf-8")


def validate(inventory: dict[str, Any]) -> None:
    """Reject duplicate ids, unknown tracks and invalid status/standard values."""
    if inventory.get("schema_version") != 1:
        raise InventoryError("unsupported schema_version")
    tracks = {track["id"] for track in inventory["tracks"]}
    seen_ids: set[str] = set()
    seen_files: set[str] = set()
    for page in inventory["pages"]:
        page_id = page["id"]
        if not PAGE_ID_RE.match(page_id):
            raise InventoryError(f"invalid page id: {page_id!r}")
        if page_id in seen_ids:
            raise InventoryError(f"duplicate page id: {page_id}")
        seen_ids.add(page_id)
        track = page_id.split("/", 1)[0]
        if track not in tracks:
            raise InventoryError(f"unknown track {track!r} in {page_id}")
        if page["status"] not in STATUSES:
            raise InventoryError(f"invalid status {page['status']!r} in {page_id}")
        if page["since"] not in STANDARDS:
            raise InventoryError(f"invalid standard {page['since']!r} in {page_id}")
        if not page.get("title_km", "").strip():
            raise InventoryError(f"missing Khmer title in {page_id}")
        if page_id in seen_files:
            raise InventoryError(f"duplicate page file: {page_id}")
        seen_files.add(page_id)


def page_file(page_id: str) -> pathlib.Path:
    """Return the Markdown file backing a page id."""
    return DOCS_DIR / f"{page_id}.md"


def examples_for(inventory: dict[str, Any], page_id: str) -> list[str]:
    """Return repository-relative example programs attached to a page.

    Examples live at ``examples/<page id>.cpp`` by convention, so a new page
    only needs its program file to be picked up.  An explicit ``examples``
    list in the inventory overrides the convention.
    """
    page = find_page(inventory, page_id)
    if page.get("examples"):
        return [str(item) for item in page["examples"]]
    candidate = EXAMPLES_DIR / f"{page_id}.cpp"
    if candidate.is_file():
        return [str(candidate.relative_to(REPO_ROOT))]
    return []


def find_page(inventory: dict[str, Any], page_id: str) -> dict[str, Any]:
    """Return a single page record or raise ``KeyError``."""
    for page in inventory["pages"]:
        if page["id"] == page_id:
            return page
    raise KeyError(f"unknown page id: {page_id}")


def pages_by_id(inventory: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {page["id"]: page for page in inventory["pages"]}


def track_pages(inventory: dict[str, Any], track_id: str) -> list[dict[str, Any]]:
    return [page for page in inventory["pages"] if page["id"].startswith(track_id + "/")]


def source_urls(inventory: dict[str, Any]) -> dict[str, list[str]]:
    """Map every recorded source URL to the pages that cite it."""
    mapping: dict[str, list[str]] = {}
    for page in inventory["pages"]:
        for url in page.get("sources", []):
            mapping.setdefault(url, []).append(page["id"])
    return mapping


def duplicate_sources(inventory: dict[str, Any]) -> dict[str, int]:
    """Return source URLs cited by more than one page, with their counts."""
    return {url: len(ids) for url, ids in source_urls(inventory).items() if len(ids) > 1}
