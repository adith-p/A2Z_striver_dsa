
# # count = 1
# # l1 = []

# # def printNos(x: int) -> list[int]: 
# #     global count
# #     global l1
# #     if count > x:
# #         return l1
# #     l1.append(count)
# #     count += 1
# #     return printNos(x)

# # print(printNos(1))

# # from  typing import *

# # count = 1
# # name = 'Coding Ninjas '

# # def printNtimes(n: int) -> List[str]:
# #     global count
# #     global name

# #     if count > n:
# #         return name * count
# #     # name += 'Coding Ninjas '
# #     count += 1
# #     return printNtimes(n)

# # print(printNtimes(3))


# def getFactorial(n:int) -> int:
#     if  n == 0:
#         return 1
#     return n * getFactorial(n-1)


# def factorialNumbers(n: int) -> list[int]:
#     fact =  getFactorial(n)
#     print(fact)
    
# factorialNumbers(7)

# def countOf3(x):
#     count = 0
#     for i in range(0,x + 1 ):
#         count = str(i).count("3")
#     return count
# print(countOf3(33))


# arr = [8, 6, 2, 5, 1]

# i = 0

# min = 4
# arr[i],arr[min] = arr[min],arr[i]

# print(arr)