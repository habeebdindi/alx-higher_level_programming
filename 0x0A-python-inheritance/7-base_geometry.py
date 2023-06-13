#!/usr/bin/python3
"""
Contains class
"""


class BaseGeometry:
    """
    Non empty class
    """
    def area(self):
        """
        raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates a value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
