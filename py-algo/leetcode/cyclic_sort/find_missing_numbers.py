"""
Find_missing_numbers

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


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_missing_numbers
    print(find_missing_numbers([]))
