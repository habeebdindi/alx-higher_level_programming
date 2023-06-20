#!/usr/bin/python3
"""Test suite for square.py"""
import unittest
from unittest.mock import patch
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_constructor(self):
        """ Test constructor with valid arguments"""
        s = Square(5, 1, 2, 10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)

        """ Test constructor with missing arguments"""
        s2 = Square(3)
        self.assertIsNotNone(s2.id)
        self.assertEqual(s2.size, 3)
        self.assertEqual(s2.x, 0)
        self.assertEqual(s2.y, 0)

    def test_string_representation(self):
        """ Test __str__ method"""
        s = Square(4, 2, 3, 5)
        expected_output = "[Square] (5) 2/3 - 4"
        self.assertEqual(str(s), expected_output)

    def test_area(self):
        """ Test area method"""
        s = Square(5)
        self.assertEqual(s.area(), 25)

    def test_update(self):
        """ Test update method with positional arguments"""
        s = Square(2)
        s.update(10, 5, 3, 4)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

        """ Test update method with keyword arguments"""
        s.update(y=7, x=2, id=15, size=6)
        self.assertEqual(s.id, 15)
        self.assertEqual(s.size, 6)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 7)

    def test_to_dictionary(self):
        """ Test to_dictionary method"""
        s = Square(3, 2, 1, 5)
        expected_dict = {'id': 5, 'size': 3, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_load_from_file(self):
        """ Test load_from_file class method"""
        Square.save_to_file([Square(2), Square(4)])
        instances = Square.load_from_file()
        self.assertEqual(len(instances), 2)
        self.assertTrue(isinstance(instances[0], Square))
        self.assertTrue(isinstance(instances[1], Square))

if __name__ == '__main__':
    unittest.main()
