#!/usr/bin/python3

"""
Module for the subclass Rectangle.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """
    Rectangle that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, 'height', height)
        self.__height = height
        BaseGeometry.integer_validator(self, 'width', width)
        self.__width = width

    def area(self):
        """
        Calculate the area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the Rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
