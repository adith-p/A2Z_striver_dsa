"""
Problem statement
You have been given an array ‘a’ of ‘n’ unique non-negative integers.



Find the second largest and second smallest element from the array.



Return the two elements (second largest and second smallest) as another array of size 2.



Example :
Input: ‘n’ = 5, ‘a’ = [1, 2, 3, 4, 5]
Output: [4, 2]

The second largest element after 5 is 4, and the second smallest element after 1 is 2.

"""

def getSecondOrderElements(n: int,  a: list[int]) -> list[int]:
    a.sort()
    return [a[1],a[0]] if n == 2 else [a[n-2],a[1]]
