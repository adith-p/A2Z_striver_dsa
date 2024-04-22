""" 
Problem statement
Given an array 'arr' of 'n' non-negative integers, your task is to move all the zeros to the end of the array while keeping the non-zero elements at the start of the array in their original order. Return the modified array.



Example :
Input: ‘n’ = 5, ‘arr’ = [1, 2, 0, 0, 2, 3]
Output: [1, 2, 2, 3, 0, 0]

Explanation: Moved all the 0’s to the end of an array, and the rest of the elements retain the order at the start.

https://www.naukri.com/code360/problems/ninja-and-the-zero-s_6581958
"""

def moveZeros(n: int,  a: list[int]) -> list[int]:

    zero_counter = 0
    i = n-1
    while i >= 0:
        if a[i] == 0:
            del a[i]
            zero_counter += 1
        i -= 1

    for i in range(zero_counter):
        a.append(0)

    return a

print(moveZeros(4,[0,0,0,1]))
