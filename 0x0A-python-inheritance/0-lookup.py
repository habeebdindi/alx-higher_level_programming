#!/usr/bin/python3
"""
This module contains one function
"""


def lookup(obj):
    """
    Returns obj's dicts
    """
    my_l = []
    for i in obj.__dict__:
        my_l.append(i)
    return my_l
