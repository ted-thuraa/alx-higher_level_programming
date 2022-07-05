#!/usr/bin/python3
"""Appends stuff"""
def append_write(filename="", text=""):
    """ appends a string to the end of a text file
    Args:
        filename: name of file
        text: text to append
        return: no of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        chars = 0
        for w in test:
            myFile.write(w)
            chars += 1
        return chars