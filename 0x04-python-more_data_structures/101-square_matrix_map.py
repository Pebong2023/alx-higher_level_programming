#!/usr/bin/python3

def square_matrix_map(matrix=[]):
    """
    Calculate the square of each element in a matrix using map and lambda functions.
    """
    squared_matrix = [[y**2 for y in row] for row in matrix]
    return (squared_matrix)
