#!/usr/bin/python3
class Square:
    """ A class representing a square"""

    def __int__(self, size=0):
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
