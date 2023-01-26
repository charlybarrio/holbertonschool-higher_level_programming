#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        n = 0
        for a in i:
            n += 1
            if len(i) != n:
                print("{:d}".format(a), end=" ")
            else:
                print("{:d}".format(a), end="")
            print()

