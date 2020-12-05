from collections import deque

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        https://leetcode.com/problems/decode-ways/
        """
        if not s or not int(s): return 0
        elif len(s) == 1: return 1





