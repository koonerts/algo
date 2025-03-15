"""
Can_partition_to_equal_subsets_tabulated

"""
def can_partition_to_equal_subsets_tabulated(nums):
    s = sum(nums)

    # if 's' is a an odd number, we can't have two subsets with equal sum
    if s % 2 != 0:
        return False

    dp = [[None for col in range(s//2)] for row in range(len(nums))]

    for row in range(len(dp)):
        for col in range(len(dp[row])):
            val = row-1 >= 0 and dp[row-1][col] is True

            if not val:
                curr_sum = col+1
                num = nums[row]
                remaining_sum = curr_sum-num

                if remaining_sum == 0:
                    val = True
                elif remaining_sum < 0:
                    val = False
                else:
                    val = row-1 >= 0 and dp[row-1][remaining_sum-1] is True

            dp[row][col] = val

    return dp[-1][-1]



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to can_partition_to_equal_subsets_tabulated
    print(can_partition_to_equal_subsets_tabulated([]))
