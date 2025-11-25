# dhruv 🐍

A foundational Python package designed for simplicity and extensibility.

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/dhruv13x/dhruv)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

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

---

## ✨ Key Features
- **Zero Dependencies**: No external packages required.
- **Easy to Install**: Get up and running with a single command.
- **Extensible**: A solid foundation for building more complex applications.

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
│       └── main.py
├── tests
└── pyproject.toml
```
The core logic resides in `src/dhruv/main.py`, which is the primary entry point for the package's functionality.

---

## 🗺️ Roadmap
- [x] Initial Release
- [ ] Add more utility functions
- [ ] Implement a command-line interface

---

## 🤝 Contributing & License
Contributions are welcome! Please feel free to submit a pull request.

This project is licensed under the MIT License. See the `pyproject.toml` file for details.
