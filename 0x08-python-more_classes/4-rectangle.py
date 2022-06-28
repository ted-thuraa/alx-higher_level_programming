#!/usr/bin/python3
"""Rectangle class to represent a rectangle"""

class Rectangle():
    """ initialize with the width and height with value checks
    Args:
        width: how phat dis 4polygon gon be
        height: how tall dis box is

    Return: notin
    """

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width of rectangle
        Return:
        width"""
        return self.__width

    @property
    def height(self):
        """ height of rectangle
        Returns:
        height"""
        return self.__height

    @width.setter
    def width(self, value):
         """ setter of the width
         Args:
            value: value of height"""
         if not isinstance(value, int):
             raise TypeError("height must be an integer")
         if value < 0:
             raise ValueError("height must be >= 0")
         self.__width = value
    @height.setter
    def height(self, value):
        """ setter of the width
        Args:
            value: value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area of rectangle
        Return:
        area of rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """ perimeter of rectangle
        Return:
        perimeter of rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ rectangle made using the character #
        """

        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for row in range(self.__height):
            if row < (self.__height - 1):
                string += ("#" * self.__width) + "\n"
            else:
                string += ("#" * self.__width)
        return string

    def __repr__(self):
        """ represent self for eval """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
