#!/usr/bin/python3
def safe_print_division(a, b):
    c = 0
    try:
        c = a / b
    except:
        pass
    finally:
        print("Inside result: {:f}".format(c))
        return c

