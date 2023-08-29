#!/usr/bin/python3

"""
Class Square that defines a square
"""
class Square:
    """
    Class Square that defines a square
    """
    def __init__(self, size=0):
        """ Initialize square

        Args:
            size (int): size of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        int: private size.

        Returns:
            Private size.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets value into size, must be int.

        Args:
            value (int): size of the square.
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value  #: size of the square

    def area(self):
        """
        Returns the area

        Returns:
            Area.
        """
        return (self.__size**2)

    def my_print(self):
        """
        Prints in stdout the square with the character #
        """

        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
