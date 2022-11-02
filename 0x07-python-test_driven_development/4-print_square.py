#!/usr/bin/python3
"""

This module prints a square with "#"
"""


def print_square(size):
    """
    function prints a square with the character #.

    Args:
        size (int): the length of the square
    """
    if not type(size) is int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)
