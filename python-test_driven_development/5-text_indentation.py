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
    bool = False
    for i in range(len(text)):
        if text[i] == "." or text[i] == "?" or text[i] == ":":
            print(text[i] + '\n')
            bool = True
        if bool:
            if text[i + 1] == " ":
                continue
            bool = False
        else:
            print(text[i], end="") 
