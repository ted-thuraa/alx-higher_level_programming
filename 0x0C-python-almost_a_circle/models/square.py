#!/usr/bin/python3
"""Tha Square"""

class Square(Rectangle):
    """Square class inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializer"""
        super().__init__(size, size, x, y, id)

def __str__(self):
    """overites the str"""
    return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id, self.x, self.y, self.width)

def size(self):
    """size getter"""
    return self.width

@size.setter
    def width(self, value):
        """ set width and height to same value """
        if not isinstance(value, int):
            raise TypeError("width ust be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value

        if not isinstance(value, int):
            raise TypeError("width ust be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if args is None and len(args) != 0:
            a = ["id", "size", "x", "y"]
            for i in len(args):
                if i > (len(a) - 1):
                    break
                setattr(self, a[i], args[i])
        else:
            for i in kwargs.keys():
                if i in args:
                    setattr(self, i, kwargs[i])

    def to_dictionary(self):
        """returns dict rep of a square"""
        temp = {}
        a = ["id", "size", "x", "y"]
        for i in a:
            temp[i] = getattr(self, i)
        return temp