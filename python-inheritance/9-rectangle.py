#!/usr/bin/python3
"""writ a class rectangle thath inherit from BaseGeometrie"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherit of baseGeometrie"""
    def __init__(self, width, height):
        """initialized rectanctangle
        Args :
        Height : The height of the rectangle
        width : The width of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Area of th rectangle"""
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle]' + str(self.__width) + "/" + str(self.__height)
