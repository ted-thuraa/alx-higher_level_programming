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

    def to_json(self):
        """retrieves a dictioinary representation of a student instance"""
        return self.__dict__