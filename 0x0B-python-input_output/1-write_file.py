#!/usr/bin/python3
""" Contains one function """


def write_file(filename="", text=""):
    """ writes to a file """
    with open(filename, mode='x', encoding="utf-8") as f:
        nb = f.write(text)
    return nb
