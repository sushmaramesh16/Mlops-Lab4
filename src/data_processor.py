"""
data_processor.py
Reads test cases from data/test_cases.csv and validates them
against the temperature_converter functions.
"""

import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.temperature_converter import (
    celsius_to_fahrenheit, fahrenheit_to_celsius,
    celsius_to_kelvin, kelvin_to_celsius,
    fahrenheit_to_kelvin, kelvin_to_fahrenheit
)

OPERATIONS = {
    "celsius_to_fahrenheit": celsius_to_fahrenheit,
    "fahrenheit_to_celsius": fahrenheit_to_celsius,
    "celsius_to_kelvin": celsius_to_kelvin,
    "kelvin_to_celsius": kelvin_to_celsius,
    "fahrenheit_to_kelvin": fahrenheit_to_kelvin,
    "kelvin_to_fahrenheit": kelvin_to_fahrenheit,
}


def load_test_cases(filepath: str) -> list:
    """Load test cases from a CSV file."""
    test_cases = []
    with open(filepath, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            test_cases.append({
                "operation": row["operation"],
                "input": float(row["input"]),
                "expected": float(row["expected"])
            })
    return test_cases


def validate_test_cases(filepath: str) -> None:
    """Run all test cases from CSV and print pass/fail results."""
    test_cases = load_test_cases(filepath)
    passed = 0
    failed = 0

    print(f"\nRunning {len(test_cases)} test cases from CSV...\n")
    print(f"{'Operation':<30} {'Input':>10} {'Expected':>10} {'Got':>10} {'Status':>8}")
    print("-" * 75)

    for tc in test_cases:
        func = OPERATIONS.get(tc["operation"])
        if func is None:
            print(f"Unknown operation: {tc['operation']}")
            continue

        result = round(func(tc["input"]), 2)
        expected = round(tc["expected"], 2)
        status = "✅ PASS" if result == expected else "❌ FAIL"

        if result == expected:
            passed += 1
        else:
            failed += 1

        print(f"{tc['operation']:<30} {tc['input']:>10} {expected:>10} {result:>10} {status:>8}")

    print("-" * 75)
    print(f"\nResults: {passed} passed, {failed} failed out of {len(test_cases)} total.\n")


if __name__ == "__main__":
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_cases.csv')
    validate_test_cases(csv_path)