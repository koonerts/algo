"""
Can_partition_with_subset_sum_equal_to_s_memoized

"""
def can_partition_with_subset_sum_equal_to_s_memoized(nums: list[int], s: int) -> bool:
    dp = [[None for col in range(s)] for row in range(len(nums))]
def can_partition_recursive(curr_sum, curr_row) -> bool:
        if curr_row >= len(nums):
            return False

        col = curr_sum - 1
        if dp[curr_row][col] is not None:
            return bool(dp[curr_row][col])
        elif curr_sum == s:
            dp[curr_row][col] = True
        else:
            num = nums[curr_row]
            new_sum = curr_sum + num
            dp[curr_row][col] = ((new_sum <= s and can_partition_recursive(new_sum, curr_row+1))
                                 or can_partition_recursive(curr_sum, curr_row+1))

        return bool(dp[curr_row][col])

    return can_partition_recursive(0, 0)



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to can_partition_with_subset_sum_equal_to_s_memoized
    print(can_partition_with_subset_sum_equal_to_s_memoized([]))
