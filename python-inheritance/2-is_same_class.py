#!/usr/bin/python3
"""
Return true if the obj is exactly an instance of the class, if not False
"""


def is_same_class(obj, a_class):
    """compare obj and instance"""
    return type(obj) == a_class
