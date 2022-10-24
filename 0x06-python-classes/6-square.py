#!/usr/bin/python3
"""
This module uses OOP and is not import guarded

classes:
    Square
"""


class Square:
    """class defining a square based on its size and coordinates"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialises instance attributes

        Args:
            size (int): 1st parameter which is the value of the size
            position (tuple): 2nd parameter which is the value of its \
            coordinates

        Attributes:
            size (int, optional): private attribute that holds the value of \
            "size".
            position_1: (int, optional): private attribute that holds the \
            value of "position[1]".
            position_2: (int, optional): private attribute that holds the \
            value of "position[2]".

        Raises:
            TypeError: if size is not of type (int) or if position is \
            not a tuple of 2 positive integers.
            ValueError: if size is less than 0
        """
        if not (isinstance(size, int)):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not (isinstance(position, tuple)) \
                or position[1] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position_1, self.__position_2 = position

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
        These are public instance getter and setter methods used to retrieve \
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

    def my_print(self):
        """
        This is a public instance used to print a square using "#" based on \
        its "size".

        check (int): variable checks for completion of inner loop
        """
        check = 0
        if self.__size == 0:
            print("")
        if self.__position_2 > 0:
            print('\n' * self.__position_2, end="")
        for i in range(self.__size):
            check = 0
            for i2 in range(self.__size):
                if check == 0:
                    for i3 in range(self.__position_1):
                        print(" ", end="")
                    check += 1
                print("#", end="")
            print("")

    @property
    def position(self):
        """
        These are public instance getter and setter methods used to retrieve \
        the "position" and assign a value pair to it respectively.

        Raises:
            TypeError: in setter method, if "value" is not a tuple of 2 \
            positive integers.

        Returns:
            tuple: the getter method returns an integer which is the position
        """

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple)) or value[1] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position_1, self.__position_2 = value
