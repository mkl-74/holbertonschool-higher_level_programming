#!/usr/bin/python3

# prints a matrix of integers


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        formatted_row = ""
        for num in row:
            formatted_row += "{:2} ".format(num)
        print(formatted_row.rstrip())