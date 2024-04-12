""" 
Problem statement
You are given an integer array 'arr' of size 'N'.



You must sort this array using 'Bubble Sort'.



Note:
Change in the input array itself. You don't need to return or print the elements.
Example:
Input: ‘N’ = 7
'arr' = [2, 13, 4, 1, 3, 6, 28]

Output: [1 2 3 4 6 13 28]

"""



from typing import List

def bubbleSort(arr: List[int], n: int):
    
    # This is not a efficent method since while loop is used !
    
    
    while n != 0:
        for i in range(len(arr)):
            if i + 1 < len(arr) and arr[i] > arr[i+1]:
                    arr[i],arr[i+1] = arr[i+1],arr[i]
                    
        n -= 1 
            

    return arr
