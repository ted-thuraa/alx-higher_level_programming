#!/usr/bin/python3
""" prints My name is <first name> <last name>
"""

def say_my_name(first_name, last_name=""):
    """ prints out My name is <first name> <last name>

    Args:
        first_name: first name
        last_name: last name

    Return: returns a string or typeerror
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
