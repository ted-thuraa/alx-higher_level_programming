#!/usr/bin/python3
"""My student module"""


class Student():
    """ My class
    """
    def __init__(self, first_name, last_name, age):
        """ instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictioinary representation of a student instance"""
        if attrs is None:
            return self.__dict__
        temp = {}
        for i in attrs:
            if i is "first_name":
                temp[i] = self.first_name
            elif i is "last_name":
                temp[i] = self.last_name
            elif i is "age":
                temp[i] = self.age
            else:
                pass
            return temp

            """ orrr
            if attrs is None:
                return self.__dict__
            temp = self.__dict__.keys()
            new = {}
            for i in attrs:
                if type(i) != str:
                    return self.__dict__
                if i in temp:
                new.update({i: self.__dict__[i]})
            return new
