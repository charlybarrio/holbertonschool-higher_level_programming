#!/usr/bin/python3
"""
return true if is a class module
"""


def is_kind_of_class(obj, a_class):
    """
    True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class
    """
    return isinstance(obj, a_class)
