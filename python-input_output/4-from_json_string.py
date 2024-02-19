#!/usr/bin/python3
"""fonction that return an object represented by a json string"""
import json

    
def from_json_string(my_str):
    """_summary_

    Args:
        my_str (obj) :
        

    Returns:
        _type_: _description_
    """
    return json.loads(my_str)
