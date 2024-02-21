#!/usr/bin/python3
"""Create a class Square"""


class Square(Rectangle):
    def __init__(self, size):
        """Initialize """
        super().__init__(size, size)
        
    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.width = args[0]
                self.height = args[0]
            if len(args) >= 2:
                self.__id = args[1]
        if kwargs:
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.__id = kwargs.get('id', self.__id)
