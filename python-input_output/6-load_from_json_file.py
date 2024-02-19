#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Create a python object"""
    with open(filename) as f:
        return json.loads(f)
