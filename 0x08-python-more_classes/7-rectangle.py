#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the width."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle with '#' characters."""
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol * self.__width) for _ in range(self.__height)])

    def __repr__(self):
        """Return a string representation of the rectangle for reproduction."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
