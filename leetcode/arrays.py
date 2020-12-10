from typing import List
from collections import deque

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in reversed(range(len(nums))):
            if i == 0:
                continue

            if nums[i] == nums[i-1]:
                del nums[i]

        return len(nums)


    def moveZeroes(self, nums: List[int]) -> None:
        """
        Given an array nums, write a function to move all 0's to the end of it while
        maintaining the relative order of the non-zero elements.

        Input: [0,1,0,3,12]
        Output: [1,3,12,0,0]
        """
        p_r = 0
        while p_r < len(nums):
            if nums[p_r] == 0 and p_r+1 < len(nums):
                for i in range(p_r+1, len(nums)):
                    if nums[i] != 0:
                        nums[p_r] = nums[i]
                        nums[i] = 0
                        break

            p_r += 1


    def sortArrayByParity(self, A: List[int]) -> List[int]:
        """
        Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
        You may return any answer array that satisfies this condition.

        Input: [3,1,2,4]
        Output: [2,4,3,1]
        The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
        """
        i = 0
        p_even = 0
        while i < len(A):
            if A[i] % 2 == 1:
                for j in range(p_even, len(A)):
                    if A[j] % 2 == 0 and j > i:
                        v = A[j]
                        A[j] = A[i]
                        A[i] = v
                        p_even = j+1
                        break
                    p_even += 1
            i += 1

        return A


    def sortedSquares(self, A: List[int]) -> List[int]:
        """
        Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
        Input: [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
        """

        ret = []
        l, r = 0, 0
        while r < len(A) and A[r] < 0:
            r += 1
        l = r-1

        while len(ret) != len(A):
            if l < 0 or l >= len(A):
                ret.append(A[r] ** 2)
                r += 1
            elif r < 0 or r >= len(A):
                ret.append(A[l] ** 2)
                l -= 1
            else:
                if abs(A[l]) <= abs(A[r]):
                    ret.append(A[l] ** 2)
                    l -= 1
                else:
                    ret.append(A[r] ** 2)
                    r += 1

        return ret


    def heightChecker(self, heights: List[int]) -> int:
        """
        Students are asked to stand in non-decreasing order of heights for an annual photo.
        Return the minimum number of students that must move in order for all students to be standing in non-decreasing order of height.
        Notice that when a group of students is selected they can reorder in any possible way between themselves
        and the non selected students remain on their seats.

        Input: heights = [1,1,4,2,1,3]
        Output: 3

        Input: heights = [5,1,2,3,4]
        Output: 5
        """

        heights_sorted = sorted(heights)
        cnt = 0
        for i in range(len(heights)):
            if heights[i] != heights_sorted[i]:
                cnt += 1
        return cnt


    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

        Input: [1,0,1,1,0]
        Output: 4
        Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
        After flipping, the maximum number of consecutive 1s is 4.
        """
        if not nums or len(nums) == 0:
            return 0

        zero_val_indexes = []
        for i, v in enumerate(nums):
            if v == 0:
                zero_val_indexes.append(i)

        curr_max = len(nums) if len(zero_val_indexes) == 0 else 0
        print(zero_val_indexes)
        for i, v in enumerate(zero_val_indexes):
            start = 0 if i == 0 else zero_val_indexes[i-1]+1
            end = len(nums) if i+1 >= len(zero_val_indexes) else zero_val_indexes[i+1]
            length = len(range(start, end))
            print(start, end, length)
            if length > curr_max:
                curr_max = length
        return curr_max


    def thirdMax(self, nums: List[int]) -> int:
        """
        Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number.
        The time complexity must be in O(n).

        Input: [3, 2, 1]
        Output: 1
        Explanation: The third maximum is 1.

        Input: [2, 2, 3, 1]
        Output: 1
        Explanation: Note that the third maximum here means the third maximum distinct number.
                     Both numbers with value 2 are both considered as second maximum.
        """

        max_set = set()
        max_set.add(nums[0])
        curr_max = nums[0]
        for n in nums:
            if n > curr_max or len(max_set) < 3:
                max_set.add(n)

            if len(max_set) > 3:
                max_set.remove(min(max_set))

        if len(max_set) == 3:
            return min(max_set)
        else:
            return max(max_set)


    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
        Find all the elements of [1, n] inclusive that do not appear in this array.
        Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

        Input: [4,3,2,7,8,2,3,1]
        Output: [5,6]
        """
        for i in range(len(nums)):

            new_index = abs(nums[i])-1
            if nums[new_index] > 0:
                nums[new_index] *= -1

        return [i+1 for i in range(len(nums)) if nums[i] > 0]

    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        elif len(s) == 1: return 1

        start = 0
        curr_substring_len, max_substr_len = 1, 1
        char_set = {s[0]}

        for i in range(1, len(s)):

            while s[i] in char_set:
                curr_substring_len -= 1
                char_set.remove(s[start])
                start += 1

            curr_substring_len += 1
            char_set.add(s[i])
            max_substr_len = max(max_substr_len, curr_substring_len)
        return max_substr_len

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        """
        https://leetcode.com/problems/median-of-two-sorted-arrays/
        """
        # TODO: Come back to

    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        return xor

    def rotate_with_extra_space(self, nums: List[int], k: int) -> None:
        if not nums: return nums
        k = k % len(nums)
        nums_copy = nums[-k:] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = nums_copy[i]

    # def rotate_in_place(self, nums: List[int], k: int) -> None:
    #     if not nums: return nums
    #     k = k % len(nums)
    #
    #     temp, cnt, i = -1, 0, 0
    #     while cnt < len(nums):

    def containsDuplicate(self, nums: List[int]) -> bool:
        set_ = set()
        for num in nums:
            if num in set_:
                return False
            else:
                set_.add(num)
        return True

    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] + 1 <= 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
        return digits

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            if num_map.get(target-num):
                return [i, num_map.get(target-num)]
            else:
                num_map[num] = i
        return []