#!/usr/bin/python3
""" Contains a class that defines a student """


class Student:
    """ This class defines a student """
    def __init__(self, first_name, last_name, age):
        """ Initialisation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dictionary representation of a Student instance """
        if (attrs is not None):
            return {a: self.__dict__[a] for a in attrs if a in self.__dict__}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attribute of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
