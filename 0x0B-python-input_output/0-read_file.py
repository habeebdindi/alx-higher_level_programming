#!/usr/bin/python3
""" Contains one function """


def read_file(filename=""):
    """ function reads a text file in UTF8 encoding """
    with open(filename, mode='r', encoding="utf-8") as f:
        contents = f.read()
        print(contents)
    return contents
