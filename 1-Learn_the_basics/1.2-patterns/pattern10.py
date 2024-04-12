#pattern10
"""
Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Rotated Triangle.

Example:
Input: ‘N’ = 3

Output: 

*
**
***
**
*

"""
def nStarTriangle(n: int) -> None:
    for i in range(1,n+1):
        for _ in range(i):
            print("*" ,end="")

        for _ in range(n-i):
            print(" ",end="")
        
        print("")
        
    for i in range(n-1,0,-1):
        for _ in range(i):
            print("*" ,end="")

        for _ in range(n+i):
            print(" ",end="")
        
        print("")
    