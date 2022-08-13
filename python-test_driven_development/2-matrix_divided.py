#!/usr/bin/python3
""" this module defines the matrix division function """


def matrix_divided(matrix, div):
    """ this function divides all elements of a matrix """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new = []
    if mtrix is None or len(matrix) is 0 or len(matrix[0]) is 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if all(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("each row of the matrix must have the same size")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix]))
