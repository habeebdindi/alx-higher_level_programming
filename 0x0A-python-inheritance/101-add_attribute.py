#!/usr/bin/python3
"""
Contains one function
"""


def add_attribute(obj, name, value):
    """ adds attribute to an object """
    if hasattr(obj, '__dict__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
