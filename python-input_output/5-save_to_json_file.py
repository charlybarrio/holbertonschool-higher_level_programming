#!/usr/bin/python3
"""
writes an Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """Function"""
    with open(filename, "w") as f:
        json.dump(list(my_obj), f)
