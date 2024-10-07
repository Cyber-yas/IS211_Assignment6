# conversions.py

def convertCelsiusToKelvin(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Kelvins"""
    return celsius + 273.15

def convertCelsiusToFahrenheit(celsius):
    """Takes in a float representing a Celsius measurement, and returns that temperature converted into Fahrenheit"""
    return (celsius * 9/5) + 32

def convertFahrenheitToCelsius(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Celsius"""
    return (fahrenheit - 32) * 5/9


def convertFahrenheitToKelvin(fahrenheit):
    """Takes in a float representing a Fahrenheit measurement, and returns that temperature converted into Kelvins"""
    return (fahrenheit - 32) * 5/9 + 273.15

def convertKelvinToCelsius(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Celsius"""
    return kelvin - 273.15

def convertKelvinToFahrenheit(kelvin):
    """Takes in a float representing a Kelvin measurement, and returns that temperature converted into Fahrenheit"""
    return (kelvin - 273.15) * 9/5 + 32

