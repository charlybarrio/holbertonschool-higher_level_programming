#!/usr/bin/python3
"""
Class base
"""


import json


class Base:
    """class"""
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Json representation of list_dictiones"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
