#!/usr/bin/python3

"""
   a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
       Matrix : n x n
       div : <int,float>
       Return: n / div for all n in matrix
    """
    
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
     
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
                        
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide all elements of the matrix by div, rounded to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix

