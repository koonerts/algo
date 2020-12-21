from collections import deque

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        https://leetcode.com/problems/decode-ways/
        """
        if not s or not int(s): return 0
        elif len(s) == 1: return 1


def increment(y):
    if y == 0:
        return 1
    else:
        if y % 2 == 1:
            return 2 * increment(y / 2)
        else:
            return y + 1


print(increment(2))