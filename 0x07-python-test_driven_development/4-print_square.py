#!usr/bin/python3
"""
Module contains one function
"""


def print_square(size):
    """
    prints a square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    count = 0
    while count < size:
        print("#" * size)
        count += 1
