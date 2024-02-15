#!/usr/bin/python3
"""return if instance is inherited"""


def is_kind_of_class(obj, a_class):
    """check if object is a a_class instance"""
    if isinstance(obj, a_class):
        return True
    return False

