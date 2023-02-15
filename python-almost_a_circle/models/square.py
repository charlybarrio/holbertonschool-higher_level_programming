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

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def __strs__(self):
        id = self.id
        s = self.width
        x = self.x
        y = self.y
        return ("[Square] ({}) {}/{} - {}".format(id, x, y, s))
