#!/usr/bin/python3
""" Create object from a JSON file """
import json


def load_from_json_file(filename):
    """ deserializes from a file """
    with open(filename, mode='r', encoding="utf-8") as f:
        x = json.load(f)
    return x
