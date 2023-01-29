#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    n = 0
    for a in range(x):
        try:
            print("{:d}".format(my_list[a]), end="")
            n += 1
    except:
        pass
    print()
    return n
