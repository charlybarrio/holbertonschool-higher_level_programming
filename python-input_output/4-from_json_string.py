#!/usr/bin/python3
"""
Returns an object represented by Json string
"""


import json


def from_json_string(my_str):
    """Function"""
    return json.loads(my_str)
