"""
Number

"""


def missingNumber(nums: list[int]) -> int:
    i = 0
    while i < len(nums):
        while nums[i] < len(nums) and nums[i] != i:
            val = nums[i]
            nums[i], nums[val] = nums[val], nums[i]
        i += 1

    for i in range(len(nums)):
        if nums[i] != i:
            return i
    return len(nums)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to missingNumber
    print(missingNumber([]))
