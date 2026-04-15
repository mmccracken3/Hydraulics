import unittest
from geometry import Length

class TestLength(unittest.TestCase):
    length = Length(inch=20)


    def test_convert_to_ft(self):
        expected = 20/12
        actual = self.length.ft
        self.assertAlmostEqual(expected, actual)

    def test_convert_to_m(self):
        expected = 20/12/3.281
        actual = self.length.m
        self.assertAlmostEqual(expected, actual)

    def test_convert_to_mile(self):
        expected = 20/12/5280
        actual = self.length.mile
        self.assertAlmostEqual(expected, actual)

    def test_convert_to_inch(self):
        expected = 20
        actual = self.length.inch
        self.assertAlmostEqual(expected, actual)

