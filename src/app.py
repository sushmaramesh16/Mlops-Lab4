"""
app.py
Demonstrates all temperature converter functions with example outputs,
and validates all CSV test cases automatically.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from temperature_converter import (
    celsius_to_fahrenheit, fahrenheit_to_celsius,
    celsius_to_kelvin, kelvin_to_celsius,
    fahrenheit_to_kelvin, kelvin_to_fahrenheit,
    is_valid_kelvin, get_all_conversions
)
from data_processor import validate_test_cases


def main():
    print("=" * 60)
    print("       TEMPERATURE CONVERTER — DEMO")
    print("=" * 60)

    print("\n📌 Basic Conversions:")
    print(f"  0°C  → Fahrenheit : {celsius_to_fahrenheit(0)}°F")
    print(f"  100°C → Fahrenheit : {celsius_to_fahrenheit(100)}°F")
    print(f"  32°F  → Celsius    : {fahrenheit_to_celsius(32)}°C")
    print(f"  0°C  → Kelvin     : {celsius_to_kelvin(0)}K")
    print(f"  373.15K → Celsius : {kelvin_to_celsius(373.15)}°C")
    print(f"  32°F  → Kelvin    : {fahrenheit_to_kelvin(32)}K")
    print(f"  373.15K → Fahrenheit: {kelvin_to_fahrenheit(373.15)}°F")

    print("\n📌 Extra Functions:")
    print(f"  is_valid_kelvin(300)  : {is_valid_kelvin(300)}")
    print(f"  is_valid_kelvin(-10)  : {is_valid_kelvin(-10)}")
    print(f"  get_all_conversions(100): {get_all_conversions(100)}")

    print("\n📌 CSV Test Case Validation:")
    csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'test_cases.csv')
    validate_test_cases(csv_path)


if __name__ == "__main__":
    main()