#!/usr/bin/python3
"""
Writes a string to a text file, return num of char
"""


def write_file(filename="", text=""):
    """Function"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
