#!/usr/bin/python3
"""Square main class"""

class Square():
    """square class"""
    def __init__(self, size=0):

        """ Instance of square

    Arguments:
            @size: size of one side of square """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Function that gets the area of a square

        Returns:
            area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Size getter

        Returns:
            size of side of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Size property setter

        Arguments:
                value: value to set as size
        """
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Square printer

        """
        if (self.size == 0):
            print("")
        for i in range(self.size):
            print("#" * self.size)
