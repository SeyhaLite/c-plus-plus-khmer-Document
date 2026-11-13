"""Khmer full-text search support for Sphinx.

Khmer is written without spaces between words, so Sphinx's default word
splitter (``\\w+``) indexes whole sentences as single tokens and search returns
nothing.  This language splits Khmer runs into overlapping two-code-point
shingles and keeps Latin/C++ identifiers as lower-cased words.

Indexing (Python, :meth:`SearchKhmer.split`) and query splitting (JavaScript,
``splitQuery`` below) use exactly the same rule, which is what makes matching
work.  Shingles trade a slightly larger index for substring recall, which is
the right trade-off for a documentation site of this size.
"""

from __future__ import annotations

import re

from sphinx.search import SearchLanguage, languages

#: Khmer block + Khmer symbols.
KHMER_RANGE = "\u1780-\u17ff\u19e0-\u19ff"
SHINGLE = 2

#: One pass over the text: Khmer runs, or Latin/digit/identifier words.
_TOKEN_RE = re.compile(
    rf"(?P<khmer>[{KHMER_RANGE}]+)"
    r"|(?P<word>[0-9A-Za-z_][0-9A-Za-z_+#]*)"
    r"|(?P<punct>[+#]+)"
)

JS_SPLITTER = """
/**
 * Khmer aware query splitter (mirrors sphinxext.kmsearch.SearchKhmer.split).
 * Khmer runs become overlapping 2-code-point shingles; Latin words are kept
 * verbatim but lower-cased.
 */
var KHMER_SHINGLE_SIZE = %(shingle)d;
function splitQuery(query) {
  var out = [];
  var re = /([\\u1780-\\u17ff\\u19e0-\\u19ff]+)|([0-9A-Za-z_][0-9A-Za-z_+#]*)|([+#]+)/g;
  var match;
  while ((match = re.exec(query)) !== null) {
    if (match[1]) {
      var run = match[1];
      if (run.length < KHMER_SHINGLE_SIZE) {
        out.push(run);
      } else {
        for (var i = 0; i + KHMER_SHINGLE_SIZE <= run.length; i += 1) {
          out.push(run.slice(i, i + KHMER_SHINGLE_SIZE));
        }
      }
    } else if (match[2] || match[3]) {
      out.push((match[2] || match[3]).toLowerCase());
    }
  }
  return out;
}
""" % {"shingle": SHINGLE}


class SearchKhmer(SearchLanguage):
    """Search preprocessor for Khmer documentation."""

    lang = "km"
    language_name = "Khmer"
    js_splitter_code = JS_SPLITTER
    stopwords: frozenset[str] = frozenset()

    def split(self, input: str) -> list[str]:  # noqa: A002 - Sphinx API name
        tokens: list[str] = []
        for match in _TOKEN_RE.finditer(input):
            khmer = match.group("khmer")
            if khmer:
                if len(khmer) < SHINGLE:
                    tokens.append(khmer)
                else:
                    tokens.extend(
                        khmer[i : i + SHINGLE] for i in range(len(khmer) - SHINGLE + 1)
                    )
                continue
            word = match.group("word") or match.group("punct")
            if word:
                tokens.append(word.lower())
        return tokens


def setup(app):
    """Register the Khmer search language with Sphinx."""
    languages["km"] = SearchKhmer
    return {"parallel_read_safe": True, "parallel_write_safe": True}
