# https://github.com/gonzalezisabellaa/lab11-IG-CM.git
# Partner 1: Isabella Gonzalez
# Partner 2: Isabella Gonzalez

import unittest
import math
from calculator import *

class TestCalculator(unittest.TestCase):


    def test_mul(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 10), 0)

    def test_div(self):
        self.assertEqual(div(10, 2), 5)
        self.assertAlmostEqual(div(7, 2), 3.5)
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(-1, 10)
        with self.assertRaises(ValueError):
            log(2, -3)
        with self.assertRaises(ValueError):
            log(1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)

    def test_square_root(self):
        self.assertEqual(square_root(25), 5)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            square_root(-9)


    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-2, 5), 3)
        self.assertEqual(add(0, 0), 0)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)
        self.assertEqual(sub(5, 10), -5)
        self.assertEqual(sub(-3, -2), -1)

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_log(self):
        self.assertAlmostEqual(log(2, 8), 3.0)
        self.assertAlmostEqual(log(10, 100), 2.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(-2, 8)
        with self.assertRaises(ValueError):
            log(2, -8)
        with self.assertRaises(ValueError):
            log(1, 10)
        with self.assertRaises(ValueError):
            log(10, 0)

if __name__ == "__main__":
    unittest.main()
