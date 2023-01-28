#!/usr/bin/python3
def best_score(a_dictionary):
     if a_dictionary is None:
         return None
     val = list(a_dictionary.values())
     keys = list(a_dictionary.keys())
     return keys[val.index(max(val))]
