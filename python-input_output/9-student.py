#!/usr/bin/python3
"""create class Student that defines a student"""


class Student:
    def __init__(self, first_name, last_name, age):
        """initialized a class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """that retrieves a dictionary representation of a Student"""
        return self.__dict__
    