#!/usr/bin/python3
"""
A module for file handling
"""
import json


def load_from_json_file(filename):
    """
    Deserializes a JSON file
    Args:
        filename(str): name of the file
    """
    with open(filename, 'w') as f:
        return json.load(f)
