#!/usr/bin/python3
""" My func"""

def pascal_triangle(n):
    """returns a list of lists of integers representing the Pascals triangle of n"""
    #base case the first row will have a one
    ans = [[1]]
    #lets build up the other rows. -1 because we already have one row
    for i in range(n-1):
        # rem the algo, assume two 0s at the both ends of the prev array
        temp = [0] + ans[-1] + [0] #this doesnt modify the array
        row = [] #lets build here
        #lets build the next row which is the last row we added in ans and its length will be +1
        for j in range(len(ans[-1]) + 1):
            row.append(temp[j] + temp[j+1]) #add them up
        ans.append(row) #append to the original list
    return ans