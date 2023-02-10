#!/usr/bin/python3
"""
Class Square inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)

    def area(self):
        return(self.__size ** 2)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
