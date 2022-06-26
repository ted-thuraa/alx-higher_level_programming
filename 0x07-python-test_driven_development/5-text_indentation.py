#!/usr/bin/python3
""" main indents text
"""

def text_indentation(text):
    """ After each . ? and : print 2 new lines

    Args:
        text: the wall of text that we are given

    Return: noting
    """
    if type(text) is str:
        text = text.strip()
        if len(text) == 0:
            return
        temp = text[0]
        delim = ['.', '?', ':']
        for char in text:
            if char == ' ' and temp in delim:
                continue
            temp = char
            print(char, end='')
            if char in delim:
                print()
                print()
    else:
        raise TypeError("text must be a string")
