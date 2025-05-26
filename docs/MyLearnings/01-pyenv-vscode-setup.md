# Pyenv-Win and Visual Studio Code Setup (Windows)

## ✅ Goal

Use `pyenv-win` to manage Python versions and integrate them cleanly with **Visual Studio Code** on Windows.

---

## 🧰 1. Installing `pyenv-win`

### Recommended via Chocolatey:

```powershell
choco install pyenv-win
```

### Or manually:

- Clone the repo to: `%USERPROFILE%\.pyenv\pyenv-win`
- Add to PATH:
  ```
  %USERPROFILE%\.pyenv\pyenv-win\bin
  %USERPROFILE%\.pyenv\pyenv-win\shims
  ```

---

## 🐍 2. Using `pyenv-win`

### Install a Python version:

```powershell
pyenv install 3.12.0
```

### Set it globally or locally:

```powershell
pyenv global 3.12.0
# or
pyenv local 3.12.0  # (per project)
```

### Confirm it's active:

```powershell
pyenv version
python --version
```

---

## 📦 3. Creating a virtual environment

In your project folder:

```powershell
pyenv local 3.12.0
python -m venv .venv
.venv\Scripts\activate
```

---

## 🧠 4. Using `pyenv` in Visual Studio Code

### Select interpreter:

1. Open folder in VS Code (`code .`)
2. Press `Ctrl+Shift+P` → `Python: Select Interpreter`
3. Choose:
   - `C:\Users\<you>\.pyenv\pyenv-win\versions\3.12.0\python.exe`
   - or `.venv\Scripts\python.exe`

---

## 🛠 5. Fix: `pyenv` not recognized in VS Code terminal

### Add to `.vscode/settings.json`:

```json
{
  "terminal.integrated.env.windows": {
    "PYENV": "${env:USERPROFILE}\\.pyenv\\pyenv-win",
    "PYENV_ROOT": "${env:PYENV}",
    "Path": "${env:PYENV}\\bin;${env:PYENV}\\shims;${env:Path}"
  }
}
```

Then **restart VS Code**.

---

## 🔍 6. Checking all installed Pythons

### All pyenv-managed:

```powershell
pyenv versions
```

### System-wide search:

```powershell
where python
```

Or scan manually:

```powershell
Get-ChildItem -Path C:\ -Recurse -Filter python.exe -ErrorAction SilentlyContinue
```

---

## ✅ You’re Now Set To:

- Manage multiple Python versions easily
- Keep clean per-project environments
- Use everything inside VS Code with full terminal support

---

Let me know if you want a PowerShell script to automate this whole setup for future projects.