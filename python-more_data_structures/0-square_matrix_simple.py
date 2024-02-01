#!/usr/bin/python3

#  function that computes the square value of all integers of a matrix.

def square_matrix_simple(matrix=[]):

    result_matrix = list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))

    return result_matrix