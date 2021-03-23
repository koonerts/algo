import numpy as np


def print_matrix(matrix):
    print(np.array(matrix))


def maxSubsetSumNoAdjacent(array):
    if not array: return 0
    EMPTY = float('-inf')
    memo = [EMPTY for n in array]

    def find(idx):
        if idx < 0:
            return 0
        else:
            if memo[idx] == EMPTY:
                memo[idx] = max(find(idx - 1), find(idx - 2) + array[idx])
            return memo[idx]

    return find(len(array) - 1)


def numberOfWaysToMakeChange(n, denoms):
    memo = [0 for i in range(n + 1)]
    memo[0] = 1

    for denom in denoms:
        for i in range(1, n + 1):
            if denom <= i:
                memo[i] += memo[i - denom]
    return memo[-1]


def minNumberOfCoinsForChange(n, denoms):
    min_coins = [float('inf') for i in range(n + 1)]
    min_coins[0] = 0

    for i in range(len(denoms)):
        for j in range(len(min_coins)):
            if denoms[i] <= j:
                min_coins[j] = min(min_coins[j], min_coins[j - denoms[i]] + 1)
    return min_coins[-1] if min_coins[-1] < float('inf') else -1


def knapsackProblem(items, capacity):
    PROFIT, WEIGHT = 0, 1
    max_profits = [[0 for _ in range(capacity + 1)] for _ in range(len(items))]

    for i in range(len(items)):
        for j in range(1, capacity + 1):
            profit_with = 0
            if items[i][WEIGHT] <= j:
                profit_with = items[i][PROFIT] + (0 if i - 1 < 0 else max_profits[i - 1][j - items[i][WEIGHT]])

            profit_without = 0
            if i - 1 >= 0 and j - 1 >= 0:
                profit_without = max_profits[i - 1][j]
            max_profits[i][j] = max(profit_with, profit_without)

    profit = max_profits[-1][-1]
    cap = capacity
    picked_items = []
    for i in reversed(range(len(max_profits))):
        if i == 0:
            if items[i][WEIGHT] <= cap:
                picked_items.append(0)
        else:
            if profit != max_profits[i - 1][cap]:
                picked_items.append(i)
                profit -= items[i][PROFIT]
                cap -= items[i][WEIGHT]
    return max_profits[-1][-1], picked_items


def knapsackProblemRecursive(items, capacity):
    PRICE, WEIGHT = 0, 1
    memo = [[-1 for j in range(capacity + 1)] for i in range(len(items) + 1)]

    def helper(i, j):
        if i >= len(memo) or j <= 0:
            return 0
        elif memo[i][j] != -1:
            return memo[i][j]
        else:
            profit_with = 0
            if items[i - 1][WEIGHT] <= j:
                profit_with = helper(i + 1, j - items[i - 1][WEIGHT]) + items[i - 1][PRICE]
            profit_without = helper(i + 1, j)

            memo[i][j] = max(profit_with, profit_without)
            return memo[i][j]

    return helper(1, capacity)


def levenshteinDistance(s, t):
    rows = len(s) + 1
    cols = len(t) + 1
    dist = [[0 for x in range(cols)] for x in range(rows)]

    # source prefixes can be transformed into empty strings
    # by deletions:
    for i in range(1, rows):
        dist[i][0] = i

    # target prefixes can be created from an empty source string
    # by inserting the characters
    for i in range(1, cols):
        dist[0][i] = i

    for col in range(1, cols):
        for row in range(1, rows):
            if s[row - 1] == t[col - 1]:
                cost = 0
            else:
                cost = 1
            dist[row][col] = min(dist[row - 1][col] + 1,  # deletion
                                 dist[row][col - 1] + 1,  # insertion
                                 dist[row - 1][col - 1] + cost)  # substitution

    print_matrix(dist)
    return dist[-1][-1]


def minNumberOfJumps(array):
    def min_jumps(idx):
        if idx <= 0:
            return 0
        else:
            return min_jumps()


def maxSumIncreasingSubsequence(array):
    if not array: return 0, []
    sums = [num for num in array]
    prev_indexes = [None] * len(array)

    max_idx = 0
    for i in range(1, len(array)):
        for j in range(i):
            if array[j] < array[i] and sums[i] < sums[j] + array[i]:
                sums[i] = sums[j] + array[i]
                prev_indexes[i] = j

        if sums[i] > sums[max_idx]:
            max_idx = i

    print(max_idx)
    print_matrix([array, sums, prev_indexes])
    max_sum = sums[max_idx]
    nums = []

    while max_idx is not None:
        nums.append(array[max_idx])
        max_idx = prev_indexes[max_idx]
    nums.reverse()
    return max_sum, nums


print(levenshteinDistance('elxyotpogyqouwyptbjqfrtkgtygvvmyqldjtjkhwzfebqzbgznsbaeixwpaelxyotpogyqouwyptbjqfrtkgtygvvmyqldjtjkhwzfebqzbgznsbaeixwpa', 'ylxyocpogynouwybtbjqxrtkgxygvvmyqldptjkhyzfebpzbgzksbaeoxwpaabcdylxyocpogynouwybtbjqxrtkgxygvvmyqldptjkhyzfebpzbgzksbaeoxwpa'))

