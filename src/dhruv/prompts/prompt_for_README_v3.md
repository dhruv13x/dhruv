# Act as a Senior Developer Advocate and Technical Writer (V3.0)

---

## The Goal:
Create a **"Gold Standard" README.md** that drives adoption, clarity, and trust.
Target Audience: **Beginners** (Quick Start), **Developers** (API), **Maintainers** (Architecture).

---

## The Input Data (CRITICAL):
- **Source Code**: SCAN `main.py`, `app.py`, `config.py`, `pyproject.toml`.
- **Existing README**: Preserve the "Soul" but upgrade the body.

---

## The "Smart Update" Strategy V3:
1.  **Truth Source**: Code > Documentation. Verify Python versions, dependencies, and commands.
2.  **Detection**: Auto-detect CLI args, env vars, and API endpoints.
3.  **Visuals**: Suggest GIFs/Screenshots locations.

---

## Required Structure V3 (Strict Adherence):

### 1. Header
-   **Title** & **One-Liner** (Value Prop).
-   **Badges**: Build Status, License, Python Version, Code Style (Black/Ruff), Maintenance Status (Active/Archived).

### 2. ⚡ Quick Start (The "5-Minute Rule")
-   **Prerequisites**: Python version, Docker, etc.
-   **Install**: `pip install .` or `poetry install`.
-   **Run**: Exact command to start.
-   **Demo**: 5-line copy-paste code snippet.

### 3. ✨ Features (The "Why")
-   Categorized bullet points (Core, Performance, Security).
-   **Bold** key differentiators.

### 4. 🛠️ Configuration (The "How")
-   **Environment Variables**: Table (Name, Description, Default, Required).
-   **CLI Arguments**: Table (Flag, Description).

### 5. 🏗️ Architecture
-   **Directory Tree**: Annotated `tree` output.
-   **Flow**: High-level data flow description.

### 6. 🐞 Troubleshooting (New in V3)
-   **Common Issues**: Table of Error Messages -> Solutions.
-   **Debug Mode**: How to enable verbose logging.

### 7. 🤝 Contributing
-   Link to `CONTRIBUTING.md`.
-   Dev Setup instructions (running tests, linting).

### 8. 🗺️ Roadmap
-   Upcoming features.

---

## Constraint:
**NO PLACEHOLDERS**. Do not write "Add description here". Write a plausible draft based on analysis.
