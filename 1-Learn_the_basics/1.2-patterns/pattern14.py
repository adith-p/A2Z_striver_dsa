#pattern14
""" 
Problem statement
Aryan and his friends are very fond of patterns. For a given integer ‘N’, they want to make the Increasing Letter Triangle.

Example:
Input: ‘N’ = 3

Output: 

A
A B
A B C

"""
def nLetterTriangle(n: int) -> None:
    for i in range(1, n + 1):
        for letter, _ in enumerate(range(1, i + 1), start=65):
             print(chr(letter), end=" ")
        print("")
        