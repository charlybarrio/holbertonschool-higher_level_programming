#!/usr/bin/python3i
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
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        Area = self.__size * self.__size
        return Area

    def my_print(self):
        if self.__size == 0:
            print ()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
