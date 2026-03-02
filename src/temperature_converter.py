"""
temperature_converter.py
Converts temperatures between Celsius, Fahrenheit, and Kelvin.
Modified from Github_Labs/Lab1 (calculator.py).
"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit. Formula: (C × 9/5) + 32"""
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number.")
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius. Formula: (F - 32) × 5/9"""
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number.")
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius: float) -> float:
    """Convert Celsius to Kelvin. Formula: C + 273.15"""
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number.")
    return celsius + 273.15


def kelvin_to_celsius(kelvin: float) -> float:
    """Convert Kelvin to Celsius. Formula: K - 273.15"""
    if not isinstance(kelvin, (int, float)):
        raise ValueError("Input must be a number.")
    if kelvin < 0:
        raise ValueError("Kelvin cannot be negative.")
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """Convert Fahrenheit to Kelvin (via Celsius)."""
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number.")
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """Convert Kelvin to Fahrenheit (via Celsius)."""
    if not isinstance(kelvin, (int, float)):
        raise ValueError("Input must be a number.")
    if kelvin < 0:
        raise ValueError("Kelvin cannot be negative.")
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))


def is_valid_kelvin(kelvin: float) -> bool:
    """Check if a Kelvin value is physically valid (>= 0)."""
    return isinstance(kelvin, (int, float)) and kelvin >= 0


def get_all_conversions(celsius: float) -> dict:
    """
    Given a Celsius value, return all equivalent temperatures.
    Returns a dictionary with Fahrenheit and Kelvin values.
    """
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number.")
    return {
        "celsius": celsius,
        "fahrenheit": round(celsius_to_fahrenheit(celsius), 4),
        "kelvin": round(celsius_to_kelvin(celsius), 4)
    }