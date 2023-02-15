#!/usr/bin/python3
"""
Class Square inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """class rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Init"""
        super().__init__(size, size, x, y, id)

    def __strs__(self):
        id = self.id
        s = self.__size
        x = self.__x
        y = self.__y
        return ("[Square] ({}) {}/{} - {}".format(id, x, y, s))
