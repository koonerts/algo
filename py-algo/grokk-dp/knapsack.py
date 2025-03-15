import numpy as np


def print_matrix(matrix):
    print(np.array(matrix))


def basic_knapsack(profits, weights, capacity):
    max_profits = [[0 for y in range(capacity + 1)] for x in range(len(weights) + 1)]
    for i in range(len(max_profits)):
        max_profits[i][0] = 0
    for i in range(len(max_profits[0])):
        max_profits[0][i] = 0

    for i in range(1, len(max_profits)):
        for j in range(1, len(max_profits[0])):
            weight, profit = weights[i - 1], profits[i - 1]

            profit_with = 0
            if weight <= j:
                profit_with = max_profits[i - 1][j - weight] + profit

            profit_without = max_profits[i - 1][j]
            max_profits[i][j] = max(profit_with, profit_without)

    return max_profits[-1][-1], get_selected_knapsack_items(
        max_profits, profits, weights
    )


def get_selected_knapsack_items(max_profits, profits, weights):
    profit = max_profits[-1][-1]
    capacity = len(max_profits[0]) - 1
    items_picked = []

    for i in reversed(range(len(max_profits))):
        if i - 1 < 0 or capacity < 0:
            break
        if profit != max_profits[i - 1][capacity]:
            items_picked.append(i - 1)
            profit -= profits[i - 1]
            capacity -= weights[i - 1]
    items_picked.reverse()
    return items_picked
