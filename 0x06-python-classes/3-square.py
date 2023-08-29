#!/usr/bin/python3

"""
Class Square that defines a square
"""
class Square:
    """
    Class Square that defines a square
    """

    def __init__(self, size=0):
        """
        Initialize square

        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size  #: size of the square

    def area(self):
        """
        Returns the area.

        Returns:
            Area.
        """
        return (self.__size**2)
