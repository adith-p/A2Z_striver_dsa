""" 
Problem statement
Sort the given unsorted array 'arr' of size 'N' in non-decreasing order using the selection sort algorithm.



 Note:
Change in the input array/list itself. 


Example:
Input:
N = 5
arr = {8, 6, 2, 5, 1}

Output:
1 2 5 6 8 

"""
from typing import List

def selectionSort(arr: List[int]) -> None: 
    l = len(arr) #5
    min = 0
    j = 1 
    for i in range(l): 
        while j < l:
            if arr[j] < arr[min]: 
                min = j 
                j += 1
                continue
            if arr[j] > arr[min]: 
                j += 1
        
        arr[i],arr[min] = arr[min],arr[i]
        min = i + 1
        j = min + 1 


    return arr

print(selectionSort([8, 6, 2, 5, 1]))