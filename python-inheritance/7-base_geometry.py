#!/usr/bin/python3
"""write a empty class"""


class BaseGeometry:
    """create a empty class"""
    def area(self):
        """raise excerption"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate or raise exception"""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
        return value
