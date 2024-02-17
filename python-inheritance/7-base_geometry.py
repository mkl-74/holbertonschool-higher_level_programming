#!/usr/bin/python3
"""write a class BaseGeometry"""


class BaseGeometry:
    """create a empty class"""
    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate or raise exception
        Args :
        name : name of the parameter(str)
        value : value is an integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
