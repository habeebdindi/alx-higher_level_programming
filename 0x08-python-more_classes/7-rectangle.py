#!/usr/bin/python3
"""
This module contains an empty class that defines an object
"""


class Rectangle:
    """
    Attributes:
        width (int): private instance attribute
        height (int): private instance attribute
        number_of_instances (int): a counter for no. of instances
        print_symbol: used as a symbol for str representation and can \
                      be any type
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Args:
            width (int): width of the rectangle.
            height (int): Height of the rectangle.

        Raises:
            TypeError: if args are not of type int
            ValueError: if args are less than 0

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
        Rectangle.number_of_instances += 1

    def __str__(self):
        sha = []
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                sha.append(str(self.print_symbol))
            sha.append("\n")
        del sha[-1]
        for i2 in sha:
            string += i2
        return string

    def __repr__(self):
        """
        Returns a formal string representation of the current class
        """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.height))

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

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __del__(self):
        """
        Delete an instance of Rectangle
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
