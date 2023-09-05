import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy's np.matmul.

    Args:
        m_a (numpy.ndarray): The first matrix.
        m_b (numpy.ndarray): The second matrix.

    Returns:
        numpy.ndarray: The result of the matrix multiplication.
    """
    return np.matmul(m_a, m_b)
