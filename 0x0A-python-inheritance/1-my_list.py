#!/usr/bin/python3
"""
This module contains a single class
"""


class MyList(list):
    """
    This class contains a single method
    """
    def print_sorted(self):
        """
        This method prints an inherited list attribute in asc order
        """
        print(sorted(self))
