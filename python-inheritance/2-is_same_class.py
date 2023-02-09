#!/usr/bin/python3
"""
Return true if the obj is exactly an instance of the class, if not False
"""


def is_same_class(obj, a_class):
    """compare obj and instance"""
    return isinstance(obj, a_class)

is_same_class(1, int)    # True
is_same_class(1, object) # Fale
