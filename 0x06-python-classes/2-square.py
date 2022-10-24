#!/usr/bin/python3
"""
This module uses OOP and is not import guarded

classes:
    Square
"""


class Square:
    """class defining a square based on its size"""
    def __init__(self, size=0):
        """Initialises instance attributes

        Args:
            size (int): single parameter which is the value of the \
            size

        Attributes:
            size (int, optional): private attribute that holds the value of \
            the size

        Raises:
            TypeError: if size is not of type (int)
            ValueError: if size is less than 0
        """
        try:
            size += 0
            self.__size = size
            if size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
