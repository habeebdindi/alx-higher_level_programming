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
    if a+1 == a:
        raise OverflowError("a too large")
    if b+1 == b:
        raise OverflowError("b too large")
    if a is None or type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    result = a+b
    if result == float('inf') or result == -float('inf'):
        return result
    return int(a) + int(b)
