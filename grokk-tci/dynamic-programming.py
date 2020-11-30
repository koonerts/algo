

def solve_knapsack(profits, weights, capacity):
    """
    Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack with a capacity ‘C.’
    The goal is to get the maximum profit out of the knapsack items.
    Each item can only be selected once, as we don’t have multiple quantities of any item.

    Let’s take Merry’s example, who wants to carry some fruits in the knapsack to get maximum profit.
    Here are the weights and profits of the fruits:
        Items: { Apple, Orange, Banana, Melon }
        Weights: { 2, 3, 1, 4 }
        Profits: { 4, 5, 3, 7 }
        Knapsack capacity: 5

    Let’s try to put various combinations of fruits in the knapsack, such that their total weight is not more than 5:
        Apple + Orange (total weight 5) => 9 profit
        Apple + Banana (total weight 3) => 7 profit
        Orange + Banana (total weight 4) => 8 profit
        Banana + Melon (total weight 5) => 10 profit

    This shows that Banana + Melon is the best combination as it gives us the maximum profit
    and the total weight does not exceed the capacity.

    Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of
    these items which will give us maximum profit such that their cumulative weight is not more than a given number ‘C.’
    Each item can only be selected once, which means either we put an item in the knapsack or we skip it.
    :param profits:
    :param weights:
    :param capacity:
    :return:
    """
    # create a two dimensional array for Memoization, each element is initialized to '-1'
    dp = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
    return knapsack_memoized(dp, profits, weights, capacity, 0)


def knapsack_memoized(dp, profits, weights, capacity, currentIndex):
    # base checks
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    # if we have already solved a similar problem, return the result from memory
    if dp[currentIndex][capacity] != -1:
        return dp[currentIndex][capacity]

    # recursive call after choosing the element at the currentIndex
    # if the weight of the element at currentIndex exceeds the capacity, we
    # shouldn't process this
    profit1 = 0
    if weights[currentIndex] <= capacity:
        profit1 = profits[currentIndex]+knapsack_memoized(
            dp, profits, weights, capacity-weights[currentIndex], currentIndex+1)

    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_memoized(
        dp, profits, weights, capacity, currentIndex+1)

    dp[currentIndex][capacity] = max(profit1, profit2)
    return dp[currentIndex][capacity]


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
                 between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.

    Example 3:
    Input: {1, 3, 100, 4}
    Output: 92
    Explanation: We can partition the given set into two subsets where minimum absolute difference
                 between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.
    """
    # TODO: Come back to


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


def count_subsets(nums, sum):
    """
    Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

    Example 1:
    Input: {1, 1, 2, 3}, S=4
    Output: 3
    The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
    Note that we have two similar sets {1, 3}, because we have two '1' in our input.

    Example 2:
    Input: {1, 2, 7, 1, 5}, S=9
    Output: 3
    The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}
    """
    # TODO: Come back to
    return -1


def find_target_subsets(nums, s):
    """
    You are given a set of positive numbers and a target sum ‘S’. Each number should be assigned either a ‘+’ or ‘-’ sign. We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.

    Example 1:
    Input: {1, 1, 2, 3}, S=1
    Output: 3
    Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

    Example 2:
    Input: {1, 2, 7, 1}, S=9
    Output: 2
    Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}
    """
    # TODO: Come back to
    return -1


def main():
    print("Can partition: " + str(partition_to_min_subset_difference_memoized([1, 2, 3, 9])))
    print("Can partition: " + str(partition_to_min_subset_difference_memoized([1, 2, 7, 1, 5])))
    print("Can partition: " + str(partition_to_min_subset_difference_memoized([1, 3, 100, 4])))


main()
