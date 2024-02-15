#!/usr/bin/python3
"""Function that return True for good instance or false for otherwise"""


def is_same_class(obj, a_class):
    """Args: object, a_class"""
    return type(obj) is a_class
