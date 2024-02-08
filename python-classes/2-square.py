#!/usr/bin/python3
"""square modul"""


class Square:
    """class that defines a square"""
    def __init__(self, size=0):
        """ init new square with his size is an >0 int in private attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size