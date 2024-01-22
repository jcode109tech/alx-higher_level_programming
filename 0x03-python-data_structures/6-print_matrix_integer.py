#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    #prints a matrix of integers 
    for i in range(len(matrix)):
        i_len = len(matrix[i])
        for j in range(i_len):
            if j != i_len - 1:
                endCh = ' '
            else:
                endCh = ''
            print("{:d}".format(matrix[i][j]), end=endCh)
        print("")
 