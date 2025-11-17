#https://github.com/gonzalezisabellaa/lab11-IG-CM.git
#Partner 1: Isabella  Gonzalez
#Partner 2: Connor Mertz

import unittest
import math
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 10), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertAlmostEqual(divide(7, 2), 3.5)

        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(-1, 10)

        with self.assertRaises(ValueError):
            logarithm(2, -3)

        with self.assertRaises(ValueError):
            logarithm(1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)

    def test_sqrt(self):
        self.assertEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))

        with self.assertRaises(ValueError):
            square_root(-9)

if __name__ == '__main__':
    unittest.main()
