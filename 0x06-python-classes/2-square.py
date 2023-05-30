#!/usr/bin/python3
""" This module contains one class

"""


class Square:
    """ Defines a square

    """
    def __init__(self, size=0):
        """ Instantiates with instance attributes.

        Args:
            size (:obj:`int`, optional): Size of the square.

        Attributes:
            __size (int): Size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
