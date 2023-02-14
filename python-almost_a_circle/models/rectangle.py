#!/usr/bin/python3
"""
Class Rectangle inherits from Base
"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        super(self.__class__, self).__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area"""
        Area = self.__width * self.__height
        return Area

    def display(self):
        """Print a rectangle with #"""
        for a in range(self.__y):
            print('')
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        id = self.id
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, w, h))

    def update(self, *args):
        """assigns arguments to the atributes"""
        id = self.id
        w = self.__width
        h = self.__height
        x = self.__x
        y = self.__y
        att = [id, w, h, x, y]
        for i in range(len(args)):
            att[i] = args[i]
        self.id = att[0]
        self.__width = att[1]
        self.__height = att[2]
        self.__x = att[3]
        self.__y = att[4]
