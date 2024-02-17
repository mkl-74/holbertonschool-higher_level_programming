#!/usr/bin/python3
"""writ a class rectangle thath inherit from BaseGeometrie"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherit of baseGeometrie"""
    def __init__(self, width, height):
        """Initialized rectangel
        Args :
        Width of the rectangle
        height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
