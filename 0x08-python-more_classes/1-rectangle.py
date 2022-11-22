#!/usr/bin/python3
"""
This module contains an empty class that defines an object
"""


class Rectangle:
    """
    Attributes:
        width (int): private instance attribute
        height (int): private instance attribute
    """

    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): width of the rectangle.
            height (int): Height of the rectangle.

        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        int: This defines a rectangle width, it can retrieve its value \
             and set it.
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        int: This defines a rectangle height, it can retrieve its value \
             and set it
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
