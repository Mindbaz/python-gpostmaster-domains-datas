PY_PACKAGE:=googlepostmasterapi
ROOT_DIR:=$(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
ROOT_NAME:=$(shell basename ${ROOT_DIR})
PARENT_DIR:=$(shell dirname ${ROOT_DIR})
TEST_FILES:=$(shell find ./tests/ -iname "*Test.py" | tr '\n' ',' | sed -e 's/,$$//g')
SPHINXOPTS?=
SPHINXBUILD?=sphinx-build
SOURCEDIR=docs/
BUILDDIR=docs/
PYTHON=python

all: run

run:

test: tests coverage

coverage:
	nosetests --with-coverage --cover-package="${PY_PACKAGE}" --cover-html --cover-html-dir="reports" --tests "${TEST_FILES}"

tests:
	nosetests --with-xunit --xunit-file="nosetests.xml" --tests "${TEST_FILES}"

syntax-check-python:
	@python -m py_compile $(shell find ./ -not \( -path ./tests -prune \) -iname "*.py" ! -iname "__init__.py" -type f)

syntax-check: syntax-check-python

valid-full-coverage: ; $(eval PERCENT_COVERAGE=$(shell nosetests --with-coverage --cover-package="${PY_PACKAGE}" --cover-html --cover-html-dir="reports" --tests "${TEST_FILES}" 2>&1 | grep -E "^TOTAL" | awk '{ print $$4 }'))
	@if [ "$(PERCENT_COVERAGE)" != "100%" ]; then false; fi

compile:
	## To use it : make target=<TARGET> deploy
	python setup.py sdist upload -r $(target)

.PHONY: docs
docs:
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS)

deploy: compile clean

auto-clean: clean

clean:
	@echo ">> Remove python compilation : *.pyc / pycache / build / dist / egg"
	@find . -iname "*.pyc" -exec rm {} \;
	@find . -iname "\_\_pycache\_\_" -type d -exec rm -rf {} \; 2>/dev/null ; true
	@find . -iname "*-info" -type d -exec rm -rf {} \; 2>/dev/null ; true
	@find . -iname "build" -type d -exec rm -rf {} \; 2>/dev/null ; true
	@find . -iname "dist" -type d -exec rm -rf {} \; 2>/dev/null ; true
	@echo ">> Remove other compilation : java / nosetests / coverage"
	@find . -iname "*.java" -exec rm {} \; 2>/dev/null ; true
	@rm -rf reports/ nosetests.xml .coverage
