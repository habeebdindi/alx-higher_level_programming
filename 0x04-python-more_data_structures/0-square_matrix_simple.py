#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    cpy = matrix.copy()
    ret = []
    fin = []
    for i in cpy:
        ret = list(map(lambda x: x ** 2, i))
        fin.append(ret)
    return fin
