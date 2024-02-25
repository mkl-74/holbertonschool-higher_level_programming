#!/usr/bin/python3
"""create a classe base"""
import json


class Base():
    """create a class Base"""
    _nb_objects = 0

    def __init__(self, id=None):
        """id condition"""
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return a json string representation of a list of dictionaries"""
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
