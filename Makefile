PY		:= python3
PROJECT	:= $(shell basename $(PWD))

.PHONY: all
all:
	$(PY) run.py

.PHONY: test
test:
	pytest

.PHONY: docs
docs:
	sphinx-build -b html -d _build/doctrees . _build/html

