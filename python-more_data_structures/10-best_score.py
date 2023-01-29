#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        new_val = max(a_dictionary, key=lambda x: a_dictionary[x])
    return new_val
