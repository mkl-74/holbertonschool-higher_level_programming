#!/usr/bin/python3
"""create class rectangle"""
from models.base import Base


class Rectangle(Base):
    """Create a class Rectangle inherit Base"""
    def __init__(self, height, width, x=0, y=0, id=None):
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    @property
    def width(self):
        """allows access to the value of width as a property"""
        return self.__width

    @width.setter
    def width(self, value):
        """let define a value of width with a verification"""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Width must be a positive number")
        self.__width = value

    @property
    def height(self):
        """allows access to the value of height as a property"""
        return self.__height

    @height.setter
    def height(self, value):
        """let define a value of height with a verification"""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Height must be a positive number")
        self.__height = value
