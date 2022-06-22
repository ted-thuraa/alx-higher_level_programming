#!/usr/bin/python3
"""Square class main"""

class Square():
    """square class"""

    def __init__(self, size=0, position=(0, 0)):
        """ Square class
    Args:
        @size: size of side of square

        """
        self.__size = size
        self.__position = position

    def area(self):
        """ area of square
        Return:
            area of square."""

        return self.__size * self.__size

    @property
    def size(self):
        """size getter
    Return:
        value of size
        """
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
        else:
            self.__size = value

    @property
    def position(self):
        """position getter
    Return:
        value of position"""
        return self.__position

    @position.setter
    def position (self, value):
        """position setter
    Arguments:
        value: value of postion"""
        if ((len(value) != 2) or
                (type(value) is not tuple) or
                (type(value[0]) is not int) or (type(value[1]) is not int) or
                 (value[0] < 0) or (value[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ prints in stdout the square with the character #
        or a blank line if @size == 0"""

        if (self.size == 0):
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                for j in range(self.size + self.position[0]):
                    if j < self.position[0]:
                        print(" ", end='')
                    else:
                        print("#", end='')
                print()
