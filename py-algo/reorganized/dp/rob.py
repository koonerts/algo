"""
House Robber

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example:
    Input: [1, 2, 3, 1]
    Output: 4 (Rob house 1 (1) and then rob house 3 (3). 1 + 3 = 4.)

Time Complexity: O(n) where n is the number of houses
Space Complexity: O(1) as we only use a constant amount of extra space
"""

from typing import List


def rob(nums: List[int]) -> int:
    """
    Calculate the maximum amount of money that can be robbed from houses,
    without robbing adjacent houses.

    This is a classic dynamic programming problem where we can use either a bottom-up
    or a top-down approach. This implementation uses a bottom-up approach with
    constant space.

    Args:
        nums (List[int]): Array of money in each house

    Returns:
        int: Maximum amount of money that can be robbed

    Time Complexity: O(n) where n is the number of houses
    Space Complexity: O(1) as we only use a constant amount of extra space
    """
    # Handle edge cases
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    # We only need to keep track of two values: the maximum money we can rob
    # if we consider all houses up to the previous one, and the maximum money
    # we can rob if we consider all houses up to the one before the previous one.
    prev1 = nums[0]  # Max money after considering house 0
    prev2 = 0  # Max money with no houses

    # For each house, we have two options:
    # 1. Rob the current house + max money from houses [0...i-2]
    # 2. Skip the current house + max money from houses [0...i-1]
    for i in range(1, len(nums)):
        # Save current max before updating prev1
        current = max(prev1, prev2 + nums[i])

        # Update prev2 and prev1 for the next iteration
        prev2 = prev1
        prev1 = current

    return prev1


# Example usage
if __name__ == "__main__":
    print(rob([1, 2, 3, 1]))  # Output: 4
    print(rob([2, 7, 9, 3, 1]))  # Output: 12
    print(rob([]))  # Output: 0
