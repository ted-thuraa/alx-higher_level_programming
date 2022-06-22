#!/usr/bin/python3
"""Square main"""


class Square():
    """Square class"""

    def __init__(self, size=0):
        """ Instance of class Square

    Arguments:
        
        @size: size of side of square"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ area of square

        return:

            area of square."""
        return self.__size * self.__size

    @property
    def size(self):
        """ getter of size

    Return:

        value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ setter of the size

    Arguments:

        value: value of size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
