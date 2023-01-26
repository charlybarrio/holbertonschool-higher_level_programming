#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    for a in range(len(matrix)):
        new_matrix[a] = new_matrix[a] * a
