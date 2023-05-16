#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 0
        while i < len(row):
            print("{}".format(row[i]), end="")
            if i != len(row) - 1:
                print(", ", end="")
            i += 1
        print("")
