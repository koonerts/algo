"""
Find_all_duplicates

We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
    The array has some numbers appearing twice, find all these duplicate numbers without using any extra space.

    Example 1:
    Input: [3, 4, 4, 5, 5]
    Output: [4, 5]

    Example 2:
    Input: [5, 4, 7, 2, 3, 5, 3]
    Output: [3, 5]
"""


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


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_all_duplicates
    print(find_all_duplicates([]))
