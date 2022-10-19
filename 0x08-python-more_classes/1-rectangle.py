#!/usr/bin/python3
class Rectangle:
    """This class defines a Rectangle by its width and height"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    @property
    def width(self):
        """This method is used to retrieve the width"""
        return self.width
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
        return self.height
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
