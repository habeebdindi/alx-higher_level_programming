#!/usr/bin/python3
"""Magic class given by ByteCode"""
import math


class MagicClass:
    """Initialization of class"""
    def __init__(self, radius=0):
        """Initialization"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius is not float):
            raise TypeError("radius must be a number")
        """Only ints and floats allowed"""
        self._MagicClass__radius = radius

    def area(self):
        return self._MagicClass__radius ** 2 * math.pi
        """Load pi to find area of circle"""

    def circumference(self):
        return 2 * math.pi * self._MagicClass__radius
        """Load pi to find circumference of circle"""
