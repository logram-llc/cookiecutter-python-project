# cookiecutter-python-project

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for modern Python projects

## Toolkit

* [isort](https://pycqa.github.io/isort/) - Import sorting
* [mypy](https://mypy-lang.org/) - Static type checking
* [Ruff](https://github.com/charliermarsh/ruff) - Code linter
* [Black](https://github.com/psf/black) - Code formatter
* [Tox](https://github.com/tox-dev/tox) - Manage virtual environments for tests
* [pytest](https://docs.pytest.org/) - Testing framework
* [sphinx](https://www.sphinx-doc.org/en/master/) - Autogen documentation from Python type hints and docstrings
* GitHub workflows to automate format checks, lint checks, tests, build docs, and more on push.

## Quick Start

### Setup
```bash
pip install -U cookiecutter
cookiecutter https://github.com/logram-llc/cookiecutter-python-project
cd my-project/
```

### Run Checks
```bash
pip install .[testing]

# Run Checks
tox -e format-check,isort-check,lint-check,pytest-check

# Run autofix for formatters, linters, and isort
tox -e format-fix,isort-fix,lint-fix
```
Most Tox test enviornments have a `*-check` and a `*-fix` variant. `format-check`, for example, will test whether the project's code is properly formatted. `format-fix` will fix the code's formatting. The same applies to other Tox test enviornments. See [tox.ini](/%7B%7Bcookiecutter.project%7D%7D/tox.ini) for more.

Alternatively, you can run these checks without Tox:
```
pip install .[dev]

black ./
ruff --respect-gitignore --fix ./
isort ./
```

### Run Tests

```bash
pip install .[testing]

# Run pytest
tox -e pytest-check -- -m "unit"
tox -e pytest-cov
```

### Build Docs

```bash
pip install .[docs]
cd docs/
make html
# Your docs will be generated under the `version/` subdirectory.
```

## Caveats

### `pyproject.toml` Incompatibility w/ Poetry

In an effort to conform to [PEP 621](https://peps.python.org/pep-0621/) and [631](https://peps.python.org/pep-0631/), the generated `pyproject.tml` is not compatible with [Poetry](https://python-poetry.org/) ([see issue](https://github.com/python-poetry/poetry/issues/3332)). If you want Poetry support, you will need to regenerate the `pyproject.toml` file and start from scratch or modify it manually.