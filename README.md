<div align="center">
  <img src="https://raw.githubusercontent.com/dhruv13x/dhruv/main/dhruv_logo.png" alt="dhruv logo" width="200"/>
</div>

<div align="center">

<!-- Package Info -->
[![PyPI version](https://img.shields.io/pypi/v/dhruv.svg)](https://pypi.org/project/dhruv/)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
![Wheel](https://img.shields.io/pypi/wheel/dhruv.svg)
[![Release](https://img.shields.io/badge/release-PyPI-blue)](https://pypi.org/project/dhruv/)

<!-- Build & Quality -->
[![Build status](https://github.com/dhruv13x/dhruv/actions/workflows/publish.yml/badge.svg)](https://github.com/dhruv13x/dhruv/actions/workflows/publish.yml)
[![Codecov](https://codecov.io/gh/dhruv13x/dhruv/graph/badge.svg)](https://codecov.io/gh/dhruv13x/dhruv)
[![Test Coverage](https://img.shields.io/badge/coverage-90%25%2B-brightgreen.svg)](https://github.com/dhruv13x/dhruv/actions/workflows/test.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Ruff](https://img.shields.io/badge/linting-ruff-yellow.svg)](https://github.com/astral-sh/ruff)
![Security](https://img.shields.io/badge/security-CodeQL-blue.svg)

<!-- Usage -->
![Downloads](https://img.shields.io/pypi/dm/dhruv.svg)
[![PyPI Downloads](https://img.shields.io/pypi/dm/dhruv.svg)](https://pypistats.org/packages/dhruv)
![OS](https://img.shields.io/badge/os-Linux%20%7C%20macOS%20%7C%20Windows-blue.svg)
[![Python Versions](https://img.shields.io/pypi/pyversions/dhruv.svg)](https://pypi.org/project/dhruv/)

<!-- License -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

<!-- Docs -->
[![Docs](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://your-docs-link)

</div>


# dhruv 🐍

A foundational Python package designed for simplicity and extensibility.

## About
This project serves as a lightweight, "batteries-included" starting point for new Python packages. It demonstrates a clean project structure and basic packaging, making it easy to build upon.

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher

### Installation
For a straightforward installation, run the following command in the root directory:
```bash
pip install .
```
For developers who wish to modify the source code, install it in editable mode:
```bash
pip install -e .
```

### Usage Example
Here's how to use the core function of this package:
```python
from dhruv.main import hello

print(hello())
# Expected Output: "Hello from Dhruv!"
```

Or via the command line:
```bash
dhruv hello
# Expected Output: "Hello from Dhruv!"
```

---

## ✨ Key Features
- **Zero Dependencies**: (Deprecated: Now includes `typer` and `rich` for CLI).
- **Easy to Install**: Get up and running with a single command.
- **Extensible**: A solid foundation for building more complex applications.
- **Command-Line Interface**: Built-in CLI for easy interaction.

---

## ⚙️ Configuration & Advanced Usage
Currently, the package requires no special configuration or environment variables.

---

## 🏗️ Architecture
The project follows a standard `src` layout:
```
.
├── src
│   └── dhruv
│       ├── __init__.py
│       ├── main.py
│       └── cli.py
├── tests
└── pyproject.toml
```
The core logic resides in `src/dhruv/main.py`, which is the primary entry point for the package's functionality. The CLI is handled by `src/dhruv/cli.py`.

---

## 🗺️ Roadmap
- [x] Initial Release
- [x] Add more utility functions
- [x] Implement a command-line interface

---

## 🤝 Contributing & License
Contributions are welcome! Please feel free to submit a pull request.

This project is licensed under the MIT License. See the `pyproject.toml` file for details.
