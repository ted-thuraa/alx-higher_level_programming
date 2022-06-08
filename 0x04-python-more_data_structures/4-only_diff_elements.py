#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    a = {i for i in set_1 if i not in set_2}
    b = {i for i in set_2 if i not in set_1}

    return a.union(b)

""" Alternative method
def only_diff_elements(set_1, set_2):
    return set(list(set_1) + list(set_2)) - (set_1 $ set_2)
"""
