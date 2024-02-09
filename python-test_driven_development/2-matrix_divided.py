#!/usr/bin/python3


"""Write a function that divides all elements of a matrix."""

def matrix_divided(matrix, div):


    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(elem, (int, float)) for row in matrix for elem in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    return [[round(elem / div, 2) for elem in row] for row in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("2-matrix_divided.txt")

