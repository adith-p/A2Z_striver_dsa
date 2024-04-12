""" 
Problem statement
You are given an array 'arr' of length 'n' containing integers within the range '1' to 'x'.



Your task is to count the frequency of all elements from 1 to n.

Note:
You do not need to print anything. Return a frequency array as an array in the function such that index 0 represents the frequency of 1, index 1 represents the frequency of 2, and so on.
Example:
Input: ‘n’ = 6 ‘x’ = 9 ‘arr’ = [1, 3, 1, 9, 2, 7]    
Output: [2, 1, 1, 0, 0, 0]
Explanation: Below Table shows the number and their counts, respectively, in the array
"""

# from typing import *

# def count(n:int,m:int,arr):
#     hash_map = {}
    

#     for i in arr:
#         if i in list(hash_map.keys()):
#             hash_map[i] += 1
#             continue
#         hash_map[i] = 1
#     for i in range(1,m+1):
#         if i not in list(hash_map.keys()):
#             hash_map[i] = 0
#             continue
        
#     return hash_map


# def countFrequency(n: int, m: int, edges):
#     hash_map = count(n,m,edges)
#     return [hash_map[i] for i in range(1,m+1)]

        



# print(countFrequency(10, 14, [11, 14, 8, 3, 12, 14, 1, 7, 4, 3 ]))
""" 
from typing import *

def count(n:int,m:int,arr):
    hash_map = {}
    

    for i in arr:
        if i in list(hash_map.keys()):
            hash_map[i] += 1
            continue
        hash_map[i] = 1
    for i in range(1,n+1):
        if i not in list(hash_map.keys()):
            hash_map[i] = 0
            continue
        
    return hash_map


def countFrequency(n: int, m: int, edges):
    hash_map = count(n,m,edges)
    return [hash_map[i] for i in range(1,n+1)]

"""

from collections import defaultdict

def count(n: int, m: int, arr):
    hash_map = defaultdict(int)

    for i in arr:
        hash_map[i] += 1

    return hash_map

def count_all(n: int, m: int, arr):
    hash_map = count(n,m,arr)
    return [hash_map[i] for i in range(1,n+1)]


print(count_all(10, 14, [11, 14, 8, 3, 12, 14, 1, 7, 4, 3 ]))