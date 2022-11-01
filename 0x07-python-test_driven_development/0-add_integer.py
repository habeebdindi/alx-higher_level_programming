#!/usr/bin/python3
"""

    This module contains a function that adds two integers
"""


def add_integer(a, b=98):
    """
    This function adds two integers

    Args:
        a (int) or (float): 1st parameter
        b (int) or (float), optional: 2nd paramter

    Returns:
        int: returns the integer sum of the two parameters
    """
    if a is None or type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
