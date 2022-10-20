#!/usr/bin/python3
class Rectangle:
    """This class defines a Rectangle by its width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def __str__(self):
        sha = ""
        for i in range(self.__width):
            sha += "#"
        for i2 in range(self.__height):
            print(sha)
    @property
    def width(self):
        """This method is used to retrieve the width"""
        return self.__width
    @width.setter
    def width(self, value):
        """This method is used to set the width"""
        try:
            if value >= 0:
                self.__width = value
            elif not type(value) is int:
                raise TypeError
            else:
                raise ValueError
        except TypeError:
            print("width must be an integer")
        except ValueError:
            print("width must be >= 0")
    @property
    def height(self):
        """This method is used to retrieve the height"""
        return self.__height
    @height.setter
    def height(self, value):
        """This method is used to set the height"""
        try:
            if value >= 0:
                self.__height = value
            elif not type(value) is int:
                raise TypeError
            else:
                raise ValueError
        except TypeError:
            print("width must be an integer")
        except ValueError:
            print("width must be >= 0")
    def area(self):
        """calculating the area and returning it"""
        return (self.__width * self.__height)
    def perimeter(self):
        """calculating the perimeter and returning it"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))
