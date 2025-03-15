"""
Partition_to_min_subset_difference_memoized

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
def partition_to_min_subset_difference_memoized(nums: list[int]):
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
                 between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.

    Example 3:
    Input: {1, 3, 100, 4}
    Output: 92
    Explanation: We can partition the given set into two subsets where minimum absolute difference
                 between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.
    """
    # TODO: Come back to
    if not nums: return 0
    elif len(nums) == 1: return nums[0]

    s = sum(nums)
    target = s//2
    dp = [[None for col in range(target)] for row in range(len(nums))]
    pass



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to partition_to_min_subset_difference_memoized
    print(partition_to_min_subset_difference_memoized([]))
