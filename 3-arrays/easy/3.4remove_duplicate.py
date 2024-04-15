"""
Problem statement

You are given a sorted integer array 'arr' of size 'n'.
You need to remove the duplicates from the array such that each element appears only once.

Return the length of this new array.

"""


def removeDuplicates(arr,n):
    # my method O(n)
    return len(set(arr))


def removeDuplicates(arr,n):
    #inplace method O(1)
    i = 0
    j = 1
    while i < n :
        if arr[i] == arr[j]:
            arr.remove(arr[i])
            n -= 1
            continue
        j,i =i,i+1
        
    return len(arr)

