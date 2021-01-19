

def maxSubsetSumNoAdjacent(array):
    if not array: return 0
    EMPTY = float('-inf')
    memo = [EMPTY for n in array]

    def find(idx):
        if idx < 0:
            return 0
        else:
            if memo[idx] == EMPTY:
                memo[idx] = max(find(idx-1), find(idx-2) + array[idx])
            return memo[idx]
    return find(len(array)-1)


def numberOfWaysToMakeChange(n, denoms):
    memo = [0 for i in range(n+1)]
    memo[0] = 1

    for denom in denoms:
        for i in range(1, n+1):
            if denom <= i:
                memo[i] += memo[i-denom]
    return memo[-1]


def minNumberOfCoinsForChange(n, denoms):
    min_coins = [float('inf') for i in range(n+1)]
    min_coins[0] = 0

    for i in range(len(denoms)):
        for j in range(len(min_coins)):
            if denoms[i] <= j:
                min_coins[j] = min(min_coins[j], min_coins[j-denoms[i]] + 1)
    return min_coins[-1] if min_coins[-1] < float('inf') else -1


def levenshteinDistance(str1, str2):
    prev_i, prev_j, prev_ij, curr = 0, 0, 0, 0
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                pass


def knapsackProblem(items, capacity):
    PRICE, WEIGHT = 0, 1
    memo = [[0 for j in range(capacity+1)] for i in range(len(items)+1)]

    for i in range(1, len(memo)):
        for j in range(1, len(memo[0])):
            if j - items[i-1][WEIGHT] >= 0:
                memo[i][j] = max(memo[i-1][j], memo[i-1][j-items[i-1][WEIGHT]] + items[i-1][PRICE])
            else:
                memo[i][j] = memo[i-1][j]

    profit = memo[-1][-1]
    chosen_items = []
    for i in range(len(memo), 0, -1):
        if profit != memo[i-1][capacity]:
            chosen_items.append(i-1)
            capacity -= items[i-1][WEIGHT]
            profit -= items[i-1][PRICE]
    return memo[-1][-1], chosen_items[-1::-1]


def knapsackProblemRecursive(items, capacity):
    PRICE, WEIGHT = 0, 1
    memo = [[-1 for j in range(capacity+1)] for i in range(len(items)+1)]

    def helper(i, j):
        if i >= len(memo) or j <= 0:
            return 0
        elif memo[i][j] != -1:
            return memo[i][j]
        else:
            profit_with = 0
            if items[i-1][WEIGHT] <= j:
                profit_with = helper(i+1, j-items[i-1][WEIGHT]) + items[i-1][PRICE]
            profit_without = helper(i+1, j)

            memo[i][j] = max(profit_with, profit_without)
            return memo[i][j]
    return helper(1, capacity)
    # profit = memo[-1][-1]
    # chosen_items = []
    # for i in range(len(memo), 0, -1):
    #     if profit != memo[i-1][capacity]:
    #         chosen_items.append(i-1)
    #         capacity -= items[i-1][WEIGHT]
    #         profit -= items[i-1][PRICE]
    # return memo[-1][-1], chosen_items[-1::-1]




print(knapsackProblemRecursive([[1, 2], [4, 3], [5, 6], [6, 7]], 10))