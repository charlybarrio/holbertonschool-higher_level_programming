#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    try:
        for a in range(x):
            print("{:d}".format(a), end="")
            n += 1
    except:
        pass
    return n
