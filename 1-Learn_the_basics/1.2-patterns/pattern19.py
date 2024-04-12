#pattern19
""" 
Problem statement
Sam is curious about symmetric patterns, so he decided to create one.

For every value of ‘N’, return the symmetry as shown in the example.

Example:
Input: ‘N’ = 3

Output:  #2*i - 2
* * * * * *  
* *     * * 
*         * 
*         * 
* *     * * 
* * * * * * 

"""
def symmetry(n: int):
        
    for i in range(n,0,-1):
        for _ in range(1,i+1):
            print('* ' ,end="")
     
        for _ in range(2*(n-i)):
            print(" ",end=" ")
        
        for _ in range(1,i+1):
            print('* ' ,end="")
        print("")
    for i in range(1,n+1):
        for _ in range(1,i+1):
            print('* ' ,end="")
            
        for _ in range(2*n - 2,0,-1):
            print(" ",end=" ")
        n -= 1
        
        for _ in range(i,0,-1):
            print('* ' ,end="")
        print("")    
