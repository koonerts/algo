from functools import lru_cache
from typing import List

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def traverse(n):
            if n <= 2:
                return n
            else:
                if n not in memo:
                    memo[n] = traverse(n-1) + traverse(n-2)
                return memo[n]
        return traverse(n)

    def max_profit_brute_force(self, prices: list[int]) -> int:
        max_profit = 0
        for i, price in enumerate(prices):
            for j in range(i+1, len(prices)):
                if prices[j] - price > max_profit:
                    max_profit = prices[j] - price
        return max_profit

    def rob(self, nums: list[int]) -> int:
        memo = {}

        def traverse(i):
            if i < 0:
                return 0
            else:
                if i not in memo:
                    robbed_result = nums[i] + traverse(i-2)
                    skipped_result = traverse(i-1)
                    memo[i] = max(robbed_result, skipped_result)
                return memo[i]
        return traverse(len(nums)-1)

    def canJump(self, nums: list[int]) -> bool:
        if len(nums) <= 1: return True

        target_index = len(nums)-1
        left_index = len(nums)-2

        while left_index >= 0:
            dist = target_index - left_index
            if nums[left_index] >= dist:
                target_index = left_index
            left_index -= 1
        return target_index == 0

    def uniquePaths(self, m: int, n: int) -> int:
        pathCnt = 0

        def traverse(x, y):
            nonlocal pathCnt

    def coinChange(self, coins: list[int], amount: int) -> int:
        if not coins or amount <= 0: return -1

    def longestPalindrome(self, s: str) -> str:
        pass


def number_of_options(prices_of_jeans: List[int], prices_of_shoes: List[int], prices_of_skirts: List[int], prices_of_tops: List[int], budget: int) -> int:
    all_prices = [prices_of_jeans, prices_of_shoes, prices_of_skirts, prices_of_tops]
    n = len(all_prices)
    for prices in all_prices:
        prices.sort()
    # cost of (lowest, highest) combination
    ranges = [(0, 0)]
    # number of all combinations, ignoring budget
    combs = [1]
    for prices in all_prices:
        low, high = ranges[-1]
        ranges.append((prices[0] + low, prices[-1] + high))
        combs.append(len(prices) * combs[-1])

    print(ranges)
    print(combs)
    @lru_cache(None)
    def search(item: int, budget: int) -> int:
        prices = all_prices[item - 1]
        low, high = ranges[item - 1]
        ways = 0
        for price in prices:
            left = budget - price
            # extreme case optimization
            if left < low:
                # not enough for cheapest combination, so 0 options;
                # same for higher `price`, so break
                break
            if left >= high:
                # enough for all combinations
                ways += combs[item - 1]
                continue
            # persistent scan optimization

            ways += search(item - 1, left)
        return ways
    return search(n, budget)


print(number_of_options([2,3], [4], [2,3], [1,2], 10))