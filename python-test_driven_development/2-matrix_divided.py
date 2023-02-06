#!/usr/bin/python3
"""Divides a given matrix by a given number"""


def matrix_divided(matrix, div):
    """division"""
    err = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError(err)
    if not all(map(lambda x: type(x) == list, matrix)):
        raise TypeError(err)
    if not all(map(lambda x: len(x) == len(matrix[0]), matrix)):
        raise TypeError("Each row of the matrix must have the same size")
    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
        raise TypeError(err)
    new_mx = []
    for lists in matrix:
        if len(lists) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        new_list = []
        for position in lists:
            if type(position) is not int and type(position) is not float:
                raise TypeError(err)
            new_list.append(round(position/div, 2))
        new_mx.append(new_list)
    return new_mx
