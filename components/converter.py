from utils.config import UNITS


def convert_temperature(value, from_unit, to_unit):
    """Converts temperature between Celsius, Fahrenheit, and Kelvin."""
    if from_unit == to_unit:
        return value
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9 / 5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5 / 9
        elif to_unit == "kelvin":
            return (value - 32) * 5 / 9 + 273.15
    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9 / 5 + 32
    return None


def unit_converter(value, from_unit, to_unit, category):
    """Converts a unit from one type to another within a given category."""
    if category == "Temperature":
        return convert_temperature(value, from_unit, to_unit)
    return value * UNITS[category][from_unit] / UNITS[category][to_unit]
