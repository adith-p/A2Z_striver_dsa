"""
Problem statement
Given an integer ‘n’, return first n Fibonacci numbers using a generator function.



Example:
Input: ‘n’ = 5

Output: 0 1 1 2 3

Explanation: First 5 Fibonacci numbers are: 0, 1, 1, 2, and 3.
Note:
You don't need to print anything. Just implement the given function.
"""

from typing import List

def generateFibonacciNumbers(n: int) -> List[int]: 
    if n == 1:
        return [0]
    if n == 2:
        return [0,1]
    
    arr = generateFibonacciNumbers(n-1)
    arr.append(arr[-1]+arr[-2])
    return arr


print(generateFibonacciNumbers(5))