#!/usr/bin/python3
"""entry"""
def write_file(filename="", text=""):
    """writes to a file
    Args:
        filename: name of the file
        text: text to be written
        Return: No of characters written
    """
    with open(filename, mode="w", encoding="utf-8") as myFile:
        chars = 0
        for w in text:
            myFile.write(w)
            chars += 1
        return chars