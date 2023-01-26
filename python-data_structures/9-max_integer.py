#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    for a in my_list:
        while my_list[a] < my_list[a + 1]:
            a += 1
        max = my_list[a]
        return max
