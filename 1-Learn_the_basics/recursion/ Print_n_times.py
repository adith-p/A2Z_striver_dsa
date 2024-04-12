""" 
Problem statement
You are given an integer ‘n’.



Print “Coding Ninjas ” ‘n’ times, without using a loop.



Example:
Input: ‘n’  = 4

Output:
Coding Ninjas Coding Ninjas Coding Ninjas Coding Ninjas 

Explanation: “Coding Ninjas” is printed 4 times. 

"""
count = 1
name =[]

def printNtimes(n: int) -> list[str]:
    global count
    global name

    if count > n:
        return name
    name.append( 'Coding Ninjas ')
    count += 1
    return printNtimes(n)