#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Contains a class that inherits from Rectangle
"""


class Square(Rectangle):
    """
    contains init method only
    """
    def __init__(self, size):
        """
        initialisation
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns Area """
        return self.__size * self.__size

    def __str__(self):
        """ the str() """
        return "[Square] {}/{}".format(self.__size, self.__size)
