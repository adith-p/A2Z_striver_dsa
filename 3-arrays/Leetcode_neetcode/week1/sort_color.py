""" 
75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

 

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 
"""

def sortColors(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """ 
    count_0 = 0
    count_1 = 0
    count_2 = 0

    for val in nums:
        if val == 0:
            count_0 += 1
        elif val == 1:
            count_1 += 1
        else:
            count_2 += 1

    for i in range(len(nums)):
        if i < count_0:
            nums[i] = 0
            continue
        if i in range(count_0,count_0 + count_1):
            nums[i] = 1
            continue
        nums[i] = 2
        
 
            


        