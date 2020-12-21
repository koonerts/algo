from typing import List
from heapq import *

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
        found_index = self.binarySearch(nums, 0, len(nums)-1, target)
        if found_index == -1:
            return [-1,-1]

        lower_bound, upper_bound = found_index, found_index
        ret_list = [found_index, found_index]
        while lower_bound >= 1 or 0 <= upper_bound < len(nums)-1:
            if lower_bound - 1 >= 0:
                lower_bound = self.binarySearch(nums, 0, lower_bound-1, target)
                if lower_bound >= 0:
                    ret_list[0] = lower_bound

            if 0 <= upper_bound + 1 < len(nums):
                upper_bound = self.binarySearch(nums, upper_bound+1, len(nums)-1, target)
                if upper_bound >= 0:
                    ret_list[1] = upper_bound
        return ret_list

    def binarySearch(self, arr: List[int], left:int, right:int, target: int) -> int:
        if not arr: return -1

        while left <= right:
            mid = (left+right)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return -1

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals: return []

        start, end = 0, 1
        result = []
        prev = None

        intervals.sort(key=lambda x:x[0])
        for curr in intervals:
            if not prev:
                prev = curr
                result.append(curr)
            else:
                if prev[end] < curr[start]:
                    prev = curr
                    result.append(curr)
                elif prev[end] >= curr[end]:
                    continue
                elif curr[start] <= prev[end] <= curr[end]:
                    prev[end] = curr[end]
        return result

    def binary_search_rotated(self, nums: List[int], target: int) -> int:
        # if not nums: return -1
        #
        # def is_ascending(curr_index):
        #     lower = curr_index if curr_index == 0 else curr_index-1
        #     upper = curr_index if curr_index == len(nums)-1 else curr_index+1
        #     return nums[lower] <= nums[curr_index] <= upper[curr_index]
        #
        # direction, start, end = -1, 0, len(nums) - 1
        # while start <= end:
        #     mid = (start+end)//2
        #     if nums[mid] == target:
        #         return mid
        #     elif nums[start] <= nums[mid] <= nums[end]:
        #
        pass

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        elif len(intervals) == 1: return 1

        start, end = 0, 1
        intervals.sort(key=lambda x:x[start])
        min_end, max_concurrent_meetings, curr_concurrent_meetings = [], 0, 0

        for curr_interval in intervals:
            while min_end and curr_interval[start] >= min_end[0]:
                heappop(min_end)
                curr_concurrent_meetings -= 1

            heappush(min_end, curr_interval[end])
            curr_concurrent_meetings += 1
            max_concurrent_meetings = max(max_concurrent_meetings, curr_concurrent_meetings)
        return max_concurrent_meetings

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return -1

        rows, cols = len(matrix), len(matrix[0])




print(Solution().minMeetingRooms([[0, 30],[5, 10],[15, 20]]))