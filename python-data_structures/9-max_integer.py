#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    if len(my_list) == 1:
        return my_list[0]
    for a in range(len(my_list) - 1):
        while my_list[a] < my_list[a + 1]:
            a += 1
            if a == len(my_list) - 1:
                return my_list[a]
        max = my_list[a]
        return max
