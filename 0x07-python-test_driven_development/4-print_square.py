#!/usr/bin/python3
""" prints a square with #
"""

def print_square(size):
    """ print_square printts a square with a #

    Args:
        size: size of square
    return square
    """
    if type(size) is int and size is not None:
        if size >= 0:
            for i in range(size):
                for j in range(size):
                    print("#", end='')
                print()
        else:
            raise TypeError("size must be >= 0")
    else:
        raise TypeError("size must be an integer")
