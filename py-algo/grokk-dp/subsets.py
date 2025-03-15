import numpy as np


def print_matrix(matrix):
    print(np.array(matrix))


def can_partition_subsets_equal(nums):
    total_sum = sum(nums)
    if total_sum % 2 == 1:
        return False

    target = total_sum // 2
    dp = [[0 for _ in range(target + 1)] for _ in range(len(nums) + 1)]

    for i in range(1, len(nums) + 1):
        for j in range(1, target + 1):
            if dp[i - 1][j] == 1:
                dp[i][j] = 1
            else:
                curr_sum = j
                remaining_sum = curr_sum - nums[i - 1]
                if remaining_sum == 0:
                    dp[i][j] = 1
                elif remaining_sum > 0:
                    dp[i][j] = dp[i - 1][remaining_sum]

    print_matrix(dp)
    return dp[-1][-1] == 1


def can_partition_subsets(nums, target):
    dp = [[0 for _ in range(target + 1)] for _ in range(len(nums) + 1)]

    for i in range(1, len(nums) + 1):
        for j in range(1, target + 1):
            if dp[i - 1][j] == 1:
                dp[i][j] = 1
            else:
                curr_sum = j
                remaining_sum = curr_sum - nums[i - 1]
                if remaining_sum == 0:
                    dp[i][j] = 1
                elif remaining_sum > 0:
                    dp[i][j] = dp[i - 1][remaining_sum]

    print_matrix(dp)
    return dp[-1][-1] == 1


def minimum_diff_subsets(nums):
    total_sum = sum(nums)
    target = total_sum // 2 + 1 if total_sum % 2 == 1 else total_sum // 2
    dp = [[0 for _ in range(target + 1)] for _ in range(len(nums))]

    for i in range(len(nums)):
        for j in range(1, target + 1):
            can_partition = dp[i - 1][j] if i - 1 >= 0 else 0
            if not can_partition and j - nums[i] >= 0:
                can_partition = 1 if j - nums[i] == 0 else dp[i - 1][j - nums[i]]
            dp[i][j] = can_partition

    # print_matrix(dp)
    min_diff = float("inf")
    for j in reversed(range(len(dp[0]))):
        if dp[-1][j] == 1:
            min_diff = abs((total_sum - j) - j)
            break
    return min_diff


def count_subsets(nums, target):
    n = len(nums)
    dp = [[0 for _ in range(target + 1)] for _ in range(n)]

    for i in range(n):
        for j in range(1, target + 1):
            prev_count = dp[i - 1][j] if i - 1 >= 0 else 0
            remaining_sum = j - nums[i]
            if remaining_sum == 0:
                dp[i][j] += prev_count + 1
            elif remaining_sum > 0 and i - 1 >= 0:
                dp[i][j] += prev_count + dp[i - 1][remaining_sum]
            else:
                dp[i][j] += prev_count
    return dp[-1][-1]


print(count_subsets([1, 2, 7, 1, 5], 9))
