#!/usr/bin/python3

# prints a matrix of integers

def print_matrix_integer(matrix=[[]]):

    for row in matrix:
        print(" ".join("{:d}".format(num) for num in row))