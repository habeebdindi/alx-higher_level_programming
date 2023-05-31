#!/usr/bin/python3
""" This module contains one class

"""


class Square:
    """ Defines a square

    """
    def __init__(self, size=0, position=(0, 0)):
        """ Instantiates with instance attributes.

        Args:
            size (:obj:`int`, optional): Size of the square.
            position (:obj:`tuple` of :obj: `int`, optional):Tuple of 2 +ve int

        Attributes:
            __size (int): Size of the square.
            __position (tuple): Coordinates of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        try:
            if not isinstance(position, tuple) or len(position) != 2:
                raise TypeError
            if not isinstance(position[0], int):
                raise TypeError
            if not isinstance(position[1], int):
                raise TypeError
            if position[0] < 0 or position[1] < 0:
                raise TypeError
        except TypeError:
            print("position must be a tuple of 2 positive integers")

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ Getter method

        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter method
        Args:
            value (:obj:`tuple` of :obj:`int`, optional): Value(position) of
            the square coordinate.

        Attributes:
            __position (tuple): Value(position) of the square.

        """
        try:
            if not isinstance(value, tuple) or len(value) != 2:
                raise TypeError
            if not isinstance(value[0], int):
                raise TypeError
            if not isinstance(value[1], int):
                raise TypeError
            if value[0] < 0 or value[1] < 0:
                raise TypeError
        except TypeError:
            print("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """ Prints in stdout the square with the character '#'.
            Prints the position with empty space character ' '.

        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for i2 in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for x2 in range(self.__size):
                print("#", end="")
            print("")
