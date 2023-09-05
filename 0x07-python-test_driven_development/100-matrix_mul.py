def matrix_mul(m_a, m_b):
    """Multiplies two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The result of the matrix multiplication.

    Raises:
        TypeError: If m_a or m_b are not lists.
        TypeError: If m_a or m_b are not lists of lists.
        ValueError: If m_a or m_b are empty.
        TypeError: If the elements in m_a or m_b are not integers or floats.
        TypeError: If the rows in m_a or m_b have different sizes.
        ValueError: If m_a and m_b cannot be multiplied.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a and m_b must be lists")

    for matrix in (m_a, m_b):
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError("m_a and m_b must be lists of lists")

    if not m_a or any(not row for row in m_a) or not m_b or any(not row for row in m_b):
        raise ValueError("m_a and m_b cannot be empty")

    for matrix in (m_a, m_b):
        for row in matrix:
            for element in row:
                if not isinstance(element, (int, float)):
                    raise TypeError("m_a and m_b should contain only integers or floats")

    m_a_rows = len(m_a)
    m_a_cols = len(m_a[0])
    m_b_cols = len(m_b[0])

    if any(len(row) != m_a_cols for row in m_a) or any(len(row) != m_b_cols for row in m_b):
        raise TypeError("Each row of m_a and m_b must have the same size")

    if m_a_cols != len(m_b):
        raise ValueError("m_a and m_b cannot be multiplied")

    result = [[0 for _ in range(m_b_cols)] for _ in range(m_a_rows)]

    for i in range(m_a_rows):
        for j in range(m_b_cols):
            for k in range(m_a_cols):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return (result)
