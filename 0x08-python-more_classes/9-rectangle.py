#!/usr/bin/python3
"""
A module containing a rectangle class
"""


class Rectangle:
    """
    ...
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        ...
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        ...
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        ...
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """
        ...
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        ...
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        ...
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        ...
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """
        ...
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        output = ""
        for i in range(self.__height):
            output += str(self.print_symbol) * self.__width + "\n"
        return output[:-1]

    def __repr__(self):
        """
        ...
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        ...
        """
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        ...
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        ...
        """
        return cls(size, size)
