#!/usr/bin/python3
"""
prints a text with 2 new lines after few character
"""


def text_indentation(text):
    """
    Inizializes
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new = text.replace(".", ".\n\n").replace("?", "?\n\n").\
        replace(":", ":\n\n")
    print(new_text, end="")
