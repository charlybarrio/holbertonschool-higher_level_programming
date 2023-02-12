#!/usr/bin/python3
"""
appends a string at the end of a tx, return num of char
"""


def append_write(filename="", text=""):
    """Function"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
