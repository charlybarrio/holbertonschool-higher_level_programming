#!/usr/bin/python3
"""function that divides a matrix"""


def matrix_divided(matrix, div):
    """Inizializes"""
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            msj = "matrix must be a matrix (list of lists) of integers/floats"
            if type(element) not in [int, float]:
                raise TypeError(msj)

    return [[round(element / div, 2) for element in row] for row in matrix]
