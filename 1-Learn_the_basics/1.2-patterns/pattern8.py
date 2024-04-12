#pattern8
""" 
Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the Reverse N-Star Triangle.

Example:
Input: ‘N’ = 3

Output: 

*****
 ***
  *
  
"""
def nStarTriangle(n: int) -> None:
    for i in range(n):
        for _ in range(i):
            print(" ",end="")
        
        for _ in range(2*n -( 2*i + 1)):
            print("*" ,end="")
        
        for _ in range(i):
            print(" ",end="")
        print("")
           
