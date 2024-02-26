#!/usr/bin/python3
"""create class rectangle"""
from models.base import Base


class Rectangle(Base):
    """Create a class Rectangle inherit Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """allows access to the value of width as a property"""
        return self.__width

    @width.setter
    def width(self, value):
        """"Setter method for width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """allows access to the value of height as a property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method for height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """allow acces to the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter method for x-coordinate."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """allow acces to the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter method for y-coordinate."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """return area"""
        return (self.__width * self.__height)

    def display(self):
        """Display"""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print((" " * self.x) + ("#" * self.width))

    def __str__(self):
        """return str of the rectangle"""
        return "[rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update the attribut"""
        if args:
            attribs = ['id', 'width', 'height', 'x', 'y']
            for attr, value in zip(attribs, args):
                setattr(self, attr, value)
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return dict of a Rectangle"""
        return {'y': self.y, 'x': self.x, 'id': self.id, 'width': self.width,
                'height': self.height}
