# 🌡️ Temperature Converter — MLOps GitHub Actions Lab

**Course:** MLOps (IE-7374) — Northeastern University  
**Modified from:** [raminmohammadi/MLOps Github_Labs/Lab1](https://github.com/raminmohammadi/MLOps/tree/main/Labs/Github_Labs/Lab1)  
**Author:** Sushma Ramesh

---

## Overview

This lab is a modified version of MLOps GitHub Actions Lab 1. The original lab focused on a basic **calculator module** with 4 arithmetic functions. This version replaces it with a **Temperature Converter** module that converts temperatures between Celsius, Fahrenheit, and Kelvin.

This lab focuses on 5 modules:
1. Creating a virtual environment
2. Creating a GitHub repository and folder structure
3. Creating Python source files
4. Creating test files using Pytest and Unittest
5. Implementing GitHub Actions for CI/CD automation

---

## Step 1: Creating a Virtual Environment

In software development, it's crucial to manage project dependencies and isolate your project's environment from the global Python environment.

To create a virtual environment, follow these steps:

1. Open a Terminal in the directory where you want to create your project.
2. Create a virtual environment:
```bash
    python3 -m venv venv
```
3. Activate the virtual environment:
```bash
    source venv/bin/activate        # Mac/Linux
    venv\Scripts\activate           # Windows
```

After activation, you will see `(venv)` in your terminal, indicating you are working within the virtual environment.

---

## Step 2: Creating a GitHub Repository and Folder Structure

### Creating a GitHub Repository
- Go to GitHub and click **"New repository"**
- Name your repository and set it to **Public**
- Do **not** initialize with a README (we create our own)
- Click **"Create repository"**

### Cloning the Repository
```bash
git clone https://github.com/sushmaramesh16/Mlops-Lab4.git
cd Mlops-Lab4
```

### Folder Structure
```
Mlops-Lab4/
├── src/
│   ├── temperature_converter.py   # Core conversion + utility functions
│   ├── data_processor.py          # Reads & validates CSV test cases
│   └── app.py                     # Demo app — runs all functions + CSV validation
├── test/
│   ├── __init__.py
│   ├── test_pytest.py             # Pytest suite — 15 tests incl. parametrized
│   └── test_unittest.py           # Unittest suite — 10 tests
├── data/
│   ├── __init__.py
│   └── test_cases.csv             # 12 real-world test cases
├── .github/
│   └── workflows/
│       ├── pytest_action.yml      # CI: runs pytest + uploads XML artifact
│       └── unittest_action.yml    # CI: runs unittest on every push
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Step 3: Creating temperature_converter.py in src Folder

Instead of the original `calculator.py`, this lab creates `temperature_converter.py` within the `src` folder. This script contains 8 functions for temperature conversion and validation.

| Function | Description | Formula |
|---|---|---|
| `celsius_to_fahrenheit(c)` | Celsius → Fahrenheit | `(C × 9/5) + 32` |
| `fahrenheit_to_celsius(f)` | Fahrenheit → Celsius | `(F - 32) × 5/9` |
| `celsius_to_kelvin(c)` | Celsius → Kelvin | `C + 273.15` |
| `kelvin_to_celsius(k)` | Kelvin → Celsius | `K - 273.15` |
| `fahrenheit_to_kelvin(f)` | Fahrenheit → Kelvin | via Celsius |
| `kelvin_to_fahrenheit(k)` | Kelvin → Fahrenheit | via Celsius |
| `is_valid_kelvin(k)` | Checks if Kelvin ≥ 0 | Physical validity check |
| `get_all_conversions(c)` | Celsius → F + K dict | All conversions at once |

All functions include **input validation** — a `ValueError` is raised for non-numeric inputs. `kelvin_to_celsius` and `kelvin_to_fahrenheit` also raise `ValueError` for negative Kelvin values (physically impossible).

---

## Step 4: Creating Tests using Pytest and Unittest

Unit testing ensures that individual components of your code work as expected, helping you catch and fix bugs early in the development process.

### Using Pytest

Install pytest if not already installed:
```bash
pip install pytest
```

Run pytest tests:
```bash
pytest test/test_pytest.py -v
```

**Pytest Test Suite (`test/test_pytest.py`):**
- 6 standard test functions covering all 6 conversion functions
- 1 parametrized test using `@pytest.mark.parametrize` with 5 input/output pairs
- Error handling tests — verifies `ValueError` for invalid inputs and negative Kelvin
- **Total: 15 test cases**

### Using Unittest

Run unittest tests:
```bash
python -m unittest test.test_unittest -v
```

**Unittest Test Suite (`test/test_unittest.py`):**
- 10 test methods inside `TestTemperatureConverter(unittest.TestCase)`
- Uses `assertEqual`, `assertAlmostEqual`, `assertTrue`, `assertFalse`, `assertRaises`
- Includes real-world test: body temperature 37°C = 98.6°F = 310.15K
- **Total: 10 test cases**

---

## Step 5: Implementing GitHub Actions

GitHub Actions is a powerful CI/CD platform that automates workflows directly within your GitHub repository. Two workflows are configured under `.github/workflows/` and trigger automatically on every push or pull request to `main`.

### `pytest_action.yml` — Testing with Pytest
- Sets up Python 3.10 on `ubuntu-latest`
- Installs dependencies from `requirements.txt`
- Runs pytest and generates `pytest-report.xml`
- Uploads the XML report as a downloadable GitHub artifact
- Notifies on success or failure

### `unittest_action.yml` — Python Unittests
- Sets up Python 3.10 on `ubuntu-latest`
- Installs dependencies from `requirements.txt`
- Runs the full unittest suite
- Notifies on success or failure

View live results under the **Actions** tab in this repository.

---

## Enhancements and Additional Features

This lab has been enhanced with the following features beyond the base Lab1:

### Extended Temperature Converter Functions
Added 2 utility functions beyond the 6 core conversions:
- `is_valid_kelvin(k)`: Checks if a Kelvin value is physically valid (≥ 0)
- `get_all_conversions(c)`: Returns a dictionary of all equivalent temperatures for a given Celsius value

All functions include input validation with descriptive `ValueError` messages, making the module production-ready.

### Expanded Test Suite
- Expanded from 4 to **15+ tests** in Pytest and **10 tests** in Unittest
- Added `@pytest.mark.parametrize` for testing multiple input/output pairs efficiently
- Added error handling tests for invalid inputs and negative Kelvin values
- Added real-world test case: human body temperature (37°C = 98.6°F = 310.15K)

### Data Processing Capabilities
- Created `data/test_cases.csv` with 12 real test cases covering all 6 conversion functions
- Built `src/data_processor.py` to read and validate operations from the CSV file
- Outputs a formatted PASS/FAIL table for each test case
- Demonstrates data handling and batch processing capabilities

### Application Integration
- Created `src/app.py` that demonstrates all 8 functions with real example outputs
- Automatically validates all 12 CSV test cases on startup
- Serves as both a demonstration tool and automated validation system

Run the demo app:
```bash
python src/app.py
```

---

## Dependencies
```
pytest==7.4.0
```

Install all dependencies:
```bash
pip install -r requirements.txt
```

---

## References
- [Original Lab1](https://github.com/raminmohammadi/MLOps/tree/main/Labs/Github_Labs/Lab1)
- [Pytest Documentation](https://docs.pytest.org/en/7.4.x/)
- [Unittest Documentation](https://docs.python.org/3/library/unittest.html)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)