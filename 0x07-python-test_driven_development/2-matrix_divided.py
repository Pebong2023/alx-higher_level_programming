def matrix_divided(matrix, div):
    """Divides the integer/float numbers of a matrix.

    Args:
        matrix (list of lists): A list of lists containing integers/floats.
        div (int or float): The number used for division.

    Returns:
        list of lists: A new matrix with the result of the division.

    Raises:
        TypeError: If the elements of the matrix aren't lists,
                   if the elements of the lists aren't integers/floats,
                   if div is not an integer/float number,
                   if the lists of the matrix don't have the same size.
        ZeroDivisionError: If div is zero.
    """
    # Check if div is a number and not zero
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if all lists in the matrix have the same length
    msg_size = "Each row of the matrix must have the same size"
    len_e = len(matrix[0])
    if any(len(row) != len_e for row in matrix):
        raise TypeError(msg_size)

    # Check if all elements in the matrix are integers or floats
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg_type)
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError(msg_type)

    # Perform the division and round to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    return (new_matrix)
