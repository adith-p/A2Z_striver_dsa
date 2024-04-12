"""
Problem statement
Given an array 'arr' of size 'n'.

Return an array with all the elements placed in reverse order.

Note:
You don t need to print anything. Just implement the given function., use recursion 
Example:
Input: n = 6, arr = [5, 7, 8, 1, 6, 3]

Output: [3, 6, 1, 8, 7, 5]

Explanation: After reversing the array, it looks like this [3, 6, 1, 8, 7, 5].
"""

def reverse(arr,start,end):
    if start >= end:
        return
    
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    
    return reverse(arr,start+1,end-1)

def reverseArray(n: int, nums: list[int]) -> list[int]:
    start = 0
    end = n-1
    reverse(nums,start,end)
    return nums

# print(reverseArray(5,[5, 7, 8, 1, 6]))