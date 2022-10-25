#!/usr/bin/python3
"""
100-my_int : 1 class


"""


class MyInt(int):
    """ Class inheriting an int
    Switch (__eq__ : '==') and (__ne__ : '!=')

    (awful prank idea)
    """

    def __eq__(self, other):
        """ Set eq attribute to '!=' """

        return super().__ne__(other)

    def __ne__(self, other):
        """ Set ne attribut to '==' """

        return super().__eq__(other)
