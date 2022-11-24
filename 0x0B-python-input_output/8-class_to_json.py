#!/usr/bin/python3
"""
Conatains one module, check module desc for more info
"""


def class_to_json(obj):
    """
    Returns: dict description of a class instance

    Args:
        obj: object of any type
    """
    return obj.__dict__
