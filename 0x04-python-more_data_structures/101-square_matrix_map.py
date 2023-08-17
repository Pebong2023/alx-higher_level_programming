#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    """
    Calculate the square of each element in a matrix using map and lambda functions.
    """
    squared_matrix = (list(map(lambda row: list(map(lambda y: y ** 2, row)), matrix)))
    return( squared_matrix)
