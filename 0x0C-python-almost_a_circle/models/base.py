#!/usr/bin/python3
"""This module contains a base class, which would be later subclassed.
"""
import json
import os


class Base:
    """ Manages `id` attribute in all future classes to avoid code duplication.

    Attributes:
        __nb_objects(int): Total number of objects created.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation.
        Args:
            id (int): id of the class.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON representation of list_dictionaries

        Args:
            list_dictionaries(:obj:`list` of `dicts`): list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return str([])
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file

        Args:
            list_objs(:obj:`list` of `objs`): list of instances that inherit
            from Base.
        """
        if list_objs is None or len(list_objs) <= 0:
            with open("{}.json".format(cls.__name__), mode='w') as f:
                f.write(str([]))
        else:
            list_dict = [obj.to_dictionary() for obj in list_objs]

            with open("{}.json".format(cls.__name__), mode='w') as f2:
                f2.write(str(Base.to_json_string(list_dict)))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string
        """
        if json_string is None:
            return []
        else:
            return list(json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        """
        dummy = cls(1, 3)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances.
        """
        f = cls.__name__ + ".json"
        if not os.path.exists(f):
            return []
        with open(f, 'r') as fil:
            json_data = fil.read()
        data_list = cls.from_json_string(json_data)
        instance_list = []
        for data in data_list:
            instance = cls.create(**data)
            instance_list.append(instance)
        return instance_list
