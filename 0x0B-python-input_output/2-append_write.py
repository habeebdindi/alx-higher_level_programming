#!/usr/bin/python3
""" Contains one function """


def append_write(filename="", text=""):
    """ appends to a file """
    with open(filename, mode='a', encoding="utf-8") as f:
        nb = f.write(text)
    return nb
