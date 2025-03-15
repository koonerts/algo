"""
Rotate_with_extra_space

"""
def rotate_with_extra_space(nums: list[int], k: int) -> None:
        if not nums: return nums
        k = k % len(nums)
        nums_copy = nums[-k:] + nums[:-k]
        for i in range(len(nums)):
            nums[i] = nums_copy[i]

        # def rotate_in_place(self, nums: list[int], k: int) -> None:
        #     if not nums: return nums
        #     k = k % len(nums)
        #
        #     temp, cnt, i = -1, 0, 0
        #     while cnt < len(nums):


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to rotate_with_extra_space
    print(rotate_with_extra_space([]))
