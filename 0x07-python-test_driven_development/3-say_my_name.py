#!/usr/bin/python3
"""
This module prints your name
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints:
    "My name is <first name> <last name>"

    Args:
        first_name (str): a string containing your firstname
        last_name (str): a string containing your last name

    Returns:
        a string containing your fullname
    """
    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
