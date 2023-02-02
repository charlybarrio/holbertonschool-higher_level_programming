#!/usr/bin/python3
 """ A class representing a square"""


class Square:
    """define a square object"""
    def __init__(self, size=0):
        """initialize with a size"""
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
