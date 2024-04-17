def addOneToNumber(arr):
    """
    Adds one to a number represented by a list of digits.

    Args:
        arr (list): A list of digits representing a number.

    Returns:
        list: A list of digits representing the number after adding one.

    Raises:
        No specific exceptions are raised.

    Examples:
        >>> addOneToNumber([1, 2, 3])
        [1, 2, 4]
    """

    digit  = 0

    for i in arr:
        digit += i
        digit *= 10
    
    digit //= 10
    digit += 1
    arr.clear()
    for i in str(digit):
        arr.append(int(i))

    return arr
addOneToNumber([0,2])