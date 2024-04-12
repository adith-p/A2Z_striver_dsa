#pattern7
""" 
Problem statement
Ninja was very fond of patterns. For a given integer ‘N’, he wants to make the N-Star Triangle.

Example:
Input: ‘N’ = 3

Output: 

  *
 ***
*****

"""
def nStarTriangle(n: int) -> None:
    for i in range(n):
        for _ in range(n-i-1):
            print(" ",end="")
        
        # for j in range(0,2*i+1):
        #     print("*" ,end="")
        print("*" * (i + i + 1)) # formula for the GD is derived using the triangle 
        
        for _ in range(n-i-1):
            print(" ",end="")
        print("")