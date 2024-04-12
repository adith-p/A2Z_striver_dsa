#pattern21


""" 
Problem statement
Ninja has been given a task to print the required star pattern and he asked your help for the same.

You must return an ‘N’*’N’ matrix corresponding to the given star pattern.

Example:
Input: ‘N’ = 4

Output: 

****
*  *
*  *
****

"""

def getStarPattern(n: int) -> None:
    for i in range(n):
        if i in [0,n-1]:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')

