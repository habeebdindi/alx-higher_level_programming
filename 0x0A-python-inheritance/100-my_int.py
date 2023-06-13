#!/usr/bin/python3
"""
Module contains a class
"""


class MyInt(int):
    """ Contains dunder methods used for class comparison """
    def __eq__(self, other):
        """ doc """
        return super().__ne__(other)

    def __ne__(self, other):
        """ doc here """
        return super().__eq__(other)
