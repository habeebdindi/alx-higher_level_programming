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

    def area(self):
        """ Returns current area.

        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """ Getter method

        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method
        Args:
            value (:obj:`int`, optional): Value(size) of the square.

        Attributes:
            __size (int): Value(size) of the square.

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ Prints in stdout the square with the character '#'

        """
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            print("#" * self.__size)
