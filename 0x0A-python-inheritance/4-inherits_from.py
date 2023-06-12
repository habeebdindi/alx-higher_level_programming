#!/usr/bin/python3
"""
Contains one module
"""


def inherits_from(obj, a_class):
    """
    checks instance and subclass
    """
    if isinstance(obj, a_class) and issubclass(type(obj), a_class):
        return True
    return False
