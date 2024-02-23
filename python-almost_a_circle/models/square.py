#!/usr/bin/python3
"""Create a class Square"""


from models.rectangle import rectangle


class Square(rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize """
        super().__init__(size, size, x, y, id)
        self.size = size
