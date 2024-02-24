#!/usr/bin/python3
"""Create a class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Create class square that inherit from class rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """return square"""
        return "[Square], ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
