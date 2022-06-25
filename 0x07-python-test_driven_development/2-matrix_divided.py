#!/usr/bin/python3
""" this module divides all elemnts of a matrix
"""

def matrix_divided(matrix, div):
    """ function that returns a new matrix with each element divided by da div

    Args:
        matrix: a 2d array, each row should be the same size or else: error
        div: a number that is not 0 or else error

    Returns: a new matrix with each element adjusted to the div amount
    """
    new = []
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    elif not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif len(matrix) == 0:
        return
    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            raise TypeError(error_1)
        for x in matrix[i]:
            if not isinstance(x, int) and not isinstance(x, float):
                raise TypeError(error_1)
        L = len(matrix[0])
        if len(matrix[i]) != L:
            raise TypeError(error_2)
    large = []
    for i in range(len(matrix)):
        new = []
        for x in matrix[i]:
            a = round(float(x)/float(div), 2)
            new.append(a)
        large.append(new)
    return large
