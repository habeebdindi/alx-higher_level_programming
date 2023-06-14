#!/usr/bin/python3
"""
Contains one function
"""


def pascal_triangle(n):
    """
    returns a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    big = []
    for x in range(n):
        small = []
        small.append(1)
        if x > 1:
            for j in range(x - 1):
                small.append(big[x - 1][j] + big[x - 1][j + 1])
        if x != 0:
            small.append(1)
        big.append(small)
    return big
