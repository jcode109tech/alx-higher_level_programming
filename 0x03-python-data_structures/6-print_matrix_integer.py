#!/usr/bin/pyhton3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{}".format(col), end=' ')
        print()