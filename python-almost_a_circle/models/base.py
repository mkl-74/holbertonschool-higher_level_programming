#!/usr/bin/python3
"""create a classe base"""

class Base(__nb_objects = 0):
    """create a class Base"""
    def __init__(self, id=None):
        
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
