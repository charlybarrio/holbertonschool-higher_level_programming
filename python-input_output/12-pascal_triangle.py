#!/usr/bin/python3
"""
Pascals Triangle
"""


def pascal_triangle(n):
    """Function"""
    pascal = []
    if n <= 0:
        return pascal
    row = [1]
    pascal.append(row)
    for a in range(1, n):
        next_row = [1]
        for b in range(1, a):
            next_row.append(row[b - 1] + row[b])
        next_row.append(1)
        pascal.append(next_row)
        row = next_row
    return pascal
