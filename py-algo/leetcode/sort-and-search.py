from heapq import *
import math


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

        mid = (1 + n) // 2
        is_mid_bad = isBadVersion(mid)
        is_prev_good = (mid == 1 or not isBadVersion(mid - 1))

        while not (is_mid_bad and is_prev_good):
            if is_mid_bad:
                mid = (1 + (mid - 1)) // 2
            else:
                mid = ((mid + 1) + n) // 2

            is_mid_bad = isBadVersion(mid)
            is_prev_good = (mid == 1 or not isBadVersion(mid - 1))

        return mid

    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1: return 0

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            prev_val = float('-inf') if mid - 1 < left else nums[mid - 1]
            next_val = float('-inf') if mid + 1 > right else nums[mid + 1]

            if prev_val < nums[mid] > next_val:
                return mid
            elif nums[mid] > next_val:
                right = mid
            else:
                left = mid + 1

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        found_index = self.binarySearch(nums, 0, len(nums) - 1, target)
        if found_index == -1:
            return [-1, -1]

        lower_bound, upper_bound = found_index, found_index
        ret_list = [found_index, found_index]
        while lower_bound >= 1 or 0 <= upper_bound < len(nums) - 1:
            if lower_bound - 1 >= 0:
                lower_bound = self.binarySearch(nums, 0, lower_bound - 1, target)
                if lower_bound >= 0:
                    ret_list[0] = lower_bound

            if 0 <= upper_bound + 1 < len(nums):
                upper_bound = self.binarySearch(nums, upper_bound + 1, len(nums) - 1, target)
                if upper_bound >= 0:
                    ret_list[1] = upper_bound
        return ret_list

    def binarySearch(self, arr: list[int], left: int, right: int, target: int) -> int:
        if not arr: return -1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals:
            return []

        start, end = 0, 1
        intervals.sort(key=lambda x: x[start])

        prev = intervals[0]
        result = [prev]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if prev[end] < curr[start]:
                result.append(curr)
                prev = curr
            else:
                prev[end] = max(prev[end], curr[end])
        return result

    def binary_search_rotated(self, nums: list[int], target: int) -> int:
        if not nums: return -1

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            else:
                # left side sorted
                if nums[start] <= nums[mid]:
                    if nums[start] <= target < nums[mid]:
                        end = mid - 1
                    else:
                        start = mid + 1
                # right side sorted
                else:
                    if nums[mid] < target <= nums[end]:
                        start = mid + 1
                    else:
                        end = mid - 1
        return -1

    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0
        elif len(intervals) == 1:
            return 1

        start, end = 0, 1
        intervals.sort(key=lambda x: x[start])

        max_concurrent_meetings = 0
        min_end_times = []

        for iv in intervals:
            if not min_end_times:
                heappush(min_end_times, iv[end])
            else:
                while min_end_times and min_end_times[0] <= iv[start]:
                    heappop(min_end_times)
                heappush(min_end_times, iv[end])
            max_concurrent_meetings = max(max_concurrent_meetings, len(min_end_times))
        return max_concurrent_meetings

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix: return -1

        rows, cols = len(matrix), len(matrix[0])

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        https://leetcode.com/problems/median-of-two-sorted-arrays/
        """
        len1, len2 = len(nums1), len(nums2)
        if len2 < len1:
            return self.findMedianSortedArrays(nums2, nums1)

        total_len = len1 + len2
        start, end = 0, len1 - 1

        while True:
            p1 = (start + end) // 2
            p2 = ((total_len + 1) // 2) - (p1 + 2)

            n1_p_val = float('-inf') if p1 < 0 else nums1[p1]
            n2_p_val = float('-inf') if p2 < 0 else nums2[p2]
            n1_next_val = float('inf') if p1 + 1 >= len1 else nums1[p1 + 1]
            n2_next_val = float('inf') if p2 + 1 >= len2 else nums2[p2 + 1]

            if n1_p_val <= n2_next_val and n2_p_val <= n1_next_val:
                if total_len % 2 == 1:
                    return max(n1_p_val, n2_p_val)
                else:
                    return (max(n1_p_val, n2_p_val) + min(n1_next_val, n2_next_val)) / 2
            elif n1_p_val > n2_next_val:
                end = p1 - 1
            else:
                start = p1 + 1

    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            val = numbers[start] + numbers[end]
            if val == target:
                return [start + 1, end + 1]
            elif val > target:
                end -= 1
            else:
                start += 1

    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        euclidean_dist = lambda p: math.sqrt(p[0] ** 2 + p[1] ** 2)

        min_heap = []
        for point in points:
            if len(min_heap) < k:
                heappush(min_heap, (-euclidean_dist(point), point))
            else:
                curr_euc_dist = euclidean_dist(point)
                if curr_euc_dist < -min_heap[0][0]:
                    heappushpop(min_heap, (-curr_euc_dist, point))
        return [tup[1] for tup in min_heap]


print(Solution().findMedianSortedArrays([0, 23], []))
