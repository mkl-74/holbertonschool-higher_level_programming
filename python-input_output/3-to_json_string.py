#!/usr/bin/python3
import json


"""
return json representation of an object
"""


def to_json_string(my_obj):
    """_summary_
    Args:
    my_obj (list):
    """
    print(json.dumps(my_obj))
