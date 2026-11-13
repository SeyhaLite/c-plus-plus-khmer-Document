# ឯកសារ C++ ជាភាសាខ្មែរ — Khmer C++ Documentation

A Khmer-language C++ learning and reference site built with Sphinx and hosted on
the free Read the Docs tier. Every technical claim is sourced to authoritative
C++ references, every code example is compiled and run in CI, and every number on
the progress dashboard is computed from the real files in this repository.

- Site content: **Khmer**. Code, keywords and identifiers stay in their original
  C++ form.
- Sources: [cppreference](https://en.cppreference.com/w/),
  [isocpp.org](https://isocpp.org/), the [C++ draft](https://eel.is/c++draft/)
  and [WG21](https://www.open-std.org/jtc1/sc22/wg21/).
- Licence: Khmer text and example code **CC BY-SA 3.0**; cppreference content is
  attributed per page and remains under its own CC BY-SA 3.0 / GFDL terms.

## Current status (measured, not estimated)

| Metric | Value |
| --- | --- |
| Required documentation pages | 71 |
| Pages translated into Khmer | 36 (50.7%) |
| Pages with compiled + executed examples | 36 |
| C++ example programs passing | 36 / 36 |
| Content validator errors / warnings | 0 / 0 |
| Tracks complete | Getting Started, Basics, Control Flow, Functions, OOP |
| Tracks still pending | Advanced, Standard Library, Reference, Practice |

These figures are regenerated on every build into `data/progress.json` and shown
live on the site at `/progress.html`. Nothing is hard-coded: a page only counts as
translated when its Markdown file exists, is valid UTF-8, contains at least 400
Khmer code points, carries a `translation-meta` directive and cites a source.

## What the site does

- Khmer UI, Khmer-friendly typography (Kantumruy Pro with local fallbacks), light
  and dark themes (Furo), responsive layout.
- **Working Khmer full-text search.** Khmer is written without spaces, so the
  default Sphinx word splitter indexes whole sentences. `sphinxext/kmsearch.py`
  registers a language that indexes overlapping two-code-point shingles, mirrored
  in JavaScript for query splitting. Searching `អថេរ` finds `អថេរ` inside prose.
- **C++ standard selector** in the sidebar: hides pages whose feature is newer than
  the selected standard (e.g. C++11 hides C++20 topics). The choice persists.
- **Per-page translation badges**: status, minimum standard, sources, feedback link.
- **Live progress dashboard** rendered at build time from `data/inventory.json`.
- Breadcrumbs, previous/next navigation, table of contents, copy-code buttons.
- C++26 is always labelled **ព្រាង** (draft), never as a published standard.

## Layout

```
docs/                     Khmer content (MyST Markdown) + Sphinx config
sphinxext/khmerdocs.py    badges, track tables, glossary, sources, dashboard
sphinxext/kmsearch.py     Khmer search tokeniser (Python + JS)
khmercpp/                 inventory, statistics, validation, providers, examples
scripts/pipeline.py       translation pipeline CLI
scripts/check_examples.py compile + run every C++ example, verify EXPECT output
examples/                 real C++ programs; examples/<page-id>.cpp by convention
data/inventory.json       the single source of truth for page status and sources
data/terminology.json     enforced Khmer glossary (one word per concept)
data/progress.json        generated snapshot of live statistics
.readthedocs.yaml         Read the Docs build configuration
```

## Build locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

make html        # docs/_build/html
make serve       # http://localhost:8000
make check       # validate + examples + build with -W (what CI runs)
```

A C++ compiler is only needed for `make examples` / `make check`
(`g++`, `clang++`; the CI uses GCC 13).

## Translation pipeline

```bash
python scripts/pipeline.py status            # live statistics
python scripts/pipeline.py status --write    # refresh data/progress.json
python scripts/pipeline.py discover          # HTTP-check every source URL
python scripts/pipeline.py fetch --page basics/variables
python scripts/pipeline.py new --page basics/my-topic
python scripts/pipeline.py verify --page basics/my-topic
python scripts/pipeline.py verify --page basics/my-topic --accept
python scripts/pipeline.py validate --strict
```

`translate --provider openai` will draft a page through any OpenAI-compatible
endpoint using `KHMER_TRANSLATE_API_KEY` (or `OPENAI_API_KEY`) from the
environment. **Keys are never stored in the repository.** Automated drafts are
always written as `translated` but `unreviewed`; only `verify --accept` promotes a
page to `verified`, and it refuses when any check fails.

The pipeline never overwrites an existing non-empty page (`--force` required),
which is what makes resuming after an interruption safe.

## What "verified" means here

A page is marked `verified` only when all of the following hold:

1. Its file exists, is UTF-8, and has ≥ 400 Khmer code points.
2. Its `translation-meta` directive points at its own page id.
3. No Khmer appears inside inline code (syntax is never translated).
4. Every `literalinclude` and relative link resolves.
5. No banned terminology variant appears (`data/terminology.json`).
6. Every attached C++ example compiles with `-std=c++NN -Wall -Wextra -pedantic`
   and prints exactly the output in its `EXPECT` block.

`verified` is a *technical* gate (compiled code, resolving links, enforced
terminology, cited sources). It is not a claim of independent human linguistic
review — see Limitations below.

## Read the Docs deployment

1. Push this repository to GitHub.
2. On [readthedocs.org](https://readthedocs.org/) choose **Import a Project** and
   select the repository.
3. Read the Docs reads `.readthedocs.yaml`: Ubuntu 24.04, Python 3.12,
   `requirements.txt`, `docs/conf.py`. Its `pre_build` jobs run the validators and
   the C++ example checks, so a broken translation fails the deploy.
4. Press **Build version**. The site appears at
   `https://<project>.readthedocs.io/`.

The free tier includes automatic builds on push, hosting, and Read the Docs'
own version flyout. Build time and concurrency are limited per month; check the
current Read the Docs plan page before relying on larger limits, since their terms
change.

## Known limitations

- The Advanced, Standard Library, Reference and Practice tracks are **not
  translated yet**; their index pages say so explicitly and link to the dashboard.
- No independent human reviewer has proofread the Khmer text. The badges describe
  the automated technical gate above, not a second-person review.
- `discover` requires network access to cppreference; the sandbox used for this
  build may block it, in which case source URLs are recorded but not HTTP-checked.
- PDF/EPUB output is not configured: Khmer PDF rendering needs extra font setup
  that the free Read the Docs build does not provide out of the box.

## Contributing

Read `docs/contributing.md` (Khmer). In short: add an inventory entry, scaffold
the page, write the Khmer, attach a compiled example, then run
`python scripts/pipeline.py verify --page <id>` before opening a pull request.

## Attribution

cppreference.com content is licensed CC BY-SA 3.0 and GFDL; their terms ask for a
link back to cppreference.com, which appears on every translated page. The C++
standard is ISO/IEC copyright; this project provides original Khmer explanations,
not reproductions of the standard text.
