#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new = set()
    for a in set_1:
        for a in set_2:
            continue
        else:
            new.add(a)
    for a in set_2:
        for a in set_1:
            continue
        else:
            new.add(a)
    return new
