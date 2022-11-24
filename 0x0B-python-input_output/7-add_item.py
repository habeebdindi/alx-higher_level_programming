#!/usr/bin/python3
"""
This module takes arguments from the shell.
This module adds arguments to a list
This module serializes the list
"""
import sys
import json
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


try:
    arg_list = load("add_item.json")
except FileNotFoundError:
    arg_list = []
arg_list += sys.argv[1:]
save(arg_list, "add_item.json")
