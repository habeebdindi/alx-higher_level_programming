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

        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """ Checks equality

        """
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """ Checks non-equality

        """
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __lt__(self, other):
        """ Checks less than

        """
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __gt__(self, other):
        """ Checks greater than

        """
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __le__(self, other):
        """ Checks less than or equal to

        """
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def __ge__(self, other):
        """ Checks greater than or equal to

        """
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented
