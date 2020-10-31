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
        p_read = 0
        p_write = len(nums) - 1

        for i in range(len(nums)):
            if nums[i] == 0:
                # shift all elements to the left




l = [0, 1, 0, 3, 12]
ArraysEasy().moveZeroes(l)
print(l)
