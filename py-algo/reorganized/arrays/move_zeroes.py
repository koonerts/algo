"""
Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
    Input: [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) as we modify the array in-place
"""

from typing import List


def moveZeroes(nums: list[int]) -> None:
    """
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Args:
        nums (List[int]): Array of integers

    Returns:
        None: The array is modified in-place

    Time Complexity: O(n) where n is the length of the array
    Space Complexity: O(1) as we modify the array in-place
    """
    if len(nums) <= 1:
        return

    left, i = 0, 1
    while i < len(nums) and left < len(nums):
        if nums[left] == 0 and nums[i] != 0:
            nums[left], nums[i] = nums[i], nums[left]
            i += 1
            left += 1
        else:
            if nums[left] != 0:
                left += 1
            if i <= left:
                i = left + 1
            elif nums[i] == 0:
                i += 1
    print(nums)


# Example usage
if __name__ == "__main__":
    arr1 = [0, 1, 0, 3, 12]
    moveZeroes(arr1)
    print(arr1)  # Output: [1, 3, 12, 0, 0]
    arr2 = [0, 0, 1]
    moveZeroes(arr2)
    print(arr2)  # Output: [1, 0, 0]
