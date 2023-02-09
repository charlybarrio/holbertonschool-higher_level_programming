#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""

class MyList(list):
    """
    Class
    """

    def print_sorted(self):
        """
        print list
        """
        list = sorted(self)
        print(list)
