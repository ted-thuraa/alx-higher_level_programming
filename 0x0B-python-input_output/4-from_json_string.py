#!/usr/bin/python3
"""from JSON string to python obj"""
import json

def from_json_string(my_str):
    """ returns an object (Python data structure) represented by a JSON string
    Args:
        my_str:
    """
    return json.loads(my_str)