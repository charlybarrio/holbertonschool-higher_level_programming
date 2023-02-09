#!/usr/bin/python3
"""
True if the obj is an instance of a class from the specifield class
"""


def inherits_from(obj, a_class):
    """function"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
