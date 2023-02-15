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

    @classmethod
    def save_to_file(cls, list_objs):
        """Json string that represent the list_obj in a file"""
        if list_objs is None:
            list_objs = "[]"
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            obj_list = [obj.to_dictionary() for obj in list_objs]
            json_str = cls.to_json_string(obj_list)
            f.write(json_str)
