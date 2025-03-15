def knapsack_memoized(profits, weights, capacity):
    """
    Finds the maximum value that can be put in a knapsack
    :param profits: The profit that can be gained by each item
    :param weights: The weight of each piece of jewelry
    :param capacity: The maximum weight that the knapsack can hold
    :return: Maximum value that can be put in a knapsack
    """

    def recurse(idx, curr_capacity):
        if idx >= len(profits):
            return 0
        elif (idx, curr_capacity) in memo:
            return memo[(idx, curr_capacity)]
        else:
            profit1 = 0
            if curr_capacity - weights[idx] >= 0:
                profit1 = profits[idx] + recurse(idx + 1, curr_capacity - weights[idx])

            profit2 = recurse(idx + 1, curr_capacity)
            memo[(idx, curr_capacity)] = max(profit1, profit2)
            return memo[(idx, curr_capacity)]

    memo = {}
    return recurse(0, capacity)


def count_ways(n):
    """
    Calculates the number of ways a stair can be climbed
    :param n: Number of stairs
    :return: Number of ways to climb a stair
    """
    pass


def can_partition(nums):
    """
    Checks if two sub-lists has equal sum or not
    :param nums: Integer list having positive numbers only
    :return: returns True if two sub-lists have equal sum, otherwise False
    """
    nums_sum = sum(nums)
    if nums_sum % 2 == 1:
        return False
    memo = [[-1 for col in range(nums_sum // 2 + 1)] for row in range(len(nums) + 1)]

    def can_partition_recursive(r, curr_sum):
        if curr_sum == 0:
            return True
        elif not ((1 <= r <= len(nums)) and (1 <= curr_sum <= nums_sum // 2)):
            return False
        else:
            if memo[r][curr_sum] == -1:
                memo[r][curr_sum] = can_partition_recursive(
                    r + 1, curr_sum
                ) or can_partition_recursive(r + 1, curr_sum - nums[r - 1])
            return memo[r][curr_sum]

    can = can_partition_recursive(1, nums_sum // 2)
    print(memo)
    return can


def longest_palindromic_subsequence(s):
    """
    Finds the longest palindromic subsequence length
    :param s: Input string
    :return: Length of shortest common superstring
    """

    def find_longest(left, right):
        if left > right:
            return 0
        elif left == right:
            return 1
        else:
            if memo[left][right] == -1:
                if s[left] == s[right]:
                    memo[left][right] = 2 + find_longest(left + 1, right - 1)
                else:
                    memo[left][right] = max(
                        find_longest(left + 1, right), find_longest(left, right - 1)
                    )
            return memo[left][right]

    memo = [[-1 for col in range(len(s))] for row in range(len(s))]
    max_len = find_longest(0, len(s) - 1)
    return max_len


def longest_palindromic_subsequence_tabulated(s):
    memo = [[0 for col in range(len(s))] for row in range(len(s))]
    for i in range(len(s)):
        memo[i][i] = 1

    for start_index in reversed(range(len(s))):
        for end_index in range(start_index + 1, len(s)):
            # case 1: elements at the beginning and the end are the same
            if s[start_index] == s[end_index]:
                memo[start_index][end_index] = 2 + memo[start_index + 1][end_index - 1]
            else:  # case 2: skip one element either from the beginning or the end
                memo[start_index][end_index] = max(
                    memo[start_index + 1][end_index], memo[start_index][end_index - 1]
                )

    return memo[0][len(s) - 1]


def count_change(denominations, amount):
    """
    Finds the number of ways that the given number of cents can be represented.
    :param denominations: Values of the coins available
    :param amount: Given cent
    :return: The number of ways that the given number of cents can be represented.
    """

    def find_ways(curr_amount, idx):
        if curr_amount == 0:
            return 1
        elif curr_amount < 0 or not (0 <= idx < len(denominations)):
            return 0
        else:
            if memo[idx][curr_amount] == -1:
                memo[idx][curr_amount] = find_ways(curr_amount, idx - 1) + find_ways(
                    curr_amount - denominations[idx], idx
                )
            return memo[idx][curr_amount]

    memo = [[-1 for col in range(amount + 1)] for row in range(len(denominations))]
    return find_ways(amount, len(denominations) - 1)


def count_change_tabulated(denominations, amount):
    memo = [[-1 for col in range(amount + 1)] for row in range(len(denominations))]
    for row in memo:
        row[0] = 1

    for i in range(len(memo)):
        for j in range(len(memo[i])):
            pass


print(count_change([25, 10, 5, 1], 950))
