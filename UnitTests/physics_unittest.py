import unittest
from physics import Velocity
from geometry import Time, Length

class TestVelocity(unittest.TestCase):
    velocity1 = Velocity(fps=30)
    velocity2 = Velocity(mps=10 / 3.281)


    def test_convert(self):
        self.assertEqual(30 / 3.281, self.velocity1.mps)
        self.assertEqual(10, self.velocity2.fps)

    def test_add(self):
        expected = 40
        actual = self.velocity1 + self.velocity2
        self.assertEqual(expected, actual.fps)

    def test_sub(self):
        expected = 20
        actual = self.velocity1 - self.velocity2
        self.assertEqual(expected, actual.fps)

    def test_mul_time(self):
        expected = 300
        actual = self.velocity1 * Time(seconds=10)
        self.assertEqual(expected, actual.ft)

    def test_div_velocity(self):
        expected = 3
        actual = self.velocity1 / self.velocity2
        self.assertEqual(expected, actual)

    def test_rdiv_length(self):
        expected = 10
        actual = Length(ft=300) / self.velocity1
        self.assertEqual(expected, actual.seconds)

