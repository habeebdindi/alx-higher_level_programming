#!/usr/bin/python3
"""
Module contains a matrix calculator
"""


def matrix_divided(matrix, div):
    """
    This function divides all elements of a matrix and rounds them to 2 d.p

    Args:
        matrix (list): a list of lists, all elements are int/float
        div (int): divisor

    Returns:
        retruns a new matrix containing the divided elements
    """
    my_matrix = []
    if not type(matrix) is list:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    sub_matrix_len = len(matrix[0])
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for m_list in matrix:
        if not type(m_list) is list:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        if len(m_list) != sub_matrix_len:
            raise TypeError("Each row of the matrix must have the same size")
        for li_member in m_list:
            if type(li_member) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
        rounded = [round((x / div), 2) for x in m_list if type(x) in
                   [int, float]]
        my_matrix.append(rounded)
    return my_matrix
