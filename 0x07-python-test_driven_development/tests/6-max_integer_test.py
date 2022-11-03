#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase for max_integer."""

    def test_int(self):
        """testing regular ints"""
        self.assertEqual(max_integer([0, 1, 2, 3, 4]), 4)

    def test_not_int(self):
        """testing non ints"""
        l = ["a", "b", 9]
        self.assertRaises(TypeError, max_integer, l)

    def test_empty(self):
        """testing None list"""
        self.assertEqual(max_integer(), None)

    def test_none(self):
        """testing non element"""
        l = [1, 2, None]
        self.assertRaises(TypeError, max_integer, l)

    def test_negative(self):
        """testing negative ints"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_float(self):
        """testing floats"""
        self.assertEqual(max_integer([3.3, 1.1, 2.2]), 3.3)
    def test_not_list(self):
        """testing if not list"""
        self.assertRaises(TypeError, max_integer, 7)

    def test_one(self):
        """testing one element list"""
        self.assertEqual(max_integer([98]), 98)
