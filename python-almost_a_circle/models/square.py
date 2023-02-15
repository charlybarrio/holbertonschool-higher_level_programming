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

    def __str__(self):
        id = self.id
        s = self.width
        x = self.x
        y = self.y
        return ("[Square] ({}) {}/{} - {}".format(id, x, y, s))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if args:
            att = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, att[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        id = self.id
        s = self.width
        x = self.x
        y = self.y
        return {'id': id, 'x': x, 'size': s, 'y': y}
