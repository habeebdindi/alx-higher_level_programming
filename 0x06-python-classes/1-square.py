#!/usr/bin/python3
"""
This module uses OOP and is not import guarded

classes:
    Square
"""


class Square:
    """class defining a square based on its size"""
    def __init__(self, size):
        """Initialises instance attributes

        Args:
            size (int): single parameter which is the value of the \
            size

        Attributes:
            size (int): private attribute that holds the value of \
                        the size
        """
        self.__size = size
