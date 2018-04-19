PY		:= python3
PROJECT	:= $(shell basename $(PWD))

.PHONY: all
all:
	$(PY) ./tikzbuild

.PHONY: test
test:
	pytest test_setup.py tests/*

.PHONY: docs
docs:
	sphinx-build -b html -d _tmp/_build/doctrees . docs

.PHONY: clean
clean:
	$(RM) *.aux *.log *.pdf *.tex *.gz
	$(RM) examples/*.aux examples/*.log examples/*.tex examples/*.pdf

