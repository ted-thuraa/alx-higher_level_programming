#!/usr/bin/python3
"""square class main"""

class Square:
    """square class"""

    def __init__(self, size=0):
        """ Instance of class Square

        Arrguments:

                @size: size of side of square"""

        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    def area(self):
        """ area of square

        return:

        area of square."""
        return self.__size * self.__size
