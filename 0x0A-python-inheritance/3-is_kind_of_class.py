#!/usr/bin/python3
"""
3-is_kind_of_class : 1 function
"""


def is_kind_of_class(obj, a_class):
    """Checks if object is a subclass of class

    Args:
    obj (obj:`object`): any object
    a_class (class): any class
    """
    if issubclass(type(obj), a_class):
        return True
    return False
