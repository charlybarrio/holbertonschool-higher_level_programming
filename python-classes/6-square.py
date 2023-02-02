#!/usr/bin/python3
"""
A class representing a square
"""


class Square:
    """
    define a square object
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialize with a size
        """
        po = position
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
        if not isinstance(po, tuple) or len(po) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(po[0], int) or not isinstance(po[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif po[0] < 0 or po[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(position, tuple)  or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        Area = self.__size * self.__size
        return Area

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print("" * self.__position[1])
        for i in range(self.__size):
            print(" " * self.__position[0])
            print("#" * self.__size)

