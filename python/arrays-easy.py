from typing import List


class ArraysEasy:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in reversed(range(len(nums))):
            if i == 0:
                continue

            if nums[i] == nums[i - 1]:
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
            if nums[p_r] == 0 and p_r + 1 < len(nums):
                for i in range(p_r + 1, len(nums)):
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
                        p_even = j + 1
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
        l = r - 1

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
            start = 0 if i == 0 else zero_val_indexes[i - 1] + 1
            end = len(nums) if i + 1 >= len(zero_val_indexes) else zero_val_indexes[i + 1]
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

        curr_max = nums[0]
        curr_third = nums[0]
        prev_third = nums[0]
        rank = 1

        for i, v in enumerate(nums):
            if rank < 3:
                if v > curr_max:
                    curr_max = v
                    rank += 1
            else
                if




arr = [2, 2, 3, 1]
print(ArraysEasy().thirdMax(arr))
