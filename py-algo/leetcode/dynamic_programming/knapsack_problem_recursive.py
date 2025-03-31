"""
Problem Recursive

"""


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


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to knapsackProblemRecursive
    print(knapsackProblemRecursive([]))
