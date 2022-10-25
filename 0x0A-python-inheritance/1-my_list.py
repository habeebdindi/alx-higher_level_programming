#!/usr/bin/python3
"""
1-my_list : 1 class

"""


class MyList(list):
    """ Inherit list from MyList """

    def print_sorted(self):
        """ Print list ascending """
        ml = [i for i in self]
        ml.sort()
        print(ml)
