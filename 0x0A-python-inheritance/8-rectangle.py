#!/usr/bin/python3
"""
8-rectangle : 1 class

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class with inherited attributes from BaseGeometry """

    def __init__(self, width, height):
        """ Initializes rectangle object

        Args:
        width (obj : 'int'): width attribute
        height(obj : 'int'): height attribute

        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
