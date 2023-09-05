def add_integer(a, b=98):
    """Function that adds two integer and/or float numbers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number (default is 98).

    Returns:
        int: The addition of the two given numbers.

    Raises:
        TypeError: If a or b are not integer and/or float numbers.

    Example:
        >>> add_integer(5, 3.5)
        8

        >>> add_integer(2)
        100

        >>> add_integer(2.5, 3.5)
        6
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
