"""
Find_duplicate

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


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_duplicate
    print(find_duplicate([]))
