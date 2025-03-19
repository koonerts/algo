"""
Partition_to_min_subset_difference_tabulated

Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.

    Example 1:
    Input: {1, 2, 3, 9}
    Output: 3
    Explanation: We can partition the given set into two subsets where minimum absolute difference
                 between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.

    Example 2:
    Input: {1, 2, 7, 1, 5}
    Output: 0
    Explanation: We can partition the given set into two subsets where minimum absolute difference
                 between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.

    Example 3:
    Input: {1, 3, 100, 4}
    Output: 92
    Explanation: We can partition the given set into two subsets where minimum absolute difference
                 between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.
"""


def partition_to_min_subset_difference_tabulated(nums: list[int]):
    """
    Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.

    Example 1:
    Input: {1, 2, 3, 9}
    Output: 3
    Explanation: We can partition the given set into two subsets where minimum absolute difference
                 between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.

    Example 2:
    Input: {1, 2, 7, 1, 5}
    Output: 0
    Explanation: We can partition the given set into two subsets where minimum absolute difference
                 between the sum of numbers is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
    """
    if not nums:
        return 0

    s = sum(nums)
    n = len(nums)
    dp = [[False for _ in range(s // 2 + 1)] for _ in range(n)]

    # populate the s=0 columns, as we can always form '0' sum with an empty set
    for i in range(n):
        dp[i][0] = True

    # with only one number, we can form a subset only when the required sum is equal to that number
    for j in range(1, s // 2 + 1):
        dp[0][j] = nums[0] == j

    # process all subsets for all sums
    for i in range(1, n):
        for j in range(1, s // 2 + 1):
            # if we can get the sum 'j' without the number at index 'i'
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            # else if we can find a subset to get the remaining sum
            elif j >= nums[i]:
                dp[i][j] = dp[i - 1][j - nums[i]]

    # Find the largest sum possible up to s//2
    sum1 = 0
    for j in range(s // 2, -1, -1):
        if dp[n - 1][j]:
            sum1 = j
            break

    sum2 = s - sum1
    return abs(sum2 - sum1)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to partition_to_min_subset_difference_tabulated
    print(partition_to_min_subset_difference_tabulated([1, 2, 3, 9]))
