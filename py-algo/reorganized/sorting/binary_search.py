"""
Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

Example:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    
Time Complexity: O(log n) where n is the length of the array
Space Complexity: O(1) as we use constant extra space
"""

from typing import List

def binarySearch(nums: List[int], target: int) -> int:
    """
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

Args:
    nums (List[int]): Sorted array of integers
target (int): Target value to search for
    
Returns:
    int: Index of target if found, otherwise -1
    
Time Complexity: O(log n) where n is the length of the array
Space Complexity: O(1) as we use constant extra space
"""
    if not nums:
    return -1

    left, right = 0, len(nums) - 1

    while left <= right:
    # Calculate middle index (avoiding potential integer overflow)
    mid = left + (right - left) // 2

    # Check if target is present at mid
    if nums[mid] == target:
    return mid

    # If target is greater, ignore left half
    elif nums[mid] < target:
    left = mid + 1

    # If target is smaller, ignore right half
    else:
    right = mid - 1

    # Target is not present in the array
    return -1


    # Example usage
if __name__ == "__main__":
    print(binarySearch([-1, 0, 3, 5, 9, 12], 9))  # Output: 4
    print(binarySearch([-1, 0, 3, 5, 9, 12], 2))  # Output: -1


# Example usage
if __name__ == "__main__":
    binarySearch([-1, 0, 3, 5, 9, 12], 9)  # Output: 4
    binarySearch([-1, 0, 3, 5, 9, 12], 2)  # Output: -1
