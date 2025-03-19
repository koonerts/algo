"""
Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example:
    Input: [7, 1, 5, 3, 6, 4]
    Output: 5 (buy on day 2 when price = 1, sell on day 5 when price = 6, profit = 6-1 = 5)

Time Complexity: O(n) where n is the number of days
Space Complexity: O(1) using constant extra space
"""

from typing import List

def maxProfit(prices: list[int]) -> int:
    """
You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Args:
    prices (List[int]): Array of prices where prices[i] is the price on day i

Returns:
    int: The maximum profit that can be achieved

Time Complexity: O(n) where n is the number of days
Space Complexity: O(1) using constant extra space
"""
    if len(prices) == 1: return 0

    profit = 0
    peak, valley = 0, 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            peak = i
            if i == len(prices) - 1:
                profit += prices[peak] - prices[valley]
        else:
            if peak > valley:
                profit += prices[peak] - prices[valley]
            valley = i
    return profit


# Example usage
if __name__ == "__main__":
    maxProfit([7, 1, 5, 3, 6, 4])  # Output: 5
    maxProfit([7, 6, 4, 3, 1])  # Output: 0
