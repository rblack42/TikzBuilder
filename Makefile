PY		:= python3
PROJECT	:= $(shell basename $(PWD))

.PHONY: all
all:
	$(PY) run.py

.PHONY: test
test:
	pytest test_setup.py tests/*

.PHONY: docs
docs:
	sphinx-build -b html -d _tmp/_build/doctrees . docs

