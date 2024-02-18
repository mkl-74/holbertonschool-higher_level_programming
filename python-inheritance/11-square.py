#!/usr/bin/python3
"""write a new class square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Initialized new class square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """print"""
        return '[Square] {:d} / {:d}'.format(
            self._Rectangle__width,
            self._Rectangle__height
            )
