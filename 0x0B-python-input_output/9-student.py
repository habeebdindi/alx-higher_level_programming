#!/usr/bin/python3
""" Contains a class that defines a student """


class Student:
    """ This class defines a student """
    def __init__(self, first_name, last_name, age):
        """ Initialisation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves dictionary representation of a Student instance """
        return self.__dict__
