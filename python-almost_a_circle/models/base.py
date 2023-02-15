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

    def save_to_file(cls, list_objs):
        """writes the JSON string representation of obj to a file"""
        filename = cls.__name__ + ".json"
        result = []
        if list_objs is not None:
            for atribute in list_objs:
                result.append(element.to_dictionary())
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(cls.to_json_string(result))
