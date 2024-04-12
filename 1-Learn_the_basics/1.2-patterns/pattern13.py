#pattern13

#pattern12
""" 
Problem statement
Aryan and his friends are very fond of patterns. For a given integer ‘N’, they want to make the Increasing Number Triangle.

Example:
Input: ‘N’ = 3

Output: 

1
2 3
4 5 6

"""

def nNumberTriangle(n: int) -> None:
    num = 0
    for i in range(1,n+1):
        for _ in range(1,i+1):
            print(num+1,end=" ")
            num += 1
        print("")
            

