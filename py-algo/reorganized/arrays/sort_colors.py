"""
Colors

Do not return anything, modify nums in-place instead.
"""
def sortColors(nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums or len(nums) == 1:
            return

        i, left, right = 0, 0, len(nums) - 1
        while i < right:
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
        print(nums)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to sortColors
    print(sortColors([]))
