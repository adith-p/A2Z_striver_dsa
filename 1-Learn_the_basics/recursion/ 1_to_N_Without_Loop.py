""" 
Problem statement
You are given an integer ‘n’.



Your task is to return an array containing integers from 1 to ‘n’ (in increasing order) without using loops.



Example:
Input: ‘n’ = 5

Output: 1 2 3 4 5

Explanation: An array containing integers from ‘1’ to ‘n’ is [1, 2, 3, 4, 5].
"""

count = 1
l1 = []

def printNos(x: int) -> list[int]: 
    global count
    global l1
    if count > x:
        return l1
    l1.append(count)
    count += 1
    return printNos(x)
