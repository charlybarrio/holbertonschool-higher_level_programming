#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = []
    if my_list is None:
        return
    for a in my_list:
        if a not in new_list:
            new_list.append(a)
    return sum(new_list)
