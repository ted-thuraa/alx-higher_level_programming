#!/usr/bin/python3
"""More practise with classes"""

class Rectangle():
    """initialize with the width and height with value checks
    Args:
        width: tha width
        height: tha height
    Return: noughtin
    """
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ Tha widthh
        Returns:
            width
        """
        return self.__width
    @property
    def height(self):
        """ Tha height
        Returns:
            height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """ width setter
        Args:
            value: value of width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ height setter
        Args:
            value: value of height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ finds the area
        Returns:
            area
        """
        return  self.__height * self.__width

    def perimeter(self):
        """ finds the perimeter
        Returns:
            perimeter
        """
        return (2 * self.__height) + (2 * self.__width)

    def __str__(self):
        """ rectangle made using the character #
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    string += str(self.print_symbol)
                if i != self.__height - 1:
                    string += "\n"
            return string

    def __repr__(self):
        """ represent self for eval"""
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """delete self and count"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
