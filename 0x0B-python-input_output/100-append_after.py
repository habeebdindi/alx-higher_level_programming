#!/usr/bin/python3
"""
Searches and updates
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to file after each line containing a specific string
    """
    with open(filename, mode='r') as f:
        fcontent = f.readlines()

    new_content = []

    for line in fcontent:
        if line.strip() == search_string or search_string in line:
            new_content.append(line)
            new_content.append(new_string)
        else:
            new_content.append(line)

    with open(filename, mode='w') as f2:
        f2.writelines(new_content)
