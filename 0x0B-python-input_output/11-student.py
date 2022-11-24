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

    def to_json(self, attrs=None):
        if not type(attrs) is list:
            return self.__dict__
        for i in attrs:
            if not type(i) is str:
                return self.__dict__
        return {ki: val for ki, val in self.__dict__.items() if ki in attrs}

    def reload_from_json(self, json):
        """
        Replaces all the attributes of Student instance with the json file
        """
        for ki, val in json.items():
            self.__dict__[ki] = val
