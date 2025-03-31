"""
Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example:
    Input: coins = [1, 2, 5], amount = 11
    Output: 3 (11 = 5 + 5 + 1)
    
Time Complexity: O(amount * n) where n is the number of coin denominations
Space Complexity: O(amount) for the DP array
"""

from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    """
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Args:
    coins (List[int]): Array of coin denominations
amount (int): Target amount to make
    
Returns:
    int: Fewest number of coins needed or -1 if impossible
    
Time Complexity: O(amount * n) where n is the number of coin denominations
Space Complexity: O(amount) for the DP array
"""
    # Edge cases
    if amount == 0:
    return 0
    if not coins or amount < 0:
    return -1

    # Initialize dp array with amount + 1 (which is greater than any possible solution)
    # dp[i] represents the fewest number of coins needed to make amount i
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0

    # Fill dp array
    for i in range(1, amount + 1):
    for coin in coins:
    if coin <= i:
    dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[amount] is still amount + 1, it means we couldn't make the amount
    return dp[amount] if dp[amount] <= amount else -1


    # Example usage
if __name__ == "__main__":
    coinChange([1, 2, 5], 11)  # Output: 3
    coinChange([2], 3)  # Output: -1
    coinChange([1], 0)  # Output: 0


# Example usage
if __name__ == "__main__":
    coinChange([1, 2, 5], 11)  # Output: 3
    coinChange([2], 3)  # Output: -1
    coinChange([1], 0)  # Output: 0
