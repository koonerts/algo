
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


print(Solution().canJump([2,3,1,1,4]))