#!/usr/bin/python3
"""modul square"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """Initialized square"""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """check if size < 0 or size is not an integer """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return square area"""
        return (self.__size ** 2)

    def my_print(self):
        """print the square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
