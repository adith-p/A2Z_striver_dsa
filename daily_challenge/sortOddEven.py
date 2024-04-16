def sortOddEven(nums: list[int]) -> list[int]:
    """
    Sorts a list of integers, with odd numbers appearing before even numbers.

    Args:
        nums: The list of integers to be sorted.

    Returns:
        A new list with odd numbers followed by even numbers.
    """

    odd = []
    even = []
    arr = []
    for i in nums:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    odd.sort()
    even.sort(reverse=True)
    arr = even + odd
    i = 0
    while i < len(nums):
        nums[i] = arr[i]
        i += 1

    return arr