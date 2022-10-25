#!/usr/bin/python3
"""
4-inherits_from : 1 method

"""


def inherits_from(obj, a_class):
    """ Check obj if instance or inherited


    Args:
    obj (obj : 'object'): object
    a_class (class) : class
    """

    if not (isinstance(obj, a_class)) and issubclass(obj, a_class):
        return True
    return False
