#!/usr/bin/python3
"""
contains a class and its methods

"""


class Student:
    """ class defines a student

    Attributes:
    first_name (obj : 'str') : first name
    last_name (obj : 'str') : last name
    age (obj : 'int') : age
    """

    def __init__(self, first_name, last_name, age):
        """ Initializing attributes """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
