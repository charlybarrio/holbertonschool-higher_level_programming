#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        print("")
    else:
        for a in reversed(my_list):
            print("{:d}".format(a))
