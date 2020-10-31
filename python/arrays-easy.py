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
        p_pos = 0
        for i, v in enumerate(A):
            if v >= 0:
                break

            squared = v*v
            for j in range(p_pos, len(A)):
                if A[j] > 0:



arr = [3, 1, 2, 4]
print(ArraysEasy().sortArrayByParity(arr))
