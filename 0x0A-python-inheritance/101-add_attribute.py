#!/usr/bin/python3
"""
101-add_attribute : 1 function

"""


def add_attribute(an_obj, an_attr, a_value):
    """ Checks object if attribute with value can be added to it

    Args:
    an_obj(obj : 'object') object
    an_attr(attribute) attribute
    a_value(obj: 'object') add to attribute
    """

    if not hasattr(an_obj, '__slots__') and not hasattr(an_obj, '__dict__'):
        raise TypeError("Can't add new attribute")
    if hasattr(an_obj, '__slots__') and not hassattr(an_obj, an_attr):
        raise TypeError("can't add new attribute")

    setattr(an_obj, an_attr, a_value)
