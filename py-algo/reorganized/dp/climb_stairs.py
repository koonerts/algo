"""
Climbing Stairs

You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
    Input: n = 3
    Output: 3 (There are three ways: 1+1+1, 1+2, 2+1)

Time Complexity: O(n) where n is the number of steps
Space Complexity: O(1) using constant extra space
"""


def climbStairs(n: int) -> int:
    """
    You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Args:
        n (int): Number of steps

    Returns:
        int: Number of distinct ways to climb to the top

    Time Complexity: O(n) where n is the number of steps
    Space Complexity: O(1) using constant extra space
    """
    memo = {}

    # Example usage


if __name__ == "__main__":
    climbStairs(2)  # Output: 2
    climbStairs(3)  # Output: 3
    climbStairs(5)  # Output: 8


# Example usage
if __name__ == "__main__":
    climbStairs(2)  # Output: 2
    climbStairs(3)  # Output: 3
    climbStairs(5)  # Output: 8
