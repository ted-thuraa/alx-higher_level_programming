#!/usr/bin/python3
"""Finds area and perimeter of a rectangle
"""

class Rectangle():
    """initialize with the width and height with value checks
    Args:
        width: wiiidth
        height: how high
    Return: notin
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """ Rectangle width
        Return:
        width"""
        return self.__width

    @property
    def height(self):
        """ Rectangle height
        Return:
        height"""
        return self.__height

    @width.setter
    def width(self, value):
        """ setter of the width
        Args:
        value: value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter of the height
        Args:
        value: value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """computes the area
        Returns:
        Area"""
        return self.__width * self.__height

    def perimeter(self):
        """computes the perimeter
        Returns:
        Perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)
