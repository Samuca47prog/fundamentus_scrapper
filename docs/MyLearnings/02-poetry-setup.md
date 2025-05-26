# Poetry Project Management Guide

This document provides a full overview of how **Poetry** helps manage your Python projects, dependencies, and environments—focusing on best practices for reproducibility, organization, and development.

---

## ✅ What Poetry Does For You

| Feature                    | Benefit                                                                 |
|---------------------------|-------------------------------------------------------------------------|
| 📦 Dependency Management   | Simplified `add`, `remove`, and version locking                         |
| 🧪 Virtual Environment     | Automatically creates and manages per-project environments              |
| 📁 `pyproject.toml`        | Centralized project configuration and metadata                          |
| 🔐 `poetry.lock`           | Ensures exact versions are reproducible across machines and CI/CD       |
| 🧰 Tooling Integration     | Works well with VS Code, test runners, formatters, and linters          |
| 🧪 Grouped Dependencies     | Clean separation of runtime vs dev/test/docs dependencies               |

---

## ✅ Project Initialization

### Create or use an existing folder

```bash
poetry init
```

This generates a `pyproject.toml` file. It **does not** create the virtual environment yet.

---

## ✅ Setting Python Version

You can set the interpreter used by Poetry (e.g., from pyenv):

```bash
poetry env use C:\Users\you\.pyenv\pyenv-win\versions\3.12.0\python.exe
```

---

## ✅ Creating the Virtual Environment

Poetry creates a virtual environment when you first:

```bash
poetry install
# OR
poetry add <package>
# OR
poetry shell (if plugin installed)
```

---

## ✅ Activating the Environment

### Recommended (Poetry 2.x+):

```bash
poetry env activate
```

Then run the path it gives you (e.g., `activate.ps1`).

### Alternative:

Install the shell plugin:

```bash
poetry self add poetry-plugin-shell
poetry shell
```

---

## ✅ Adding Dependencies

### Runtime dependencies:

```bash
poetry add requests
poetry add selenium
```

### Dev dependencies (used only during development):

```bash
poetry add --group dev pytest
poetry add --group dev black
```

### Custom groups:

```bash
poetry add --group docs mkdocs
poetry add --group lint flake8
```

---

## ✅ Removing Dependencies

```bash
poetry remove requests
```

---

## ✅ Listing Dependencies

```bash
poetry show --tree
```

---

## ✅ Installing the Project in Another Machine

1. Clone the repo
2. Ensure Poetry is installed
3. Install dependencies:

```bash
poetry install
```

This uses the versions from `poetry.lock`.

---

## ✅ Running Code in the Environment

Without activating the shell:

```bash
poetry run python script.py
poetry run pytest
```

---

## ✅ Version Control Notes

Only commit:

- `pyproject.toml`
- `poetry.lock`

Ignore:

```
.venv/
__pycache__/
*.pyc
```

---

Poetry is a full project and dependency manager—greatly simplifying setup, sharing, and maintaining Python projects.