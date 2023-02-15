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
        filename = cls.__name__ + ".json"
        if list_objs:
            obj_list = [obj.to_dictionary() for obj in list_objs]
        else:
            obj_list = []
        json_str = cls.to_json_string(obj_list)
        with open(filename, "w") as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Json string representation jsonstring"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all atributes"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        instance_list = []
        if filename:
            with open(filename, 'r') as file:
                jsonstring = cls.from_json_string(file.read())
                for obj_dict in jsonstring:
                    instance_list.append(cls.create(**obj_dict))
            return instance_list
        else:
            return instance_list
