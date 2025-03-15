"""
Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1] (because nums[0] + nums[1] = 2 + 7 = 9)

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(n) for the hash table
"""

from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Args:
        nums (List[int]): Array of integers
        target (int): Target sum

    Returns:
        List[int]: Indices of the two numbers that add up to target

    Time Complexity: O(n) where n is the length of the array
    Space Complexity: O(n) for the hash table
    """
    num_map = {}
    for i, num in enumerate(nums):
        if target - num in num_map:
            return [i, num_map[target - num]]
        num_map[num] = i
    return []


# Example usage
if __name__ == "__main__":
    print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]
    print(twoSum([3, 2, 4], 6))  # Output: [1, 2]
    print(twoSum([3, 3], 6))  # Output: [0, 1]
