"""
Problem statement
You have been given an array ‘a’ of ‘n’ non-negative integers.You have to check whether the given array is sorted in the non-decreasing order or not.

Your task is to return 1 if the given array is sorted. Else, return 0.

Example :
Input: ‘n’ = 5, ‘a’ = [1, 2, 3, 4, 5]
Output: 1

The given array is sorted in non-decreasing order; hence the answer will be 1.

https://www.naukri.com/code360/problems/ninja-and-the-sorted-check_6581957
"""
def isSorted(n: int,  a: list[int]) -> int:
    if sorted(a) == a:
        return 1
    return 0