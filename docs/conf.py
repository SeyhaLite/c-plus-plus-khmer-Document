"""Sphinx configuration for the Khmer C++ documentation.

The site is a normal Sphinx project so that it builds on the free Read the Docs
tier. Everything language specific (search tokenisation, translation badges,
live statistics) lives in ``sphinxext/`` and ``khmercpp/`` in the repository
root, which is why the root is added to ``sys.path`` below.
"""

from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.abspath(".."))

project = "ឯកសារ C++ ជាភាសាខ្មែរ"
author = "អ្នករួមចំណែកឯកសារ C++ ខ្មែរ"
copyright = (
    "2026, អ្នករួមចំណែកឯកសារ C++ ខ្មែរ។ "
    "ខ្លឹមសារខ្មែរ និងគំរូកូដ៖ CC BY-SA 3.0។ "
    "C++ ជាពាណិជ្ជសញ្ញា និងរក្សាសិទ្ធិដោយ ISO/IEC។"
)
release = "0.3.0"
version = "0.3"

#: Khmer UI, Khmer search tokenisation (custom), and C++ syntax highlighting.
language = "km"
html_search_language = "km"
# Khmer translations for Sphinx/Furo interface strings (neither ships a km
# catalogue). Sphinx compiles these .po files during the build.
locale_dirs = ["locale/"]
highlight_language = "cpp"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinxext.khmerdocs",
    "sphinxext.kmsearch",
]

source_suffix = {".md": "markdown", ".rst": "restructuredtext"}
root_doc = "index"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "fieldlist",
    "tasklist",
    "attrs_inline",
]
myst_heading_anchors = 3

# --- Theme ---------------------------------------------------------------
html_theme = "furo"
html_title = "ឯកសារ C++ ជាភាសាខ្មែរ"
html_short_title = "C++ ខ្មែរ"
html_meta = {
    "description": (
        "ឯកសាររៀន និងឯកសារយោង C++ ជាភាសាខ្មែរ ពីមេរៀនមូលដ្ឋានដល់កម្រិតខ្ពស់ "
        "រួមមានការពន្យល់ ឧទាហរណ៍កូដ និងប្រភពបច្ចេកទេសដែលអាចផ្ទៀងផ្ទាត់បាន។"
    ),
    "keywords": "C++, C++ Khmer, រៀន C++, ឯកសារ C++ ជាភាសាខ្មែរ",
}
html_static_path = ["_static"]
html_css_files = ["khmer.css"]
html_js_files = ["translation-ui.js"]
html_show_sourcelink = False
html_copy_source = False
html_last_updated_fmt = ""

html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "light_css_variables": {
        "font-stack": (
            "'Kantumruy Pro', 'Noto Sans Khmer', 'Khmer OS Battambang', "
            "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif"
        ),
        "font-stack--monospace": (
            "'JetBrains Mono', 'Kantumruy Pro', 'Noto Sans Khmer', "
            "ui-monospace, SFMono-Regular, Menlo, monospace"
        ),
        "color-brand-primary": "#0f5fa8",
        "color-brand-content": "#0f5fa8",
    },
    "dark_css_variables": {
        "color-brand-primary": "#72b7f2",
        "color-brand-content": "#72b7f2",
    },
}

html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
    ]
}

# --- Project specific ----------------------------------------------------
#: Used by the per-page feedback link. Leave empty to point readers at the
#: local feedback page instead of a GitHub issue form.
khmer_repo_url = os.environ.get("KHMER_CPP_REPO_URL", "")
khmer_feedback_doc = "feedback"

copybutton_prompt_text = r"^\$ "
copybutton_prompt_is_regexp = True
copybutton_only_copy_prompt_lines = False

linkcheck_ignore = [
    r"https://en\.cppreference\.com/w/.*",  # rate limited for automated clients
    r"https://eel\.is/.*",
]
linkcheck_timeout = 20

nitpicky = False
suppress_warnings: list[str] = []
