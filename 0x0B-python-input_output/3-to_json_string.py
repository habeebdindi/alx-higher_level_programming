#!/usr/bin/python3
"""
Contains a function for serializing
"""
import json


def to_json_string(my_obj):
    """
    Serializes an object

    Returns (str): JSON representation of an object

    Args:
        my_obj (str): the object to be serialized
    """
    return json.dumps(my_obj)
