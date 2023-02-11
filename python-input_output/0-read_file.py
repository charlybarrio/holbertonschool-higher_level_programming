#!/usr/bin/python3
"""
Read a text file and prints it
"""


def read_file(filename=""):
    """Function"""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
