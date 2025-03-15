"""
Duplicates

"""
def removeDuplicates(nums: list[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return 1

        s, i = 0, 1
        while i < len(nums):
            if nums[s] == nums[i]:
                i += 1
            else:
                nums[s + 1] = nums[i]
                i += 1
                s += 1
        return s + 1


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to removeDuplicates
    print(removeDuplicates([]))
