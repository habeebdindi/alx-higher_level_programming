#!/usr/bin/python3
"""
contains a function for handling files
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file

    Args:
        my_obj (str): JSON data packet
        filename (str): name of the file to be written to
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return json.dump(my_obj, f)
