from collections import defaultdict
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
                    memo[n] = traverse(n - 1) + traverse(n - 2)
                return memo[n]

        return traverse(n)

    def max_profit_brute_force(self, prices: list[int]) -> int:
        max_profit = 0
        for i, price in enumerate(prices):
            for j in range(i + 1, len(prices)):
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
                    robbed_result = nums[i] + traverse(i - 2)
                    skipped_result = traverse(i - 1)
                    memo[i] = max(robbed_result, skipped_result)
                return memo[i]

        return traverse(len(nums) - 1)

    def canJump(self, nums: list[int]) -> bool:
        if len(nums) <= 1: return True

        target_index = len(nums) - 1
        left_index = len(nums) - 2

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


def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    wordSet = set(wordDict)
    # table to map a string to its corresponding words break
    # {string: [['word1', 'word2'...], ['word3', 'word4', ...]]}
    memo = defaultdict(list)

    # @lru_cache(maxsize=None)    # alternative memoization solution
    def _wordBreak_topdown(s):
        """ return list of word lists """
        if not s:
            return [[]]  # list of empty list

        if s in memo:
            return memo[s]

        for endIndex in range(1, len(s) + 1):
            word = s[:endIndex]
            if word in wordSet:
                # move forwards to break the postfix into words
                for subsentence in _wordBreak_topdown(s[endIndex:]):
                    print(word, subsentence)
                    memo[s].append([word] + subsentence)
        return memo[s]

    # break the input string into lists of words list
    _wordBreak_topdown(s)

    print(memo)
    # chain up the lists of words into sentences.
    return [" ".join(words) for words in memo[s]]


def longestArithSeqLength(A):
    ret = 1

    def maxSeqHelper(d):
        memo, ans = dict(), 1
        for num in A:
            if num - d in memo:
                memo[num] = memo[num - d] + 1
            else:
                memo[num] = 1
            ans = max(ans, memo[num])
        print(memo)
        return ans

    for d in range(-500, 501): ret = max(ret, maxSeqHelper(d))
    return ret


from collections import deque

primes = set()
for a in range(2, 1000):
    if all(a % p != 0 for p in primes):
        primes.add(a)


def split_primes(input_str: str) -> int:

    primes = set()
    for a in range(2, 1000):
        if all(a % p != 0 for p in primes):
            primes.add(a)

    dp = deque([1], maxlen=3)
    for i in range(1, len(input_str) + 1):
        lst = []
        for n, count in zip(range(len(dp), 0, -1), dp):
            if input_str[i - n] != '0' and int(input_str[i - n:i]) in primes:
                lst.append(count)
        dp.append(sum(lst))
    return dp[-1]


def number_of_options(a, b, c, d, target):
    sources = [a, b, c, d]

    @lru_cache(None)
    def dfs(count, i):
        if count > target: return 0

        if i == 4:
            return 1

        return sum([dfs(count + sources[i][j], i + 1) for j in range(len(sources[i]))])

    return dfs(0, 0)


def number_of_options2(a, b, c, d, target):
    sources = [a, b, c, d]
    dp = [[0] * (target + 1) for _ in range(5)]
    dp[4][0] = 1

    for i in range(3, -1, -1):
        for j in range(target + 1)[::-1]:
            if dp[i + 1][j]:
                for v in sources[i]:
                    if j + v <= target:
                        dp[i][v + j] += dp[i + 1][j]

    return sum(dp[0])


print(split_primes("31173"))
