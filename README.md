# 🌡️ Temperature Converter — MLOps GitHub Actions Lab

**Course:** MLOps (IE-7374) — Northeastern University  
**Modified from:** [raminmohammadi/MLOps Github_Labs/Lab1](https://github.com/raminmohammadi/MLOps/tree/main/Labs/Github_Labs/Lab1)  
**Author:** Sushma Ramesh

---

## Overview

This lab is a modified version of MLOps GitHub Actions Lab 1. The original lab used a basic **calculator module** (add, subtract, multiply). This version replaces it with a **Temperature Converter** that converts between Celsius, Fahrenheit, and Kelvin — with additional features like input validation, CSV-based test cases, a data processor, and a demo app.

The lab covers 5 key MLOps concepts:
1. Setting up a Python virtual environment
2. Creating and structuring a GitHub repository
3. Writing modular, well-documented Python code
4. Writing unit tests using **Pytest** and **Unittest**
5. Automating tests using **GitHub Actions CI/CD**

---

## What's Different from the Base Lab

| Aspect | Base Lab (Lab1) | This Version |
|---|---|---|
| **Module** | `calculator.py` | `temperature_converter.py` |
| **Functions** | 4 basic math functions | 8 conversion + utility functions |
| **Input validation** | None | ValueError raised for invalid inputs |
| **Test count** | 4 tests | 15+ tests including parametrized |
| **Data processing** | None | `data_processor.py` + `test_cases.csv` |
| **Demo app** | None | `app.py` with full demonstration |

---

## Project Structure

```
Mlops-Lab4/
├── src/
│   ├── temperature_converter.py   # Core conversion functions
│   ├── data_processor.py          # Reads & validates CSV test cases
│   └── app.py                     # Demo app showing all functions
├── test/
│   ├── __init__.py
│   ├── test_pytest.py             # Pytest test suite (15 tests)
│   └── test_unittest.py           # Unittest test suite (10 tests)
├── data/
│   ├── __init__.py
│   └── test_cases.csv             # 12 real test cases
├── .github/
│   └── workflows/
│       ├── pytest_action.yml      # Runs pytest on every push
│       └── unittest_action.yml    # Runs unittest on every push
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Functions

| Function | Description |
|---|---|
| `celsius_to_fahrenheit(c)` | Converts Celsius → Fahrenheit |
| `fahrenheit_to_celsius(f)` | Converts Fahrenheit → Celsius |
| `celsius_to_kelvin(c)` | Converts Celsius → Kelvin |
| `kelvin_to_celsius(k)` | Converts Kelvin → Celsius |
| `fahrenheit_to_kelvin(f)` | Converts Fahrenheit → Kelvin |
| `kelvin_to_fahrenheit(k)` | Converts Kelvin → Fahrenheit |
| `is_valid_kelvin(k)` | Checks if Kelvin value is physically valid (≥ 0) |
| `get_all_conversions(c)` | Returns Fahrenheit & Kelvin for a given Celsius value |

---

## How to Run Locally

```bash
# Clone the repo
git clone https://github.com/sushmaramesh16/Mlops-Lab4.git
cd Mlops-Lab4

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the demo app
python src/app.py

# Run Pytest
pytest test/test_pytest.py -v

# Run Unittest
python -m unittest test.test_unittest -v
```

---

## GitHub Actions

Two workflows run automatically on every push to `main`:

- **`pytest_action.yml`** — runs pytest, generates XML report, uploads as artifact
- **`unittest_action.yml`** — runs full unittest suite

View results under the **Actions** tab in this repository.

---

## References
- [Original Lab1](https://github.com/raminmohammadi/MLOps/tree/main/Labs/Github_Labs/Lab1)
- [Pytest Docs](https://docs.pytest.org/en/7.4.x/)
- [Unittest Docs](https://docs.python.org/3/library/unittest.html)
- [GitHub Actions Docs](https://docs.github.com/en/actions)