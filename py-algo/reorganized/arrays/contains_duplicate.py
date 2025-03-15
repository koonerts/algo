"""
Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example:
    Input: [1, 2, 3, 1]
    Output: true (because 1 appears twice)
    
Time Complexity: O(n) where n is the length of the array
Space Complexity: O(n) for the hash set
"""

from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    """
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Args:
    nums (List[int]): Array of integers
    
Returns:
    bool: True if the array contains duplicates, False otherwise
    
Time Complexity: O(n) where n is the length of the array
Space Complexity: O(n) for the hash set
"""
    set_ = set()
    for num in nums:
    if num in set_:
    return True
    else:
    set_.add(num)
    return False




    # Example usage
    if __name__ == "__main__":
    containsDuplicate([1, 2, 3, 1])  # Output: True
    containsDuplicate([1, 2, 3, 4])  # Output: False
    containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])  # Output: True




# Example usage
if __name__ == "__main__":
    containsDuplicate([1, 2, 3, 1])  # Output: True
    containsDuplicate([1, 2, 3, 4])  # Output: False
    containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])  # Output: True
