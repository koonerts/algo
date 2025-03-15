"""
Can_partition_with_subset_sum_equal_to_s_tabulated

Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.

    Example 1:
    Input: {1, 2, 3, 7}, S=6
    Output: True
    The given set has a subset whose sum is '6': {1, 2, 3}

    Example 2:
    Input: {1, 2, 7, 1, 5}, S=10
    Output: True
    The given set has a subset whose sum is '10': {1, 2, 7}

    Example 3:
    Input: {1, 3, 4, 8}, S=6
    Output: False
    The given set does not have any subset whose sum is equal to '6'.
"""
def can_partition_with_subset_sum_equal_to_s_tabulated(nums: list[int], s: int) -> bool:
    """
    Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.

    Example 1:
    Input: {1, 2, 3, 7}, S=6
    Output: True
    The given set has a subset whose sum is '6': {1, 2, 3}

    Example 2:
    Input: {1, 2, 7, 1, 5}, S=10
    Output: True
    The given set has a subset whose sum is '10': {1, 2, 7}

    Example 3:
    Input: {1, 3, 4, 8}, S=6
    Output: False
    The given set does not have any subset whose sum is equal to '6'.
    """
    dp = [[None for col in range(s)] for row in range(len(nums))]

    for row in range(len(dp)):
        for col in range(len(dp[row])):
            val = row-1 >= 0 and dp[row-1][col] is True

            if not val:
                num = nums[row]
                curr_sum = col+1
                remaining_sum = curr_sum - num
                val = remaining_sum == 0 or (remaining_sum > 0 and row-1 >= 0 and dp[row-1][remaining_sum-1] is True)

            dp[row][col] = val

    return bool(dp[-1][-1])



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to can_partition_with_subset_sum_equal_to_s_tabulated
    print(can_partition_with_subset_sum_equal_to_s_tabulated([]))
