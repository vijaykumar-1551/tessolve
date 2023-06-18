# Variables
VENV           = .venv
VENV_PYTHON    = $(VENV)/bin/python
SYSTEM_PYTHON  = $(or $(shell which python3), $(shell which python))
PYTHON         = $(or $(wildcard $(VENV_PYTHON)), $(SYSTEM_PYTHON))

## Dev/build environment

$(VENV_PYTHON):
    rm -rf $(VENV)
    $(SYSTEM_PYTHON) -m venv $(VENV)

venv: $(VENV_PYTHON)


deps: venv
    $(PYTHON) -m pip install --upgrade pip
    $(PYTHON) -m pip install -r requirements.txt

.PHONY: venv deps

## Lint, test

test:
    $(PYTHON) -m tox

lint:
    $(PYTHON) -m tox -e lint

lintfix:

.PHONY: test lint lintfix

## Build source distribution, install

# sdist:
#     $(PYTHON) setup.py sdist

install:
    $(SYSTEM_PYTHON) -m pip install .

.PHONY: build install

## Clean

clean:
    rm -rf .tox *.egg-info dist

.PHONY: clean
