#!/usr/bin/python3
"""My dunc
"""

def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascal’s triangle of n"""
    ans = [[1]] # our first base row will have a one

    #lets build the rest of rows
    for i in range(n - 1):
        # a rep of our previos row with two assumed 0s at both ends
        #this doesnt change anything just temporary
        temp = [0] + ans[-1] + [0]
        row = []
        #Next row will be len of previous + 1
        for j in range(len(ans[-1] - 1) + 1):
            #add them up ie prev and next
            row.append(temp[j] + temp[j + 1])
        #append them to the main list
        ans.append(row)
    return ans