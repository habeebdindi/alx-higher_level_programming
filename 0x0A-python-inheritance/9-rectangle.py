#!/usr/bin/python3
"""
9-rectangle : 2 classes

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

        def area(self):
            """ Area of object """
            return self.__width * self.__height

        def __str__(self):
            """ Print attributes """
            return "[Rectangle] {}/{}".format(self.__width, self.__height)
