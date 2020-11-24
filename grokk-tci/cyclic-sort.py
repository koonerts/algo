def cyclic_sort(nums: list[int]) -> list[int]:
    """
    We are given an array containing ‘n’ objects. Each object, when created, was assigned a
    unique number from 1 to ‘n’ based on their creation sequence.

    This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.
    Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space.
    For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

    Example 1:
    Input: [3, 1, 5, 4, 2]
    Output: [1, 2, 3, 4, 5]

    Example 2:
    Input: [2, 6, 4, 3, 1, 5]
    Output: [1, 2, 3, 4, 5, 6]

    Example 3:
    Input: [1, 5, 6, 4, 3, 2]
    Output: [1, 2, 3, 4, 5, 6]
    """
    i = 0
    while i < len(nums):
        if nums[i] == i + 1:
            i += 1
        else:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    return nums


def find_missing_number(nums):
    """
    We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.
    Example 1:
    Input: [4, 0, 3, 1]
    Output: 2

    Example 2:
    Input: [8, 3, 5, 2, 4, 6, 0, 1]
    Output: 7
    """
    n_index, i = -1, 0
    while i < len(nums):
        if nums[i] == len(nums):
            n_index = i
            i += 1
        elif nums[i] == i:
            i += 1
        else:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return n_index


def find_missing_numbers(nums):
    """
    We are given an unsorted array containing numbers taken from the range 1 to ‘n’.
    The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

    Example 1:
    Input: [2, 3, 1, 8, 2, 3, 5, 1]
    Output: 4, 6, 7
    Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

    Example 2:
    Input: [2, 4, 1, 2]
    Output: 3

    Example 3:
    Input: [2, 3, 2, 1]
    Output: 4
    """
    i = 0
    missing_nums = []
    while i < len(nums):
        val = nums[i]

        # if in correct position or if the swap index is already correct: increment
        if val == i + 1 or nums[val - 1] == val:
            i += 1
        else:
            nums[val - 1], nums[i] = nums[i], nums[val - 1]

    for i, num in enumerate(nums):
        if i + 1 != num:
            missing_nums.append(i + 1)

    return missing_nums


def find_duplicate(nums):
    """
    We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
    The array has only one duplicate but it can be repeated multiple times.
    Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

    Example 1:
    Input: [1, 4, 4, 3, 2]
    Output: 4

    Example 2:
    Input: [2, 1, 3, 3, 5, 4]
    Output: 3

    Example 3:
    Input: [2, 4, 1, 4, 4]
    Output: 4
    """
    i = 0
    while i < len(nums):
        if nums[i] == i + 1:
            i += 1
        elif nums[i] == nums[nums[i] - 1]:
            return nums[i]
        else:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]


def find_all_duplicates(nums):
    """
    We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
    The array has some numbers appearing twice, find all these duplicate numbers without using any extra space.

    Example 1:
    Input: [3, 4, 4, 5, 5]
    Output: [4, 5]

    Example 2:
    Input: [5, 4, 7, 2, 3, 5, 3]
    Output: [3, 5]
    """
    duplicate_numbers = []
    i = 0

    while i < len(nums):
        val = nums[i]

        # if in correct position or if the swap index is already correct: increment
        if val == i + 1 or nums[val - 1] == val:
            i += 1
        else:
            nums[val - 1], nums[i] = nums[i], nums[val - 1]

    for i, num in enumerate(nums):
        if i + 1 != num:
            duplicate_numbers.append(num)

    return duplicate_numbers


def find_corrupt_numbers(nums):
    """
    We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
    The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the
    numbers got duplicated which also resulted in one number going missing.
    Find both these numbers.

    Example 1:
    Input: [3, 1, 2, 5, 2]
    Output: [2, 4]
    Explanation: '2' is duplicated and '4' is missing.

    Example 2:
    Input: [3, 1, 2, 3, 6, 4]
    Output: [3, 5]
    Explanation: '3' is duplicated and '5' is missing.
    """
    i = 0
    return_list = []
    while i < len(nums):
        if nums[i] == i + 1 or nums[i] == nums[nums[i] - 1]:
            i += 1
        else:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i, num in enumerate(nums):
        if i + 1 != num:
            return_list.append(num)
            return_list.append(i + 1)

    return return_list


def find_first_missing_positive(nums):
    """
    Given an unsorted array containing numbers, find the smallest missing positive number in it.

    Example 1:
    Input: [-3, 1, 5, 4, 2]
    Output: 3
    Explanation: The smallest missing positive number is '3'

    Example 2:
    Input: [3, -2, 0, 1, 2]
    Output: 4

    Example 3:
    Input: [3, 2, 5, 1]
    Output: 4
    """


print(find_corrupt_numbers([3, 1, 2, 5, 2]))
