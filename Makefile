PYTHON ?= .venv/bin/python
SPHINX  = $(PYTHON) -m sphinx

.PHONY: help install html strict serve examples validate verify progress clean check html-links

help:
	@echo "make install   install dependencies into .venv"
	@echo "make html      build the documentation (docs/_build/html)"
	@echo "make strict    build with warnings treated as errors"
	@echo "make serve     serve the built site on http://localhost:8000"
	@echo "make examples  compile and run every C++ example"
	@echo "make validate  run all content validators"
	@echo "make verify    validate + examples + statistics snapshot"
	@echo "make check     everything CI runs (strict build + HTML link check)"
	@echo "make html-links check generated HTML for duplicated .html suffixes"
	@echo "make clean     remove build output"

install:
	python3 -m venv .venv
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install -r requirements.txt

html:
	$(SPHINX) -b html docs docs/_build/html

strict:
	$(SPHINX) -b html -W docs docs/_build/html

serve:
	$(PYTHON) -m http.server 8000 --directory docs/_build/html

examples:
	$(PYTHON) scripts/check_examples.py

validate:
	$(PYTHON) scripts/pipeline.py validate --verbose

verify:
	$(PYTHON) scripts/pipeline.py verify

progress:
	$(PYTHON) scripts/pipeline.py status --write

html-links:
	$(PYTHON) scripts/check_html_links.py docs/_build/html

check:
	$(PYTHON) scripts/pipeline.py validate --strict
	$(PYTHON) scripts/check_examples.py --strict
	$(SPHINX) -b html -W docs docs/_build/html
	$(PYTHON) scripts/check_html_links.py docs/_build/html

clean:
	rm -rf docs/_build
