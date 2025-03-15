"""
Three Sum

Given an array of integers, find all unique triplets in the array that give the sum of zero.

Example:
    Input: [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]
    
Time Complexity: O(n²) where n is the length of the array
Space Complexity: O(n) for the result (not counting the input)
"""

from typing import List

def threeSum(nums: list[int]) -> list[list[int]]:
    """
Given an array of integers, find all unique triplets in the array that give the sum of zero.

Args:
    nums (List[int]): Array of integers
    
Returns:
    List[List[int]]: List of triplets that sum to zero
    
Time Complexity: O(n²) where n is the length of the array
Space Complexity: O(n) for the result (not counting the input)
"""
    result = []
    nums.sort()

    i = 0
    while i < len(nums):
    start, end = i + 1, len(nums) - 1

    while start < end:
    val = nums[i] + nums[start] + nums[end]
    if val == 0:
    result.append([nums[i], nums[start], nums[end]])
    start += 1
    end -= 1

    while start < end and nums[start] == nums[start - 1]:
    start += 1
    elif val < 0:
    start += 1
    else:
    end -= 1

    i += 1
    return result




    # Example usage
    if __name__ == "__main__":
    threeSum([-1, 0, 1, 2, -1, -4])  # Output: [[-1, -1, 2], [-1, 0, 1]]
    threeSum([0, 0, 0])  # Output: [[0, 0, 0]]
    threeSum([1, 2, -2, -1])  # Output: []




# Example usage
if __name__ == "__main__":
    threeSum([-1, 0, 1, 2, -1, -4])  # Output: [[-1, -1, 2], [-1, 0, 1]]
    threeSum([0, 0, 0])  # Output: [[0, 0, 0]]
    threeSum([1, 2, -2, -1])  # Output: []
