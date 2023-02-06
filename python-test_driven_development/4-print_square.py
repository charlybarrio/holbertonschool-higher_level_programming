#!/usr/bin/python3
"""
Print a square
"""


def print_square(size):
    """
    initializacion
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)

