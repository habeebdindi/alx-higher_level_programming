#!/usr/bin/python3
""" Loads, adds, and saves """
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

final = []
my_list = []
for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])

if os.path.exists("add_item.json"):
    final += list(load_from_json_file("add_item.json"))

save_to_json_file(my_list, "add_item.json")

final += list(load_from_json_file("add_item.json"))
save_to_json_file(final, "add_item.json")
