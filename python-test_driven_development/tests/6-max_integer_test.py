#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max(self):
        #Test maxs when list is all 0
        self.assertAlmostEqual(max_integer([0, 0, 0, 0]), 0)
        self.assertAlmostEqual(max_integer([32, 90, 22, 57]), 90)
        self.assertAlmostEqual(max_integer([-66, -73, -20, -68]), -20)
        self.assertRaises(TypeError, max_integer, [0, 0, 0, "Hola"], "")
        self.assertRaises(TypeError, max_integer, "Hola", "")
        self.assertRaises(TypeError, max_integer, 9, "")
        self.assertAlmostEqual(max_integer([]), None)
        self.assertAlmostEqual(max_integer([1, 1, 1, 1, 1, 1, 1, 1, -4]), 1)
        self.assertAlmostEqual(max_integer([1, -4, -2 , -3]), 1)
        self.assertAlmostEqual(max_integer([1, 2]), 2)
        self.assertAlmostEqual(max_integer([2, 1]), 2)
        self.assertAlmostEqual(max_integer([2]), 2)


if __name__ == "__main__":
    unittest.main()
