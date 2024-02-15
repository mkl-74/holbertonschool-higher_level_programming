#!/usr/bin/python3
"""return if instance of class that inherited directly or indirectly"""


def inherits_from(obj, a_class):
    """
    check if object is subclass 

    """
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
