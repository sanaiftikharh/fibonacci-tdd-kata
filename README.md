# Fibonacci TDD Kata

A complete Python implementation of the Fibonacci sequence developed using Test-Driven Development. The project demonstrates:

- Red-Green-Refactor development
- Unit testing with pytest
- Iterative and fast-doubled Fibonacci implementations
- A reusable Python API
- A command-line interface
- Interactive Marimo notebooks
- Static typing and linting
- Automated testing and coverage
- GitHub Pages deployment
- PyPI package publication

## Project Status

The project is packaged as `fibonaccii-kata` version `0.1.0`.

[![Tests](https://github.com/sanaiftikharh/fibonacci-tdd-kata/actions/workflows/tests.yml/badge.svg)](https://github.com/sanaiftikharh/fibonacci-tdd-kata/actions/workflows/tests.yml)
[![Publish package](https://github.com/sanaiftikharh/fibonacci-tdd-kata/actions/workflows/publish.yml/badge.svg)](https://github.com/sanaiftikharh/fibonacci-tdd-kata/actions/workflows/publish.yml)
[![Deploy Pages](https://github.com/sanaiftikharh/fibonacci-tdd-kata/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/sanaiftikharh/fibonacci-tdd-kata/actions/workflows/deploy-pages.yml)

## Interactive Demo

Explore Fibonacci values in the deployed Marimo notebook:

[Open the Fibonacci demo](https://sanaiftikharh.github.io/fibonacci-tdd-kata/)

## Fibonacci Rules

The sequence starts with:

```text
F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2)
```

Examples:

```text
F(0)  -> 0
F(1)  -> 1
F(2)  -> 1
F(5)  -> 5
F(10) -> 55
F(20) -> 6765
```

Negative indices raise `ValueError`.

## Requirements

- Python 3.11 or newer
- `uv`

The project uses:

- pytest and pytest-cov
- Ruff
- mypy
- Marimo
- Matplotlib
- Hatchling
- GitHub Actions

## Installation

### From the repository

```bash
git clone https://github.com/sanaiftikharh/fibonacci-tdd-kata.git
cd fibonacci-tdd-kata
uv sync --all-groups
```

### From PyPI

```bash
python -m pip install fibonaccii-kata
```

## Python API

The package exposes both Fibonacci functions from the package root:

```python
from fibonacci_kata import fibonacci, fibonacci_mod

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(10) == 55
assert fibonacci_mod(10) == 55
assert fibonacci_mod(10**18, 1_000_000_000) == 560546875
```

You can also import the implementation directly:

```python
from fibonacci_kata.core import fibonacci, fibonacci_mod
```

### Standard Fibonacci

`fibonacci(n)` uses an iterative implementation and returns `F(n)`:

```python
fibonacci(0)  # 0
fibonacci(1)  # 1
fibonacci(5)  # 5
fibonacci(10)  # 55
fibonacci(20)  # 6765
```

Negative indices raise `ValueError`:

```python
fibonacci(-1)  # ValueError
```

### Fast Modular Fibonacci

`fibonacci_mod(n, m)` uses fast doubling and returns `F(n) mod m`:

```python
fibonacci_mod(100, 1_000_000_000)  # Modular result
fibonacci_mod(10**18, 1_000_000_000) == 560546875
```

The default modulus is `1_000_000_000`:

```python
fibonacci_mod(20) == 6765
```

The function raises `ValueError` when:

- `n` is negative;
- `m` is zero or negative.

## Command-Line Interface

The package provides the `fibonacci-kata` command:

```bash
uv run fibonacci-kata 10
```

Output:

```text
55
```

### Single index

```bash
uv run fibonacci-kata 0
uv run fibonacci-kata 1
uv run fibonacci-kata 5
uv run fibonacci-kata 10
```

### Inclusive range

```bash
uv run fibonacci-kata --start 0 --end 10
```

The range prints one Fibonacci value per line:

```text
0
1
1
2
3
5
8
13
21
34
55
```

### CLI help

```bash
uv run fibonacci-kata --help
```

The CLI requires either:

- one positional index; or
- both `--start` and `--end`.

## Marimo Notebooks

### Fibonacci Explorer

The explorer consumes the installed `fibonacci_kata` package and does not duplicate the core implementation.

```bash
uv run marimo edit notebooks/fibonacci_explorer.py
```

It provides:

- configurable range start and end sliders;
- live Fibonacci values;
- an interactive Matplotlib chart;
- direct use of the packaged `fibonacci` function.

### TDD Demonstration

The TDD notebook demonstrates the development process with tests and implementations for:

- Fibonacci base cases;
- iterative Fibonacci values;
- modular Fibonacci base cases;
- fast-doubling modular values;
- very large indices.

Run it with:

```bash
uv run marimo edit notebooks/tdd_fibonacci_marimo_en.py
```

## Test-Driven Development

The kata follows the Red-Green-Refactor cycle:

1. Write a failing test.
2. Implement the smallest behavior required to pass.
3. Run all tests to detect regressions.
4. Refactor only after the tests are green.
5. Repeat for the next behavior.

### Iterative implementation

The standard implementation uses a small iterative loop:

```python
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must be non-negative")

    if n <= 1:
        return n

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b
```

### Fast-doubling implementation

The modular implementation uses recursive fast doubling:

```python
F(2k) = F(k) * (2F(k+1) - F(k))
F(2k+1) = F(k+1)^2 + F(k)^2
```

This allows computations for very large indices such as `10**18` without constructing the complete sequence.

The tests cover:

- base cases;
- small Fibonacci values;
- negative input;
- modular base cases;
- modular range validation;
- modular small values;
- very large indices;
- invalid modulus values;
- single-number CLI output;
- CLI ranges;
- parser behavior;
- missing CLI arguments.

## Testing

Install the development dependencies:

```bash
uv sync --all-groups
```

Run the test suite:

```bash
uv run pytest
```

Run coverage:

```bash
uv run pytest --cov=src --cov-report=term-missing --cov-report=xml
```

Run formatting:

```bash
uv run ruff format --check .
```

Run lint checks:

```bash
uv run ruff check .
```

Run strict type checking:

```bash
uv run mypy src
```

The pytest configuration:

- discovers tests in `tests/`;
- adds `src/` to the Python import path;
- requires at least 90% coverage.

## Project Structure

```text
fibonacci-tdd-kata/
├── .github/
│   └── workflows/
│       ├── deploy-pages.yml
│       ├── publish.yml
│       └── tests.yml
├── notebooks/
│   ├── fibonacci_explorer.py
│   └── tdd_fibonacci_marimo_en.py
├── src/
│   └── fibonacci_kata/
│       ├── __init__.py
│       ├── cli.py
│       └── core.py
├── tests/
│   ├── test_cli.py
│   └── test_core.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## Continuous Integration

GitHub Actions tests pushes and pull requests targeting `main` with:

- Python 3.11
- Python 3.12
- Python 3.13
- Ruff formatting
- Ruff linting
- mypy strict type checking
- pytest
- coverage reporting

The coverage threshold is configured as 90% in `pyproject.toml`.

## GitHub Pages

The Marimo explorer can be exported as a WebAssembly-powered static site:

```bash
uv run marimo check notebooks/fibonacci_explorer.py --select MW
uv run marimo export html-wasm \
  notebooks/fibonacci_explorer.py \
  -o site \
  --mode run
```

The `deploy-pages.yml` workflow:

1. runs the test workflow;
2. installs dependencies;
3. validates the notebook;
4. exports the notebook to `site/`;
5. uploads the Pages artifact;
6. deploys it to GitHub Pages.

## Package Publication

The project uses trusted PyPI publishing.

A GitHub release triggers:

1. the reusable test workflow;
2. package construction with Hatchling;
3. publication using `pypa/gh-action-pypi-publish@release/v1`.

Package metadata is declared in `pyproject.toml`, including:

- package name;
- package version;
- Python requirement;
- MIT license declaration;
- CLI entry point;
- build backend;
- development dependencies;
- pytest, Ruff, mypy, and coverage settings.

## Development Workflow

Use issue-based branches and pull requests:

```bash
git switch main
git pull origin main
git switch -c feature/your-feature
```

Recommended workflow:

1. Create a GitHub issue.
2. Create a focused branch from `main`.
3. Add a failing test.
4. Implement the smallest passing change.
5. Run all local quality checks.
6. Commit the change using an imperative commit subject.
7. Open a pull request against `main`.
8. Merge only after the CI workflow passes.

Use issue-closing commit or pull-request text where appropriate:

```text
Closes #issue-number
```

## Commit History Highlights

The repository history shows the assignment workflow:

- package publishing workflow creation;
- test automation;
- code-quality checks;
- Marimo notebook exploration;
- CLI exposure;
- notebook deployment fixes;
- GitHub Pages project-site deployment;
- branch, merge, revert, and refactor activity.

## Author

**Sana Iftikhar**

- GitHub: [@sanaiftikharh](https://github.com/sanaiftikharh)
- Repository: [github.com/sanaiftikharh/fibonacci-tdd-kata](https://github.com/sanaiftikharh/fibonacci-tdd-kata)
