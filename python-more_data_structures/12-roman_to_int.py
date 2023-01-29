#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, (str, type(None))):
        return 0
    else:
        letter_val = {
                'I': 1,
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D': 500,
                'M': 1000}
    value = 0
    for x in range(len(roman_string)):
        a = roman_string[x]
        b = roman_string[x - 1]
        if x > 0 and letter_val[a] > letter_val[b]:
            value += letter_val[a] - 2 * letter_val[b]
        else:
            value += letter_val[a]
    return value
