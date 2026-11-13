"""Sphinx extension: Khmer documentation metadata and live progress dashboard.

Everything rendered here is read from ``data/inventory.json`` and from the
files on disk at build time.  There is no hand-written number anywhere: if a
translation is missing, the badge and the dashboard say so.
"""

from __future__ import annotations

import html
import json
from typing import Any

from docutils import nodes
from sphinx.util.docutils import SphinxDirective

from khmercpp import inventory as inv_mod
from khmercpp import stats as stats_mod

STATUS_LABELS = {
    "verified": ("✓ បានផ្ទៀងផ្ទាត់", "verified"),
    "translated": ("បានបកប្រែ", "translated"),
    "in_progress": ("កំពុងបកប្រែ", "progress"),
    "pending": ("រង់ចាំបកប្រែ", "pending"),
    "failed": ("មានបញ្ហា", "failed"),
}


def _paragraph(items: list[Any]) -> nodes.paragraph:
    para = nodes.paragraph()
    for item in items:
        para += item
    return para


def _table(header: list[str], rows: list[list[str]], widths: list[int] | None = None) -> nodes.table:
    table = nodes.table()
    tgroup = nodes.tgroup(cols=len(header))
    table += tgroup
    for width in widths or [1] * len(header):
        tgroup += nodes.colspec(colwidth=width)
    thead = nodes.thead()
    tgroup += thead
    head_row = nodes.row()
    for title in header:
        entry = nodes.entry()
        entry += nodes.paragraph(text=title)
        head_row += entry
    thead += head_row
    tbody = nodes.tbody()
    tgroup += tbody
    for row in rows:
        table_row = nodes.row()
        for cell in row:
            entry = nodes.entry()
            entry += nodes.paragraph(text=cell)
            table_row += entry
        tbody += table_row
    return table


class TranslationMeta(SphinxDirective):
    """Render the translation status block for one page.

    ``.. translation-meta:: getting-started/what-is-cpp``
    """

    required_arguments = 1
    optional_arguments = 0
    has_content = False

    def run(self):
        page_id = self.arguments[0].strip()
        inventory = self.env.app.khmer_inventory
        try:
            page = inv_mod.find_page(inventory, page_id)
        except KeyError as error:
            raise self.error(str(error)) from error

        self.env.note_dependency(str(inv_mod.INVENTORY_PATH))
        path = inv_mod.page_file(page_id)
        chars = stats_mod.khmer_char_count(path) if path.is_file() else 0
        status = page["status"]
        if status in inv_mod.DONE_STATUSES and chars < stats_mod.MIN_KHMER_CHARS:
            status = "failed"

        label, css = STATUS_LABELS.get(status, (status, "pending"))
        standard = inv_mod.STANDARD_LABELS[page["since"]]
        is_html = self.env.app.builder.format == "html"

        badges: list[Any] = []
        if is_html:
            badges.append(
                nodes.raw(
                    "",
                    f'<span class="kc-badge kc-badge--{css}">{html.escape(label)}</span>',
                    format="html",
                )
            )
            badges.append(
                nodes.raw(
                    "",
                    f'<span class="kc-badge kc-badge--std">{html.escape(standard)}+</span>',
                    format="html",
                )
            )
            if status in inv_mod.DONE_STATUSES and not page.get("reviewed", False):
                badges.append(
                    nodes.raw(
                        "",
                        '<span class="kc-badge kc-badge--review">រង់ចាំត្រួតពិនិត្យបច្ចេកទេស</span>',
                        format="html",
                    )
                )
        else:
            badges.append(nodes.Text(f"[{label}] [{standard}+] "))

        container = nodes.container(classes=["kc-meta"])
        container += _paragraph(badges)

        sources = page.get("sources", [])
        if sources:
            items: list[Any] = [nodes.Text("ប្រភពយោង៖ ")]
            for index, url in enumerate(sources):
                if index:
                    items.append(nodes.Text(" · "))
                items.append(nodes.reference("", url, refuri=url))
            container += _paragraph(items)

        feedback = self._feedback_href()
        if feedback:
            container += _paragraph(
                [
                    nodes.reference("", "ផ្តល់មតិ ឬរាយការណ៍បញ្ហាសម្រាប់ទំព័រនេះ", refuri=feedback),
                ]
            )
        return [container]

    def _feedback_href(self) -> str:
        if self.env.app.builder.format != "html":
            return ""
        feedback_doc = self.env.config.khmer_feedback_doc
        try:
            uri = self.env.app.builder.get_relative_uri(self.env.docname, feedback_doc)
        except Exception:  # pragma: no cover - defensive, builder specific
            return ""
        repo = (self.env.config.khmer_repo_url or "").rstrip("/")
        if repo:
            return f"{repo}/issues/new?title=Feedback%3A+{self.env.docname}"
        return uri


class ProgressDashboard(SphinxDirective):
    """Render the whole translation dashboard from live project data."""

    has_content = False

    def run(self):
        self.env.note_dependency(str(inv_mod.INVENTORY_PATH))
        stats = stats_mod.compute(self.env.app.khmer_inventory)
        totals = stats["totals"]
        container = nodes.container(classes=["kc-dashboard"])

        container += nodes.paragraph(
            text=f"ស្ថិតិគណនាដោយស្វ័យប្រវត្តិពី data/inventory.json នៅ {stats['generated_at']}។ "
            "គ្មានលេខណាមួយត្រូវបានសរសេរដោយដៃទេ។"
        )

        summary_rows = [
            ["ចំនួនទំព័រត្រូវការសរុប", str(totals["required"]), "រាល់ទំព័រក្នុងផែនការឯកសារ"],
            ["បានបកប្រែរួច", str(totals["translated"]), "មានឯកសារខ្មែរពិតប្រាកដ"],
            ["បានផ្ទៀងផ្ទាត់បច្ចេកទេស", str(totals["verified"]), "ឆ្លងកាត់ការត្រួតពិនិត្យ"],
            ["រង់ចាំត្រួតពិនិត្យ", str(totals["awaiting_review"]), "បកប្រែរួច មិនទាន់ verify"],
            ["កំពុងបកប្រែ", str(totals["in_progress"]), "កំពុងដំណើរការ"],
            ["រង់ចាំបកប្រែ", str(totals["pending"]), "មិនទាន់ចាប់ផ្ដើម"],
            ["បរាជ័យ ឬខ្វះឯកសារ", str(totals["failed"]), "ស្ថានភាពមិនត្រូវនឹងឯកសារ"],
            ["ភាគរយសម្រេច", f"{totals['completion_pct']}%", "បានបកប្រែ ÷ ត្រូវការ"],
        ]
        container += _table(
            ["សូចនាករ", "តម្លៃ", "អត្ថន័យ"], summary_rows, widths=[5, 2, 6]
        )

        track_rows = [
            [
                track["title_km"],
                str(track["total"]),
                str(track["translated"]),
                str(track["verified"]),
                str(track["pending"]),
                f"{track['completion_pct']}%",
            ]
            for track in stats["tracks"]
        ]
        container += nodes.paragraph(text="វឌ្ឍនភាពតាមផ្នែក")
        container += _table(
            ["ផ្នែក", "ទំព័រ", "បកប្រែ", "ផ្ទៀងផ្ទាត់", "រង់ចាំ", "%"],
            track_rows,
            widths=[5, 2, 2, 2, 2, 2],
        )

        source_rows = [
            ["ទំព័រដែលមានប្រភពយោង", str(stats["sources"]["pages_with_sources"])],
            ["URL ប្រភពតែមួយគត់", str(stats["sources"]["unique_urls"])],
            ["គំរូកូដសរុប", str(stats["examples"].get("total", 0))],
            ["គំរូកូដដែលបានបកប្រែដោយជោគជ័យ", str(stats["examples"].get("passed", 0))],
            ["តួអក្សរខ្មែរសរុប", f"{stats['khmer']['characters']:,}"],
        ]
        container += nodes.paragraph(text="គុណភាព និងប្រភព")
        container += _table(["សូចនាករ", "តម្លៃ"], source_rows, widths=[8, 3])

        if stats["problems"]:
            container += nodes.paragraph(
                text="បញ្ហាដែលរកឃើញ (ទំព័រទាំងនេះមិនត្រូវរាប់ចូលក្នុងភាគរយទេ)"
            )
            container += _table(
                ["ទំព័រ", "បញ្ហា"],
                [[item["id"], item["problem"]] for item in stats["problems"]],
                widths=[6, 5],
            )

        if stats["pending_pages"]:
            container += nodes.paragraph(
                text=f"ទំព័រដែលនៅសល់ ({len(stats['pending_pages'])})"
            )
            bullet = nodes.bullet_list()
            for item in stats["pending_pages"]:
                entry = nodes.list_item()
                entry += nodes.paragraph(text=f"{item['title_km']} — {item['id']}")
                bullet += entry
            container += bullet

        return [container]


class TrackPages(SphinxDirective):
    """List every planned page of one track with its real translation status.

    Pages that are not translated yet are listed as plain text, so the table
    never contains a broken link.
    """

    required_arguments = 1
    has_content = False

    def run(self):
        inventory = self.env.app.khmer_inventory
        track_id = self.arguments[0].strip()
        if track_id not in {track["id"] for track in inventory["tracks"]}:
            raise self.error(f"unknown track: {track_id}")
        self.env.note_dependency(str(inv_mod.INVENTORY_PATH))
        is_html = self.env.app.builder.format == "html"

        table = nodes.table()
        tgroup = nodes.tgroup(cols=3)
        table += tgroup
        for width in (7, 3, 3):
            tgroup += nodes.colspec(colwidth=width)
        thead = nodes.thead()
        tgroup += thead
        head_row = nodes.row()
        for title in ("ទំព័រ", "ស្ថានភាព", "ស្តង់ដារ"):
            entry = nodes.entry()
            entry += nodes.paragraph(text=title)
            head_row += entry
        thead += head_row
        tbody = nodes.tbody()
        tgroup += tbody

        for page in inv_mod.track_pages(inventory, track_id):
            file_path = inv_mod.page_file(page["id"])
            done = page["status"] in inv_mod.DONE_STATUSES and file_path.is_file()
            title_entry = nodes.entry()
            if done and is_html:
                uri = self.env.app.builder.get_relative_uri(
                    self.env.docname, page["id"]
                )
                title_entry += _paragraph(
                    [nodes.reference("", page["title_km"], refuri=uri)]
                )
            else:
                suffix = "" if done else ""
                title_entry += nodes.paragraph(text=page["title_km"] + suffix)
            status_label = STATUS_LABELS.get(page["status"], (page["status"], ""))[0]
            if page["status"] in inv_mod.DONE_STATUSES and not file_path.is_file():
                status_label = STATUS_LABELS["failed"][0]
            status_entry = nodes.entry()
            status_entry += nodes.paragraph(text=status_label)
            std_entry = nodes.entry()
            std_entry += nodes.paragraph(
                text=inv_mod.STANDARD_LABELS[page["since"]] + "+"
            )
            row = nodes.row()
            row += title_entry
            row += status_entry
            row += std_entry
            tbody += row

        return [table]


class TerminologyTable(SphinxDirective):
    """Render the enforced glossary from data/terminology.json."""

    has_content = False

    def run(self):
        from khmercpp.validate import TERMINOLOGY_PATH, load_terminology

        self.env.note_dependency(str(TERMINOLOGY_PATH))
        terminology = load_terminology()
        rows = sorted(
            ([term["km"], term["en"]] for term in terminology["terms"]),
            key=lambda row: row[0],
        )
        table = _table(["ពាក្យខ្មែរ", "ពាក្យអង់គ្លេស"], rows, widths=[4, 4])

        protected = nodes.bullet_list()
        for token in terminology["never_translate"]:
            item = nodes.list_item()
            paragraph = nodes.paragraph()
            paragraph += nodes.literal(text=token)
            item += paragraph
            protected += item
        caption = nodes.paragraph(
            text="ពាក្យ និងនិមិត្តសញ្ញាខាងក្រោមត្រូវរក្សាជាភាសាអង់គ្លេសដើម ហើយមិនត្រូវបកប្រែឡើយ៖"
        )
        return [table, caption, protected]


class SourceList(SphinxDirective):
    """List every page with its authoritative sources (attribution table)."""

    has_content = False

    def run(self):
        self.env.note_dependency(str(inv_mod.INVENTORY_PATH))
        inventory = self.env.app.khmer_inventory
        items: list[nodes.bullet_list] = []
        container = nodes.container(classes=["kc-sources"])
        bullet = nodes.bullet_list()
        for page in inventory["pages"]:
            if not page.get("sources"):
                continue
            entry = nodes.list_item()
            paragraph = nodes.paragraph()
            paragraph += nodes.strong(text=page["title_km"])
            paragraph += nodes.Text(" — ")
            for index, url in enumerate(page["sources"]):
                if index:
                    paragraph += nodes.Text(" · ")
                paragraph += nodes.reference("", url, refuri=url)
            entry += paragraph
            bullet += entry
            items.append(bullet)
        if not items:
            container += nodes.paragraph(text="មិនទាន់មានប្រភពយោងដែលបានកត់ត្រាទេ។")
            return [container]
        container += bullet
        return [container]


def _load(app, config) -> None:
    app.khmer_inventory = inv_mod.load()


def _page_context(app, pagename, templatename, context, doctree):
    page = app.khmer_pages.get(pagename)
    if not page:
        return
    context["kc_page"] = page
    meta = (
        f'<meta name="cpp-standard" content="{html.escape(page["since"])}">\n'
        f'<meta name="translation-status" content="{html.escape(page["status"])}">\n'
    )
    context["metatags"] = context.get("metatags", "") + meta


def _write_index(app, exception) -> None:
    if exception is not None or app.builder.format != "html":
        return
    inventory = app.khmer_inventory
    index = {
        "standards": [
            {"id": name, "label": inv_mod.STANDARD_LABELS[name]} for name in inv_mod.STANDARDS
        ],
        "tracks": {
            track["id"]: {"title_km": track["title_km"], "doc": track["doc"]}
            for track in inventory["tracks"]
        },
        "pages": {
            page["id"]: {
                "title_km": page["title_km"],
                "track": page["id"].split("/", 1)[0],
                "since": page["since"],
                "status": page["status"],
                "status_label": STATUS_LABELS.get(page["status"], (page["status"], ""))[0],
            }
            for page in inventory["pages"]
        },
    }
    target = app.outdir / "_static" / "khmer-index.json"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(index, ensure_ascii=False), encoding="utf-8")
    # Keep a committed snapshot of the live numbers for README badges and CI.
    try:
        stats_mod.write_snapshot(stats_mod.compute(inventory))
    except OSError:
        pass


def setup(app):
    app.add_config_value("khmer_repo_url", "", "html")
    app.add_config_value("khmer_feedback_doc", "feedback", "html")
    app.add_directive("translation-meta", TranslationMeta)
    app.add_directive("progress-dashboard", ProgressDashboard)
    app.add_directive("track-pages", TrackPages)
    app.add_directive("terminology-table", TerminologyTable)
    app.add_directive("source-list", SourceList)
    app.connect("builder-inited", _set_pages)
    app.connect("config-inited", _load)
    app.connect("html-page-context", _page_context)
    app.connect("build-finished", _write_index)
    return {"parallel_read_safe": True, "parallel_write_safe": True, "version": "1.0"}


def _set_pages(app) -> None:
    app.khmer_pages = inv_mod.pages_by_id(app.khmer_inventory)
