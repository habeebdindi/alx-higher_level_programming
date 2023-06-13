#!/usr/bin/python3
""" returns dictionary desc for a serialized object """


def class_to_json(obj):
    """ serializes obj and returns it in a dictionary """
    return obj.__dict__
