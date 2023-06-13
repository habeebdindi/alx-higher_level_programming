#!/usr/bin/python3
""" Save json to file """
import json


def save_to_json_file(my_obj, filename):
    """ serializes to a file """
    with open(filename, mode='w', encoding="utf-8") as f:
        json.dump(my_obj, f)
