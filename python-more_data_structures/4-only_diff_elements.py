#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_list = []
    if set_1 is None:
        return set_2
    if set_2 is None:
        return set_1
    for a in set_1:
        for b in set_2:
            if a != b:
                new_list.append(a)
        for c in set_2:
            for d in set_1:
                if c != d:
                    new_list.append(c)
    return(set(new_list))
