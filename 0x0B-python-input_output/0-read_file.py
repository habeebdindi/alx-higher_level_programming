#!/usr/bin/python3
"""
This module contains a function for reading a text file
"""


def read_file(filename=""):
    """
    This function reads a text file and prints it to stdout

    Args:
        filename (str): name of the file
    """
    with open('filename', 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
