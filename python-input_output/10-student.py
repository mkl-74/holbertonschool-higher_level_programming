#!/usr/bin/python3
"""class Student that defines a student by: (based on 9-student.py)"""


class Student():
    """create a class Student"""
    def __init__(self, first_name, last_name, age):
        """create a Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student"""
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for i in attrs:
            try:
                new_dict[i] = self.__dict__[i]
            except Exception:
                pass

            return new_dict
