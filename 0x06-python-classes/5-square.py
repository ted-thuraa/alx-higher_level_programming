class Square:
    def __init__(self, size=0):
        self.size = size

    def area(self):
         return self.__size * self.__size

    @property
    def size(self):
         return self.__size

    @size.setter
    def size(self, value):
         if type(value) is not int:
             raise TypeError("size must be an integer")
         elif value < 0:
             raise ValueError("size must be >= 0")
         self.__size = value
    def my_print(self):
        if self.size is 0:
            print()
        for i in range(self.size):
            for j in range(self.size):
                print("#", end='')
            print()
