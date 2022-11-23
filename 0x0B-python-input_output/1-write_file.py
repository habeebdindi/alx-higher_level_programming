#!/usr/bin/python3
"""
contains 1 function, write_file
"""


def write_file(filename="", text=""):
    """
    write string to a file and returns no. of characcters written

    Args:
        filename (str): name of the file
        text (str): the string
    """
    with open(filename, 'w', encoding="utf-8") as f:
        write_data = f.write(text)
        return write_data
