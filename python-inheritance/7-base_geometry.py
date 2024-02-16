#!/usr/bin/python3
"""write a empty class"""


class BaseGeometry:
    """create a empty class"""
    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate or raise exception"""
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        return value
