#pattern16
""" 
Problem statement
Sam is curious about Alpha-Ramp, so he decided to create Alpha-Ramp of different sizes.

An Alpha-Ramp is represented by a triangle, where alphabets are filled from the top in order.

For every value of ‘N’, help sam to return the corresponding Alpha-Ramp.

Example:
Input: ‘N’ = 3

Output: 
A
B B
C C C

"""

def alphaRamp(n: int) -> None:
    for letter_num, i in enumerate(range(1,n+1), start=65):
        for _ in range(1,i+1):
            print(chr(letter_num),end=" ")
        print("")
