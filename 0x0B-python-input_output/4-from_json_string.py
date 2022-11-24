#!/usr/bin/python3
"""
contains one function
"""
import json


def from_json_string(my_str):
    """
    Function reconstructs data form string representation

    Returns an object represented by a JSON string

    Args:
        my_str (str): JSON sttring
    """
    return json.loads(my_str)
