"""
Peak Element

"""


def findPeakElement(nums: list[int]) -> int:
    if len(nums) == 1:
        return 0

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        prev_val = float("-inf") if mid - 1 < left else nums[mid - 1]
        next_val = float("-inf") if mid + 1 > right else nums[mid + 1]

        if prev_val < nums[mid] > next_val:
            return mid
        elif nums[mid] > next_val:
            right = mid
        else:
            left = mid + 1


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to findPeakElement
    print(findPeakElement([]))
