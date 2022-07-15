#!/usr/bin/python3
"""Rectangle"""
from models.base import Base

class Rectangle(Base):
    """Rectangle class inherits from base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instatiator"""
        super().__init__(id) # this super call with use the logic of the __init__ of the Base class
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ set width of rectangle or set error value """
        if not isinstance(value, int):
            raise TypeError("width ust be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ width of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ set height of rectangle or set error value """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ width of rectangle """
        return self.__width

    @x.setter
    def x(self, value):
        """ set x of rectangle or set error value """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ width of rectangle """
        return self.__width

    @y.setter
    def y(self, value):
        """ set y of rectangle or set error value """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area of rectagle"""
        return self.__width * self.__height

    def display(self):
        """displays  a rectangle using #"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            for j in range(self.width + self.x):
                if j >= self.x:
                    print("#", end='')
                else:
                    print(" ", end='')
            print()

    def __str__(self):
        """ overwrites the str """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    
    def update(self, *args, **kwargs):
        """ assigns argument to each attribute """
        if args is not None and len(args) != 0:
            for index, value in enumerate(args):
                if index == 0:
                    self.id = value
                elif index == 1:
                    self.width = value
                elif index == 2:
                    self.height = value
                elif index == 3:
                    self.x = value
                elif index == 4:
                    self.y = value
                elif index >= 5:
                    raise Exception("too many arguments")
        else:
            for i in kwargs:
                if i == "id":
                    self.id = kwargs["id"]
                elif i == "width":
                    self.width = kwargs["width"]
                elif i == "height":
                    self.height = kwargs["height"]
                elif i == "x":
                    self.x = kwargs["x"]
                elif i == "y":
                    self.y = kwargs["y"]

                
        """alternative method"""
        """
        a = ["id", "width", "height", "x", "y"]
        if args is not None and len(args) != 0:
            for v in range(len(args)):
                if v > len(a) - 1:
                    break
                setattr(self, a[v]), args[v]

        else:
            for i in kwargs.keys():
                if i in a:
                    setattr(self, i, kwargs[i])
        """
    def to_dictionary(self):
        """returns dict rep of a rectangle"""
        temp = {}
        a = ["id", "width", "height", "x", "y"]
        for i in a:
            temp[i] = getattr(self, i)
        return temp
