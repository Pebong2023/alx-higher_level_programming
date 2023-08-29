#!/usr/bin/python3

"""
Define a class Square that defines a square.
"""

class Square:
    """
    Represents a square.
    """
    def __init__(self, size=0):
        """
        Initialize a square instance.
        
        Args:
            size (int): Size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Get or set the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): Size of the square.
        
        Raises:
            TypeError: If the value is not a number.
            ValueError: If the value is negative.
        """
        if not isinstance(value, (int, float)):
            raise TypeError('size must be a number')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __lt__(self, other):
        """
        Compare the size of this square with another square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this square's size is less than the other's, False otherwise.
        """
        return self.size < other.size

    def __le__(self, other):
        """
        Compare the size of this square with another square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this square's size is less than or equal to the other's, False otherwise.
        """
        return self.size <= other.size

    def __eq__(self, other):
        """
        Compare the size of this square with another square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this square's size is equal to the other's, False otherwise.
        """
        return self.size == other.size

    def __ne__(self, other):
        """
        Compare the size of this square with another square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this square's size is not equal to the other's, False otherwise.
        """
        return self.size != other.size

    def __ge__(self, other):
        """
        Compare the size of this square with another square.

        Args:
            other (Square): Another square to compare with.

        Returns:
            bool: True if this square's size is greater than or equal to the other's, False otherwise.
        """
        return self.size() >= other.size()
