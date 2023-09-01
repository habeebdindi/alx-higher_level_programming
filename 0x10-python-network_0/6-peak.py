#!/usr/bin/python3
"""
contains a funct
"""


def find_peak(arr):
    """
    Function finds peak
    """
    n = len(arr)
    for i in range(n):
        if (i == 0 or arr[i - 1] <= arr[i]) and \
           (i == n - 1 or arr[i + 1] <= arr[i]):
            return arr[i]
    return None  # No peak found
