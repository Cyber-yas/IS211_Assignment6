# tests.py

import unittest
from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit
from conversions_refactored import convert, ConversionNotPossible

class TestTemperatureConversions(unittest.TestCase):

    def test_convert_celsius_to_kelvin(self):
        self.assertAlmostEqual(convertCelsiusToKelvin(300), 573.15)
        self.assertAlmostEqual(convertCelsiusToKelvin(100.0), 373.15)

    def test_convert_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convertCelsiusToFahrenheit(300), 572.0)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(0.0), 32.0)

class TestRefactoredConversions(unittest.TestCase):
    def test_temperature_conversion(self):
        self.assertAlmostEqual(convert("Celsius", "Kelvin", 300), 573.15)
    

    def test_incompatible_conversion(self):
        with self.assertRaises(ConversionNotPossible):
            convert("Celsius", "Meters", 100)

if __name__ == '__main__':
    unittest.main()
