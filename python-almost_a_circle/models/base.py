#!/usr/bin/python3
"""create a classe base"""


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
