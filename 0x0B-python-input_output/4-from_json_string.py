#!/usr/bin/python3
""" Contains one function  """
import json


def from_json_string(my_str):
    """ returnds objec represented by jsom """
    return json.loads(my_str)
