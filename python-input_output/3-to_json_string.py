#!/usr/bin/python3
"""
return json representation of an object
"""
import json


def to_json_string(my_obj):
    """_summary_
    Args:
    my_obj (list):
    """
    return json.dumps(my_obj)
