#!/usr/bin/python3
"""
7-base_geometry : 1 class

"""


class BaseGeometry:
    """ Exception handling methods """

    def area(self):
        """ Error message """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Error handling for non int attributes """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise TypeError("{} must be an integer".format(name))
