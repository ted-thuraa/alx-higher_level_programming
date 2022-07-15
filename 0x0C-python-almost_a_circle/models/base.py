#!/usr/bin/python3
"""Base class"""
import json

class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiator"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        string = []
        if list_dictionaries None or list_dictionaries == "[]" or len(list_dictionaries) == 0:
            return string
        else:
            return json.dumps(list_dictionaries)


    @classmethod
    def save_to_file(cls, list_objs):
        """writes/saves the json string rep of list_objs to a file"""
        string = []
        if list_objs is None or len(list_objs) == 0:
            with open("{}.json".format(cls.__name__), mode="w", encoding="utf-8") as mfile:
                mfile.write(cls.to_json_string(string))
        else:
            for i in list_objs:
                string.append(i.to_dictionary())
            string = cls.to_json_string(string)
        with open("{}.json".format(cls.__name__), mode="w", encoding="utf-8") as mfile:
                mfile.write(string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            temp = cls(width=2, height=3)
        if cls.__name__ == "Square":
            temp = cls(size=2)
        temp.update(**dictionary)
        return temp

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        temp = []
        try:
            with open("{}.json".format(cls.__name__), mode="r", encoding="utf-8") as file:
                a = cls.from_json_string(file.read())
            for i in a:
                temp.append(cls.create(**i))
            return temp
        except FileNotFoundError:
            return temp