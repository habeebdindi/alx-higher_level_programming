#!/usr/bin/python3
"""
cotains function tha appends to file
"""


def append_write(filename="", text=""):
    """
    Adds text to a file

    Returns: no of characters added to file

    Args:
        filename (str): name of the file
        text (str): text to be added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        append_data = f.write(text)
        return append_data
