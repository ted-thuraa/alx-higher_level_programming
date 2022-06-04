#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    copyof = []
    for i in my_list:
        if i % 2 == 0:
            copyof.append(True)
        else:
            copyof.append(False)
    return copyof
