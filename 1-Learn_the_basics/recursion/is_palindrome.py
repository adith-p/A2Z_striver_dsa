""" 
(Q) Check Palindrome (recursive)

Problem statement

Determine if a given string ‘S’ is a palindrome using recursion. Return a Boolean value of true if it is a palindrome and false if it is not.

Note: You are not required to print anything, just implement the function.

Example:
Input: s = "racecar"
Output: true
Explanation: "racecar" is a palindrome.

"""

def reverse(arr,start,end):
    if start >= end:
        return

    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    
    return reverse(arr, start + 1, end - 1) 
    
def isPalindrome(string: str) -> bool:
    rev_arr = []
    start = 0
    end = len(string) - 1
    
    for c in string:
        rev_arr.append(c)
        
    reverse(rev_arr,start,end)
    
    rev_str = ""
    for i in rev_arr:
        rev_str += i
    
    return rev_str == string

print(isPalindrome('adda'))