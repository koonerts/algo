from typing import List

def isBadVersion(n) -> bool:
    return True

class Solution:

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1

        mid = (1+n)//2
        is_mid_bad = isBadVersion(mid)
        is_prev_good = (mid == 1 or not isBadVersion(mid-1))

        while not (is_mid_bad and is_prev_good):
            if is_mid_bad:
                mid = (1+(mid-1))//2
            else:
                mid = ((mid+1)+n)//2

            is_mid_bad = isBadVersion(mid)
            is_prev_good = (mid == 1 or not isBadVersion(mid-1))

        return mid

    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            prev_val = float('-inf') if mid-1 < left else nums[mid-1]
            next_val = float('-inf') if mid+1 > right else nums[mid+1]

            if prev_val < nums[mid] > next_val:
                return mid
            elif nums[mid] > next_val:
                right = mid
            else:
                left = mid + 1

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            pass

print(Solution().findPeakElement([1,2,3,1]))