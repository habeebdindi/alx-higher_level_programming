#!/usr/bin/python3
"""
Contains one class
"""


class LockedClass:
    """
    Allows access to only a specific instance
    """
    def __setattr__(self, name, value):
        """
        sets an instance attribute if only it's name is first_name
        """
        if not hasattr(self, name) and name != "first_name":
            raise AttributeError("'LockedClass' object has no attribute '{}'".
                                 format(name))
        super().__setattr__(name, value)
