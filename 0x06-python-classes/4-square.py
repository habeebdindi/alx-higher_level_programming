#!/usr/bin/python3
"""
This module uses OOP and is not import guarded

classes:
    Square
"""


class Square:
    """class defining a square based on its size"""
    def __init__(self, size=0):
        """Initialises instance attributes

        Args:
            size (int): single parameter which is the value of the \
            size

        Attributes:
            size (int, optional): private attribute that holds the value of \
            the size

        Raises:
            TypeError: if size is not of type (int)
            ValueError: if size is less than 0
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        This is a public instance method. It calculates the area of a square

        Returns:
            int: an integer which is the calculated area
        """
        return self.__size ** 2
    @property
    def size(self):
        """
        This is a public instance getter and setter method used to retrieve \
        the "size" and assign value to it respectively

        Returns:
            int: the getter method returns an integer which is the size

        Raises:
            TypeError: if value is not of type (int)
            ValueError: is value is less than 0
        """
        return self.__size
    @size.setter
    def size(self, value):
        if not (isinstance(value, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
