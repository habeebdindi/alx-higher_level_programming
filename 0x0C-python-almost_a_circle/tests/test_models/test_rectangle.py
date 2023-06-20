#!/usr/bin/python3
"""Testsuite for models/rectangle.py
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        Base._Base__nb_objects = 0

    def test_constructor_valid_arguments(self):
        """Test that constructor creates a Rectangle instance with valid args"""
        rect = Rectangle(5, 10)
        self.assertIsInstance(rect, Rectangle)
        self.assertIsInstance(rect, Base)

    def test_constructor_invalid_arguments(self):
        """Test that constructor raises approp. exceptions for invalid args"""
        with self.assertRaises(TypeError):
            rect = Rectangle("invalid", 10)

        with self.assertRaises(ValueError):
            rect = Rectangle(5, 0)

        with self.assertRaises(ValueError):
            rect = Rectangle(-5, 10)

        with self.assertRaises(ValueError):
            rect = Rectangle(5, 10, -1, 2)

    def test_width_property(self):
        """ Test the width property"""
        rect = Rectangle(5, 10)
        self.assertEqual(rect.width, 5)
        rect.width = 7
        self.assertEqual(rect.width, 7)

    def test_height_property(self):
        """ Test the height property"""
        rect = Rectangle(5, 10)
        self.assertEqual(rect.height, 10)
        rect.height = 15
        self.assertEqual(rect.height, 15)

    def test_x_property(self):
        """ Test the x property"""
        rect = Rectangle(5, 10, 2)
        self.assertEqual(rect.x, 2)
        rect.x = 4
        self.assertEqual(rect.x, 4)

    def test_y_property(self):
        """Test the y property"""
        rect = Rectangle(5, 10, 2, 3)
        self.assertEqual(rect.y, 3)
        rect.y = 5
        self.assertEqual(rect.y, 5)

    def test_area_method(self):
        """Test the area method"""
        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_update_method(self):
        """ Test the update method"""
        rect = Rectangle(5, 10)
        rect.update(7, 3, 4, 1, 2)
        self.assertEqual(rect.id, 7)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 4)
        self.assertEqual(rect.x, 1)
        self.assertEqual(rect.y, 2)

    def test_to_dictionary_method(self):
        """ Test the to_dictionary method """
        rect = Rectangle(5, 10, 2, 3)
        expected_dict = {'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}
        self.assertDictEqual(rect.to_dictionary(), expected_dict)

    def test_str_representation(self):
        """ Test the __str__ representation """
        rect = Rectangle(5, 10, 2, 3)
        expected_output = "[Rectangle] (1) 2/3 - 5/10"
        self.assertEqual(str(rect), expected_output)

if __name__ == '__main__':
    unittest.main()
