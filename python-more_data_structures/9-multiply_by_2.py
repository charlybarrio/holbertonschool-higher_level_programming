#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    new_dic.update((key, value * 2) for key, value in new_dic.items())
    return new_dic
