#!/usr/bin/python3
"""Json converter"""
import json

def to_json_string(my_obj):
    """returns the JSON representation of an object (string)
    Args:
        my_obj: object
    """
    return json.dumps(my_obj)

