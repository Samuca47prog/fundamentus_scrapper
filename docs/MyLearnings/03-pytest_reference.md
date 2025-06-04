# Pytest Quick Reference for Developers Starting with Testing

This document summarizes best practices and technical patterns we've discussed while integrating `pytest` in a Python project. It's aimed at developers who are familiar with software development but just getting started with testing in `pytest`.

---

## ✅ Project Structure (src/ layout)

```
project-root/
├── src/
│   ├── main.py
│   ├── run_tests.py
│   ├── scrapper/
│   │   ├── __init__.py
│   │   └── parser.py
│   └── filters/
│       └── filters.py
├── tests/
│   └── test_parser.py
├── pyproject.toml
```

---

## ✅ Running Pytest with Output

- To see `print()` statements while running tests:

```bash
pytest -s
```

- To assert printed output:

```python
def test_output(capsys):
    print("Hello")
    captured = capsys.readouterr()
    assert "Hello" in captured.out
```

---

## ✅ Check DataFrame Column Type

Use `pandas.api.types` to check if a column is float:

```python
from pandas.api.types import is_float_dtype

def test_column_is_float():
    assert is_float_dtype(df["column_name"])
```

---

## ✅ Skipping Tests

- Skip a test unconditionally:

```python
import pytest

@pytest.mark.skip(reason="Temporarily disabled")
def test_skip_me():
    ...
```

- Conditionally skip a test:

```python
import sys

@pytest.mark.skipif(sys.platform != "win32", reason="Only runs on Windows")
def test_windows_only():
    ...
```

- Skip dynamically at runtime:

```python
def test_maybe_skip():
    import pytest
    if some_condition():
        pytest.skip("Condition not met")
```

---

## ✅ Common Pytest Decorators

- `@pytest.mark.skip(reason=...)`: unconditionally skip a test.
- `@pytest.mark.skipif(condition, reason=...)`: skip if a condition is true.
- `@pytest.mark.xfail`: test is expected to fail (won’t break the suite).
- `@pytest.mark.parametrize`: run the same test function with multiple sets of inputs.

Example using `parametrize`:

```python
import pytest

@pytest.mark.parametrize("a,b,result", [
    (2, 3, 5),
    (1, 1, 2),
])
def test_add(a, b, result):
    assert a + b == result
```

---

## ✅ PYTHONPATH with src/ Layout

If your project uses a `src/` layout, Python needs to know where to find the packages.

- Set PYTHONPATH at runtime:

```bash
PYTHONPATH=src pytest
```

- Or define it in `pytest.ini`:

```ini
[pytest]
pythonpath = src
```

---

## ✅ Data Directories in Tests

- Simple reusable function:

```python
from pathlib import Path

def get_data_dir():
    dir_ = Path(__file__).parent / "data"
    dir_.mkdir(exist_ok=True)
    return dir_
```

- Prefer `tmp_path` for isolated tests:

```python
def test_temp_file(tmp_path):
    file = tmp_path / "test.csv"
    ...
```

---

## ✅ Fixtures for Shared Setup

Use fixtures for reusable setup logic across multiple tests:

```python
import pytest
import pandas as pd

@pytest.fixture
def sample_dataframe():
    return pd.DataFrame({"value": [1.0, 2.5, 3.7]})
```

Then use it in your test:

```python
def test_mean(sample_dataframe):
    assert sample_dataframe["value"].mean() > 2
```

You can scope fixtures as `"function"`, `"module"`, `"session"` etc.

---

## ✅ pyproject.toml Configuration with Poetry

```toml
[tool.poetry.scripts]
main = "app.main:main"
tests = "app.run_tests:main"

[tool.poetry.packages]
packages = [
  { include = "scrapper", from = "src" },
  { include = "filters", from = "src" },
  { include = "app", from = "src" }
]
```

This makes your packages and scripts importable and runnable via:

```bash
poetry run main
poetry run tests
```

---

Let this guide serve as a starter reference. You can now build on this with advanced topics like mocking, integration testing, and plugin usage.


---

## ✅ Mocking with pytest and unittest.mock

You can mock dependencies in your tests using the built-in `unittest.mock` or the `pytest-mock` plugin.

### Using `unittest.mock.patch`:

```python
from unittest.mock import patch

@patch("scrapper.parser.urlopen")
def test_get_page_soup(mock_urlopen):
    mock_urlopen.return_value.read.return_value = b"<html><body><p>Hello</p></body></html>"
    soup = get_page_soup("http://example.com")
    assert soup.p.text == "Hello"
```

### Using the `mocker` fixture from `pytest-mock`:

```python
def test_with_mocker(mocker):
    mock_urlopen = mocker.patch("scrapper.parser.urlopen")
    mock_urlopen.return_value.read.return_value = b"<html><body><p>Hello</p></body></html>"
    soup = get_page_soup("http://example.com")
    assert soup.p.text == "Hello"
```

Install `pytest-mock` via:

```bash
poetry add --group dev pytest-mock
```

---

## ✅ Running Pytest in Continuous Integration (CI)

You can integrate pytest in CI tools like GitHub Actions, GitLab CI, etc.

### Example: GitHub Actions `.github/workflows/tests.yml`

```yaml
name: Run Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install Poetry
        run: |
          curl -sSL https://install.python-poetry.org | python3 -
          export PATH="$HOME/.local/bin:$PATH"

      - name: Install dependencies
        run: poetry install

      - name: Run tests
        run: poetry run pytest
```

### GitLab CI:

```yaml
stages:
  - test

pytest:
  stage: test
  script:
    - poetry install
    - poetry run pytest
```

---

## ✅ Tips for Scaling Your Tests

- Organize tests by module inside the `tests/` folder.
- Use `conftest.py` to share fixtures across test files.
- Mark slow or integration tests with `@pytest.mark.slow` and filter with `-m`.
- Use coverage:

```bash
poetry add --group dev pytest-cov
poetry run pytest --cov=src
```

---

You're now equipped with a solid starting toolkit for professional testing workflows in Python using `pytest`.
