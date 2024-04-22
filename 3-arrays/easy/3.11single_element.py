""" 
Problem statement
You are given a sorted array 'arr' of positive integers of size 'n'.

It contains each number exactly twice except for one number, which occurs exactly once.

Find the number that occurs exactly once.

Example :
Input: ‘arr’ = {1, 1, 2, 3, 3, 4, 4}.

Output: 2

Explanation: 1, 3, and 4 occur exactly twice. 2 occurs exactly once. Hence the answer is 2.
"""

from typing import *

def getSingleElement(arr : List[int]) -> int:
    
    n = len(arr)-1
    if n == 0:
        return arr[0]

    while n >= 0:

        if arr[n] == arr[n-1]:
            del arr[n],arr[n-1]
            n -= 2
        else:
            n-=1

    # return arr[0]

    # or just use xnor
    """
    XOR of two same numbers is always 0 i.e. a ^ a = 0. ←Property 1.
    XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.  ←Property 2     
    """
    xor = 0
    for val in arr:
        xor ^= val
    return xor
    
    
getSingleElement([1, 1, 2, 3, 3, 4, 4])