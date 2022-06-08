#!/usr/bin/python3
def common_elements(set_1, set_2):
    return {i for i in set_1 if i in set_2}


""" This also works
def common_elements(set_1, set_2):
    return (set_1.intersection(set_2))
"""

