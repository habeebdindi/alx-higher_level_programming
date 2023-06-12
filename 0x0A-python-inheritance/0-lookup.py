#!/usr/bin/python3
"""
This module contains one function
"""


def lookup(obj):
    """
    Returns obj's dicts
    """
    return [attr for attr in dir(obj)]
