"""
Problem statement
Given an array ‘arr’ of size ‘n’ find the largest element in the array.



Example:

Input: 'n' = 5, 'arr' = [1, 2, 3, 4, 5]

Output: 5

Explanation: From the array {1, 2, 3, 4, 5}, the largest element is 5.

https://www.naukri.com/code360/problems/largest-element-in-the-array-largest-element-in-the-array_5026279

"""

# using in-bulid method 
def largestElement(arr: list[int], n: int) -> int:
    
    return sorted(arr)[len(arr)-1]
