#!/usr/bin/python3
"""create class rectangle"""


class Rectangle(Base):
    def __init__(self, height, width, x = 0, y = 0, id = None):
        super().__init__(id)
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        
    @property
    def width(self):
        """allows access to the value of width as a property"""
        return self.__width

    @width.setter
    def width(self, value):
        """let define a value of width with a verification"""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Width must be a positive number")
        self.__width = value

    @property
    def height(self):
        """allows access to the value of height as a property"""
        return self.__height

    @height.setter
    def height(self, value):
        """let define a value of height with a verification"""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Height must be a positive number")
        self.__height = value

    @property
    def area(self):
        """Define a area property"""
        return self.__width * self.__height

    @property
    def perimeter(self):
        """Define a perimeter property"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Convert into a string"""
        return f"Rectangle(width={self.__width}, height={self.__height})"
    
    def display(self):
        for _ in range(self.__height):
            print('#' * self.__width)

    def update(self, *args, **kwargs):
        if args:
            if len(args) >= 1:
                self.width = args[0]
            if len(args) >= 2:
                self.height = args[1]
            if len(args) >= 3:
                self.__id = args[2]
        if kwargs:
            self.width = kwargs.get('width', self.width)
            self.height = kwargs.get('height', self.height)
            self.__id = kwargs.get('id', self.__id)

    def to_dictionary(self):
        return {'width': self.__width, 'height': self.__height, 'id': self.__id}
    