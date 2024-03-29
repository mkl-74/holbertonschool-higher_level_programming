#!/usr/bin/python3
"""write a class square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """initialized class square
    Args :
    size : the size of the square
    """
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
