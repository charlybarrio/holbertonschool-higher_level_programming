#!/usr/bin/python3
 """ A class representing a square"""


class Square:
    """define a square object"""
    def __init__(self, size=0):
        """initialize with a size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
