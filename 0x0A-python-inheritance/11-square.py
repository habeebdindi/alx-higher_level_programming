#!/usr/bin/python3
"""
10-square : 1 class

"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square with inherited attributes from rectangle"""

    def __init__(self, size):
        """ Initialization

        Args:
            size (obj:'int'): size of the square

        """
        super(). __init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """ Print dimensions on square call """

        return str("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """ Returns area of the square """

        return self.__size ** 2
