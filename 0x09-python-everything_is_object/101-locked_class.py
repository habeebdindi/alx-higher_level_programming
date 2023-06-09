#!/usr/bin/python3
"""
Contains one class
"""


class LockedClass(object):
    """
    Allows access to only a specific instance
    """

    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        """
        sets an instance attribute if only it's name is first_name
        """
        if name not in self.__slots__:
            raise AttributeError("'LockedClass' object has no attribute '{}'".
                                 format(name))
        super().__setattr__(name, value)
