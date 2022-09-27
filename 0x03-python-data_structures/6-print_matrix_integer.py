#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    #l1 = [[row[i] for row in matrix] for i in range(3)]
    for i in matrix:
        lent = len(i)
        for i2 in i:
            print("{}".format(i2))
