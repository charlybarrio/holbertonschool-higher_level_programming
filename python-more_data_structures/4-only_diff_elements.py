#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = set()
    for a in set_1:
        if a in set_2:
            continue
        else:
            new.add(a)
    for a in set_2:
        if a in set_1:
            continue
        else:
            new.add(a)
    return new
