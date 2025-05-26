# ✅ Checklist: Starting a Python Project in VS Code

Use this checklist to track your progress while setting up your Python project in VS Code.

## 🧾 To-Do List

- [ ] 1. Project Structure
- [x] 2. Virtual Environment
- [x] 3. Dependency Management
- [x] 4. Python Version
- [x] 5. Version Control
- [x] 6. .gitignore
- [ ] 7. Testing Framework
- [ ] 8. Code Formatter
- [ ] 9. Import Sorter
- [ ] 10. Static Analysis
- [ ] 11. Security Checks
- [ ] 12. Documentation
- [ ] 13. Pre-commit Hooks
- [ ] 14. CI/CD Integration

---

# ✅ Checklist: Starting a Python Project in VS Code

This checklist helps you create a well-structured Python project in Visual Studio Code, with best practices for maintainability, testing, formatting, and automation.

---

## 1. 📁 Project Structure

| Decision | Options | Benefits | Drawbacks |
|----------|---------|----------|-----------|
| Directory layout | `src/`, `tests/`, `docs/` | Organized code separation, supports clean packaging and testing | Requires initial setup effort |
| Flat structure | All files in root | Simpler for small scripts | Doesn't scale well, cluttered root |

---

## 2. 🐍 Virtual Environment

| Decision | Options | Benefits | Drawbacks |
|----------|---------|----------|-----------|
| Env manager | `venv` | Native, no extra tools | Lacks dependency grouping |
|              | `poetry` | Modern, manages dependencies and envs | Requires learning new tool |

---

## 3. 📦 Dependency Management

| Decision | Options | Benefits | Drawbacks |
|----------|---------|----------|-----------|
| How to declare deps | `requirements.txt` | Simple, widely supported | Not reproducible, hard to manage |
|                     | `pyproject.toml` (with `poetry`) | Lockfiles, dev/prod separation | Less common in legacy projects |

---

## 4. 🐍 Python Version

| Decision | Options | Benefits | Drawbacks |
|----------|---------|----------|-----------|
| Python version | Latest stable (e.g. 3.12) | Best performance, modern features | May lack support in old libs |

---

## 5. 🔄 Version Control

| Decision | Options | Benefits | Drawbacks |
|----------|---------|----------|-----------|
| Tool | Git + GitHub | Standard, enables CI/CD | Needs git knowledge |

---

## 6. 📂 .gitignore

| Decision | Options | Benefits | Drawbacks |
|----------|---------|----------|-----------|
| How to generate | [gitignore.io](https://gitignore.io) | Automatically updates for Python | Review is still needed |

---

## 7. 🧪 Testing Framework

| Decision | Options | Benefits | Drawbacks |
|----------|---------|----------|-----------|
| Tool | `pytest` | Clean, concise, powerful | Requires installation |
|      | `unittest` | Built-in | Verbose syntax |

---

## 8. 🧼 Code Formatter

| Decision | Options | Benefits | Drawbacks |
|----------|---------|----------|-----------|
| Formatter | `blue` | PEP8-compliant, minimal diffs | Less known |
|           | `black` | Popular, strict consistency | Invasive changes |

---

## 9. 🧩 Import Sorter

| Decision | Options | Benefits | Drawbacks |
|----------|---------|----------|-----------|
| Tool | `isort` | Clean imports, auto-organized | Can override logical import grouping |

---

## 10. 🔎 Static Analysis

| Decision | Options | Benefits | Drawbacks |
|----------|---------|----------|-----------|
| Tool | `prospector` | Aggregates tools like `pylint`, `pep257` | Complex configuration |
|      | `flake8` | Lightweight, simple | Less comprehensive |
|      | `pylint` | Detailed diagnostics | Too verbose for some users |

---

## 11. 🔐 Security Checks

| Decision | Options | Benefits | Drawbacks |
|----------|---------|----------|-----------|
| Tool | `pip-audit` | Highlights vulnerable packages | False positives possible |
|      | `safety` | Broad CVE database | May require subscription for full DB |

---

## 12. 📚 Documentation

| Decision | Options | Benefits | Drawbacks |
|----------|---------|----------|-----------|
| Generator | `MkDocs` | Fast, modern static docs | Basic features |
|           | `Sphinx` | Full-featured, supports docstrings | Steeper learning curve |

---

## 13. 🧩 Pre-commit Hooks

| Decision | Options | Benefits | Drawbacks |
|----------|---------|----------|-----------|
| Tool | `pre-commit` | Auto format, lint before commit | Increases commit time |

---

## 14. 🚀 CI/CD Integration

| Decision | Options | Benefits | Drawbacks |
|----------|---------|----------|-----------|
| Tool | GitHub Actions | Easy automation, community support | Requires initial config |
|      | GitLab CI | Strong integration in GitLab | Slightly more complex config |

---

Feel free to adapt this checklist depending on the complexity and goals of your project!
