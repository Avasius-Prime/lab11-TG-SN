# https://github.com/Avasius-Prime/lab11-TG-SN.git
# Partner 1: Timothy Giles (did not participate)
# Partner 2: Selasi Nukunya

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        x = 1
        y = 1
        expected = 2
        result = add(x, y)
        self.assertEqual(result, expected)

    def test_subtract(self): # 3 assertions
        x = 1
        y = 1
        expected = 0
        result = subtract(x, y)
        self.assertEqual(result, expected)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        x = 1
        y = 1
        expected = 1
        result = mul(x, y)
        self.assertEqual(result, expected)

    def test_divide(self): # 3 assertions
        x = 1
        y = 1
        expected = 1
        result = div(x, y)
        self.assertEqual(result, expected)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        x = 10
        y = 100
        expected = 2
        result = logarithm(x, y)
        self.assertEqual(result, expected)

    def test_log_invalid_base(self): # 1 assertion
    # use same technique from test_divide_by_zero
        x = 1
        y = 100
        with self.assertRaises(ValueError):
            logarithm(x, y)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
        x = 0
        y = 5

        with self.assertRaises(ValueError):
            logarithm(x, y)

    def test_hypotenuse(self): # 3 assertions
        x = 3
        y = 4
        expected = 5
        result = hypotenuse(x, y)
        self.assertEqual(result, expected)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
        x = -1

        with self.assertRaises(ValueError):
            square_root(x)

# Do not touch this
if __name__ == "__main__":
    unittest.main()