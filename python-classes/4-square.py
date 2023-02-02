#!/usr/bin/python3
"""
A class representing a square
"""


class Square:
    """
    define a square object
    """
    def __init__(self, size=0):
        """
        initialize with a size
        """
        try:
            if not isinstance(size, int):
                raise TypeError
            if size < 0:
                raise ValueError
            self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")
    
    @property
    def size(self):
        return self.__size

    @size.setter
    def int(size, value):
        self.__size = value

    def area(self):
        Area = self.__size * self.__size
        return Area
