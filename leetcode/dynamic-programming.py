
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


print(Solution().rob([2,7,9,3,1]))