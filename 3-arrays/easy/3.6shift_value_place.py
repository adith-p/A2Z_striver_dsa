""" 
Problem statement
Given an array 'arr' with 'n' elements, the task is to rotate the array to the left by 'k' steps, where 'k' is non-negative.



Example:
'arr '= [1,2,3,4,5]
'k' = 1  rotated array = [2,3,4,5,1]
'k' = 2  rotated array = [3,4,5,1,2]
'k' = 3  rotated array = [4,5,1,2,3] and so on.

https://www.naukri.com/code360/problems/rotate-array_1230543
"""

def rotateArray(arr: list, k: int) -> list:
    temp = []

    for x in arr[:k]:
        temp.append(x)

    del arr[:k]
    
    for y in temp:
        arr.append(y)

    return arr
   

