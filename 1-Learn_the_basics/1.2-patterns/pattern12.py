#pattern12

""" 
Problem statement
Aryan and his friends are very fond of the pattern. They want to make the Reverse N-Number Crown for a given integer' N'.

Given 'N', print the corresponding pattern.

Example:
Input: ‘N’ = 3

Output: 

1         1 #4
1 2     2 1 #2
1 2 3 3 2 1 #0

Sample Input 2 :
4

Sample Output 2 :
1             1 #6   
1 2         2 1 #4
1 2 3     3 2 1 #2
1 2 3 4 4 3 2 1 #0


GD = 2r - 2
"""
def numberCrown(n: int) -> None:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(f'{j} ' ,end="")
            
        for _ in range(2*n - 2,0,-1):
            print(" ",end=" ")
        n -= 1
        
        for j in range(i,0,-1):
            print(f'{j} ' ,end="")
        print("")


numberCrown(3)