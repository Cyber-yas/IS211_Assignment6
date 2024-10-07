# conversions_refactored.py

class ConversionNotPossible(Exception):
    """Custom exception for incompatible unit conversions."""
    pass

def convert(from_unit, to_unit, value):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit == to_unit:
        return value

    # Temperature conversions
    if from_unit in ["celsius", "fahrenheit", "kelvin"] and to_unit in ["celsius", "fahrenheit", "kelvin"]:
        if from_unit == "celsius":
            if to_unit == "kelvin":
                return value + 273.15
            elif to_unit == "fahrenheit":
                return (value * 9/5) + 32
        elif from_unit == "fahrenheit":
            if to_unit == "celsius":
                return (value - 32) * 5/9
            elif to_unit == "kelvin":
                return (value - 32) * 5/9 + 273.15
        elif from_unit == "kelvin":
            if to_unit == "celsius":
                return value - 273.15
            elif to_unit == "fahrenheit":
                return (value - 273.15) * 9/5 + 32

    # Distance conversions
    distance_conversion_factors = {
        "miles": {"yards": 1760, "meters": 1609.34},
        "yards": {"miles": 1/1760, "meters": 0.9144},
        "meters": {"miles": 1/1609.34, "yards": 1.09361}
    }

    if from_unit in distance_conversion_factors and to_unit in distance_conversion_factors[from_unit]:
        return value * distance_conversion_factors[from_unit][to_unit]

    raise ConversionNotPossible(f"Conversion from {from_unit} to {to_unit} is not possible.")




