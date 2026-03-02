"""
test_pytest.py — Pytest tests for temperature_converter.py
"""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.temperature_converter import (
    celsius_to_fahrenheit, fahrenheit_to_celsius,
    celsius_to_kelvin, kelvin_to_celsius,
    fahrenheit_to_kelvin, kelvin_to_fahrenheit,
    is_valid_kelvin, get_all_conversions
)


def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(0) == 32.0
    assert celsius_to_fahrenheit(100) == 212.0
    assert celsius_to_fahrenheit(-40) == -40.0


def test_fahrenheit_to_celsius():
    assert fahrenheit_to_celsius(32) == 0.0
    assert fahrenheit_to_celsius(212) == 100.0
    assert fahrenheit_to_celsius(-40) == -40.0


def test_celsius_to_kelvin():
    assert celsius_to_kelvin(0) == 273.15
    assert celsius_to_kelvin(100) == 373.15


def test_kelvin_to_celsius():
    assert kelvin_to_celsius(273.15) == 0.0
    assert kelvin_to_celsius(373.15) == 100.0


def test_fahrenheit_to_kelvin():
    assert round(fahrenheit_to_kelvin(32), 2) == 273.15
    assert round(fahrenheit_to_kelvin(212), 2) == 373.15


def test_kelvin_to_fahrenheit():
    assert round(kelvin_to_fahrenheit(273.15), 2) == 32.0
    assert round(kelvin_to_fahrenheit(373.15), 2) == 212.0


def test_is_valid_kelvin():
    assert is_valid_kelvin(0) == True
    assert is_valid_kelvin(300) == True
    assert is_valid_kelvin(-1) == False


def test_get_all_conversions():
    result = get_all_conversions(0)
    assert result["celsius"] == 0
    assert result["fahrenheit"] == 32.0
    assert result["kelvin"] == 273.15


def test_invalid_input_raises_error():
    with pytest.raises(ValueError):
        celsius_to_fahrenheit("hot")
    with pytest.raises(ValueError):
        kelvin_to_celsius(-5)


# Parametrized test
@pytest.mark.parametrize("celsius, expected", [
    (0, 32.0),
    (100, 212.0),
    (-40, -40.0),
    (37, 98.6),
    (-273.15, -459.67),
])
def test_celsius_to_fahrenheit_parametrized(celsius, expected):
    assert round(celsius_to_fahrenheit(celsius), 2) == round(expected, 2)