""" 
Problem statement
Given two sorted arrays, ‘a’ and ‘b’, of size ‘n’ and ‘m’, respectively, return the union of the arrays.



The union of two sorted arrays can be defined as an array consisting of the common and the distinct elements of the two arrays. The final array should be sorted in ascending order.



Note: 'a' and 'b' may contain duplicate elements, but the union array must contain unique elements.



Example:
Input: ‘n’ = 5 ‘m’ = 3
‘a’ = [1, 2, 3, 4, 6]
‘b’ = [2, 3, 5]

Output: [1, 2, 3, 4, 5, 6]

https://www.naukri.com/code360/problems/sorted-array_6613259

"""

def sortedArray(a: list[int], b: list[int]) -> list[int]:
    
    result = []
    
    for i in a:
        if i not in result:
            result.append(i)

    for i in b:
        if i not in result:
            result.append(i)
    
    result.sort()
    return result

print(sortedArray( [1, 2, 3, 4, 6],[2, 3, 5]))
    
        
