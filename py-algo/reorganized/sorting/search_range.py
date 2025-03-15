"""
Range

"""


def searchRange(nums: list[int], target: int) -> list[int]:
    found_index = self.binarySearch(nums, 0, len(nums) - 1, target)
    if found_index == -1:
        return [-1, -1]

    lower_bound, upper_bound = found_index, found_index
    ret_list = [found_index, found_index]
    while lower_bound >= 1 or 0 <= upper_bound < len(nums) - 1:
        if lower_bound - 1 >= 0:
            lower_bound = self.binarySearch(nums, 0, lower_bound - 1, target)
            if lower_bound >= 0:
                ret_list[0] = lower_bound

        if 0 <= upper_bound + 1 < len(nums):
            upper_bound = self.binarySearch(
                nums, upper_bound + 1, len(nums) - 1, target
            )
            if upper_bound >= 0:
                ret_list[1] = upper_bound
    return ret_list


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to searchRange
    print(searchRange([]))
