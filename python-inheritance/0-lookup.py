#!/usr/bin/python3


"""return list of attributs and method of an object"""
  
  
def lookup(obj):
    """
    Args :
    obj : object whose attributes and methods are listed
    rerturn : list content the name of  attributs and method
    """
    return dir(obj)
