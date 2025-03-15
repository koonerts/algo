"""
Binary_search_rotated

"""


def binary_search_rotated(nums: list[int], target: int) -> int:
    if not nums:
        return -1

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


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to binary_search_rotated
    print(binary_search_rotated([]))
