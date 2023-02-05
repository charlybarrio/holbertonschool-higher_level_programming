#!/usr/bin/python3
"""
Add two int
"""


def add_integer(a, b=98):
    """
    This function add 2 int.
    """
    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")
    return a + b
