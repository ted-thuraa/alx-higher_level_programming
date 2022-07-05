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

    def reload_from_json(self, json):
        """replaces all attr of student with json stuff"""
        for i in json:
            self.__dict__[i] = json[i]