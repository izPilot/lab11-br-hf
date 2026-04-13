# https://github.com/izPilot/lab11-br-hf
# Partner 1: Braden Rennolds
# Partner 2: Hunter Fairbanks

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5, 7), 12)
        self.assertEqual(add(-3, 8), 5)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(4, 10), -6)
        self.assertEqual(subtract(-5, -5), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(10, 5), 50)
        self.assertEqual(mul(-2, 4), -8)
        self.assertEqual(mul(0, 100), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(4, 20), 5.0)
        self.assertEqual(div(2, -10), -5.0)
        self.assertAlmostEqual(div(2, 5), 2.5)

    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(5, 125), 3.0)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(1.5, 2.0), 2.5)
        self.assertAlmostEqual(hypotenuse(-5, 12), 13.0)

    def test_sqrt(self):  # 3 assertions
        self.assertIsNone(square_root(-1))
        self.assertEqual(square_root(25), 5.0)
        self.assertAlmostEqual(square_root(2.25), 1.5)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()
