import unittest
from geometry import Length, Area, Volume, Time


class TestLength(unittest.TestCase):
    length1 = Length(inch=20)
    length2 = Length(ft=3)
    length3 = Length(ft=5.5)


    def test_convert_to_ft(self):
        expected = 20/12
        actual = self.length1.ft
        self.assertAlmostEqual(expected, actual)

    def test_convert_to_m(self):
        expected = 20/12/3.281
        actual = self.length1.m
        self.assertAlmostEqual(expected, actual)

    def test_convert_to_mile(self):
        expected = 20/12/5280
        actual = self.length1.mile
        self.assertAlmostEqual(expected, actual)

    def test_convert_to_inch(self):
        expected = 20
        actual = self.length1.inch
        self.assertAlmostEqual(expected, actual)

    def test_zero(self):
        expected = 0
        actual = Length(ft=0).ft
        self.assertEqual(expected, actual)

    def test_add(self):
        expected = 20 / 12 + 3
        actual = self.length1 + self.length2
        self.assertAlmostEqual(expected, actual.ft)

    def test_sub(self):
        expected = 3 - 20 / 12
        actual = self.length2 - self.length1
        self.assertAlmostEqual(expected, actual.ft)

    def test_mul_length(self):
        expected = 20 / 12 * 3
        actual = self.length1 * self.length2
        self.assertAlmostEqual(expected, actual.sf)
        self.assertIsInstance(actual, Area)

    def test_mul_area(self):
        expected = 20 / 12 * 3 * 5.5
        actual = self.length1 * self.length2 * self.length3
        self.assertAlmostEqual(expected, actual.cf)
        self.assertIsInstance(actual, Volume)

    def test_mul_scalar(self):
        expected = 20 / 12 * 7
        actual = self.length1 * 7
        self.assertAlmostEqual(expected, actual.ft)
        self.assertIsInstance(actual, Length)

    def test_div_length(self):
        expected = 20 / 12 / 3
        actual = self.length1 / self.length2
        self.assertAlmostEqual(expected, actual)
        self.assertIsInstance(actual, float)

    def test_div_scalar(self):
        expected = 20 / 12 / 5
        actual = self.length1 / 5
        self.assertAlmostEqual(expected, actual.ft)

    def test_pow_2(self):
        expected = (20 / 12) ** 2
        actual = self.length1 ** 2
        self.assertAlmostEqual(expected, actual.sf)

    def test_pow_3(self):
        expected = (20 / 12) ** 3
        actual = self.length1 ** 3
        self.assertAlmostEqual(expected, actual.cf)

    def test_eq(self):
        self.assertTrue(self.length1 == self.length1)
        self.assertFalse(self.length1 == Area(sf=1))
        self.assertTrue(self.length1 == Length(inch=20))

class TestArea(unittest.TestCase):
    area1 = Area(sf=15)
    area2 = Area(inch2=1440)

    def test_convert_units(self):
        expected = 10
        actual = self.area2.sf
        self.assertAlmostEqual(expected, actual)
        self.assertAlmostEqual(2160, self.area1.inch2)
        self.assertAlmostEqual(15 / 5280 / 5280, self.area1.mile2)
        self.assertAlmostEqual(15 / 3.281 / 3.281, self.area1.m2)

    def test_add(self):
        expected = 25
        actual = self.area1 + self.area2
        self.assertAlmostEqual(expected, actual.sf)

    def test_sub(self):
        expected = 5
        actual = self.area1 - self.area2
        self.assertAlmostEqual(expected, actual.sf)

    def test_mul_length(self):
        expected = 30
        actual = self.area1 * Length(ft=2)
        self.assertAlmostEqual(expected, actual.cf)

    def test_mul_scalar(self):
        expected = 45
        actual = self.area1 * 3
        self.assertAlmostEqual(expected, actual.sf)

    def test_div_length(self):
        expected = 5
        actual = self.area1 / Length(ft=3)
        self.assertAlmostEqual(expected, actual.ft)

    def test_div_area(self):
        expected = 1.5
        actual = self.area1 / self.area2
        self.assertAlmostEqual(expected, actual)

    def test_div_scalar(self):
        expected = 3
        actual = self.area1 / 5
        self.assertAlmostEqual(expected, actual.sf)

    def test_eq(self):
        self.assertTrue(self.area1 == self.area1)
        self.assertFalse(self.area1 == Length(ft=15))
        self.assertTrue(self.area1 == Area(sf=15))

class TestVolume(unittest.TestCase):
    vol1 = Volume(cf=100)
    vol2 = Volume(gal=374.026)
    area = Area(sf=10)
    length = Length(ft=20)

    def test_convert_units(self):
        self.assertAlmostEqual(50, self.vol2.cf)
        self.assertAlmostEqual(748.052, self.vol1.gal)
        self.assertAlmostEqual(100 / 3.281 / 3.281 / 3.281, self.vol1.m3)

    def test_add(self):
        expected = 150
        actual = self.vol1 + self.vol2
        self.assertAlmostEqual(expected, actual.cf)

    def test_sub(self):
        expected = 50
        actual = self.vol1 - self.vol2
        self.assertAlmostEqual(expected, actual.cf)

    def test_mul_scalar(self):
        expected = 200
        actual = self.vol1 * 2
        self.assertAlmostEqual(expected, actual.cf)

    def test_div_volume(self):
        expected = 2
        actual = self.vol1 / self.vol2
        self.assertAlmostEqual(expected, actual)

    def test_div_area(self):
        expected = Length(ft=10)
        actual = self.vol1 / self.area
        self.assertAlmostEqual(expected, actual)

    def test_div_length(self):
        expected = Area(sf=5)
        actual = self.vol1 / self.length
        self.assertAlmostEqual(expected, actual)

    def test_div_scalar(self):
        expected = Volume(cf=25)
        actual = self.vol1 / 4
        self.assertAlmostEqual(expected, actual)

    def test_eq(self):
        self.assertTrue(self.vol1 == self.vol1)
        self.assertFalse(self.vol1 == Length(ft=20))
        self.assertTrue(self.vol1 == Volume(cf=100))

class TestTime(unittest.TestCase):
    time1 = Time(seconds=300)
    time2 = Time(minutes=3)

    def test_convert_units(self):
        self.assertAlmostEqual(180, self.time2.seconds)
        self.assertAlmostEqual(5, self.time1.minutes)
        self.assertAlmostEqual(300 / 60 / 60, self.time1.hours)
        self.assertAlmostEqual(300 / 60 / 60 / 24, self.time1.days)

    def test_add(self):
        expected = 480
        actual = self.time1 + self.time2
        self.assertEqual(expected, actual.seconds)

    def test_sub(self):
        expected = 120
        actual = self.time1 - self.time2
        self.assertEqual(expected, actual.seconds)

    def test_div_time(self):
        expected = 300/180
        actual = self.time1 / self.time2
        self.assertEqual(expected, actual)

    def test_div_scalar(self):
        expected = 100
        actual = self.time1 / 3
        self.assertAlmostEqual(expected, actual.seconds)

    def test_eq(self):
        self.assertTrue(self.time1 == self.time1)
        self.assertFalse(self.time1 == Length(ft=20))
        self.assertTrue(self.time1 == Time(minutes=5))
