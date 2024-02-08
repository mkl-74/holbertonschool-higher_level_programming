#!/usr/bin/python3
"""square modul"""


class Square:
    """class that defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """init a new square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """retrieve size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """ def if size is an >0 int in private attribute"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ retrieve the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """ define if position is a tuple of two positive integers"""
        if not isinstance(value, tuple) or\
                len(value) != 2 or\
                not isinstance(value[0], int) or\
                not isinstance(value[1], int) or\
                value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ define the area of a square entrer in argument"""
        return (self.__size ** 2)

    def my_print(self):
        """print in stdout a # square of size __size"""
        if self.__size == 0:
            print("")
        else:
            for whiteline in range(0, self.position[1]):
                print("")
            for index in range(0, self.__size):
                print(" " * self.__position[0], end="")
                for index2 in range(0, self.__size):
                    print("#", end="")
                print("")
