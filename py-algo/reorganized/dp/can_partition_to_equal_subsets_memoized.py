"""
Can_partition_to_equal_subsets_memoized

"""
def can_partition_to_equal_subsets_memoized(nums) -> bool:
    s = sum(nums)

    # if 's' is a an odd number, we can't have two subsets with equal sum
    if s % 2 != 0:
        return False

    # initialize the 'dp' array, -1 for default, 1 for true and 0 for false
    dp = [[None for row in range(s//2)] for col in range(len(nums))]
def can_partition_recursive(curr_sum: int, curr_index: int) -> bool:
        if curr_sum == 0:
            return True
        elif curr_index >= len(nums):
            return False

        row = curr_index
        col = curr_sum - 1

        if dp[row][col] is None:
            num = nums[row]
            new_sum = curr_sum - num
            dp[row][col] = (new_sum >= 0 and can_partition_recursive(new_sum, row+1)) or can_partition_recursive(curr_sum, row+1)

        return bool(dp[row][col])

    return can_partition_recursive(s//2, 0)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to can_partition_to_equal_subsets_memoized
    print(can_partition_to_equal_subsets_memoized([]))
