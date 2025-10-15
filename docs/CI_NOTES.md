## 🧭 CI Documentation

### 🎯 Purpose
This document explains the Continuous Integration (CI) workflow for **AI-UHP / NetSentry**.  
It defines what happens on every code push, why each step exists, and how to debug or extend the pipeline.

---

### 🧩 1️⃣ Overview
Our CI pipeline runs automatically on **every push or pull request** to the `main` branch.  
It verifies that the entire project — FastAPI API, CLI, and Docker build — works correctly on a fresh environment before any code is merged or released.

**Key objectives**
- Ensure every commit builds and tests successfully.
- Detect broken imports, dependency issues, or syntax errors early.
- Maintain reproducible environments through Docker and virtual envs.
- Provide visible status via the README badge.

---

### 🧱 2️⃣ Workflow File
Location: `.github/workflows/ci.yml`

**Main jobs**

| Step | Description | Notes |
|------|--------------|-------|
| **Checkout code** | Pulls the repo into the runner | Standard GitHub Action |
| **List repository files** | Prints directory tree for diagnostics | Helps verify missing files |
| **Set up Python** | Installs requested Python version(s) | Controlled via `matrix.python-version` |
| **Cache pip dependencies** | Reuses previous `pip` installs | Cuts build time by 50–60 % |
| **Install dependencies** | Installs from `requirements.txt` | Creates and activates `.venv` |
| **Run FastAPI sanity test** | Imports `app.main` and checks `/` route | Verifies API startup |
| **Run CLI sanity test** | Executes `python src/netsentry/cli.py check --url https://example.com` | Verifies CLI entry point |
| **Run pytest** | Executes all tests under `tests/` | Unit / integration coverage |
| **Build Docker image** | Confirms Dockerfile builds cleanly | Ensures deployability |
| **Upload artifacts** | Saves `requirements.txt`, Dockerfile, ci.yml | Reference snapshot for each run |

---

### 🧠 3️⃣ Execution Flow
1. GitHub spins up a fresh Ubuntu runner.  
2. Code is checked out.  
3. The selected Python version(s) are installed (matrix testing).  
4. Dependencies are installed → tests run → Docker image builds.  
5. If any step fails, the job stops and the badge turns red.  
6. On success, the badge remains green ✅ and artifacts are stored for 90 days.

---

### 🧰 4️⃣ Key Files in Repo
| File | Purpose |
|------|----------|
| `.github/workflows/ci.yml` | CI pipeline definition |
| `requirements.txt` | Dependency list |
| `pytest.ini` | Adds project root to `PYTHONPATH` for imports |
| `app/__init__.py` | Marks API folder as package for imports |
| `tests/test_basic.py` | Example pytest to validate API health |
| `.gitignore` | Excludes cache/venv files from commits |

---

### 🧩 5️⃣ Caching Logic
Caching uses `actions/cache@v4` with key  
`${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}`.  
- If `requirements.txt` hasn’t changed → **Cache hit** ✅ → installs reused.  
- If dependencies changed → **Cache miss** 🟡 → rebuilds and saves new cache.  

---

### 🧩 6️⃣ Matrix Testing
The pipeline can run across multiple Python versions:
```yaml
matrix:
  python-version: ["3.10", "3.11", "3.12"]
