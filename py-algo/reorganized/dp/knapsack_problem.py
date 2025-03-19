"""
Knapsack Problem

Given a set of items, each with a weight and a value, determine the maximum value subset of items you can include in a knapsack 
so that the total weight is less than or equal to a given capacity.

Each item can only be selected once (0/1 knapsack problem).

Example:
    Input: 
        items = [[1, 2], [4, 3], [5, 6], [6, 7]]  # [value, weight]
        capacity = 10
    Output: 
        [10, [0, 2, 3]]  # Maximum profit of 10, using items at indices 0, 2, and 3
"""


def knapsackProblem(items, capacity):
    """
    Solves the 0/1 knapsack problem using dynamic programming.

    Args:
        items (list): List of [value, weight] pairs
        capacity (int): Maximum weight capacity of the knapsack

    Returns:
        tuple: (maximum profit, list of indices of selected items)
    """
    if not items or capacity <= 0:
        return 0, []

    PROFIT, WEIGHT = 0, 1
    max_profits = [[0 for _ in range(capacity + 1)] for _ in range(len(items))]

    # Fill the dp table
    for i in range(len(items)):
        for j in range(1, capacity + 1):
            profit_with = 0
            if items[i][WEIGHT] <= j:
                profit_with = items[i][PROFIT] + (
                    0 if i -
                    1 < 0 else max_profits[i - 1][j - items[i][WEIGHT]]
                )

            profit_without = 0
            if i - 1 >= 0:
                profit_without = max_profits[i - 1][j]
            max_profits[i][j] = max(profit_with, profit_without)

    # Backtrack to find which items were included
    profit = max_profits[-1][-1]
    cap = capacity
    picked_items = []
    for i in reversed(range(len(items))):
        if i == 0:
            if max_profits[0][cap] != 0:
                picked_items.append(0)
        else:
            if profit != max_profits[i - 1][cap]:
                picked_items.append(i)
                profit -= items[i][PROFIT]
                cap -= items[i][WEIGHT]

    return max_profits[-1][-1], sorted(picked_items)


# Example usage
if __name__ == "__main__":
    items = [
        [1, 2],  # value: 1, weight: 2
        [4, 3],  # value: 4, weight: 3
        [5, 6],  # value: 5, weight: 6
        [6, 7]   # value: 6, weight: 7
    ]
    capacity = 10

    max_profit, selected_items = knapsackProblem(items, capacity)
    print(f"Maximum profit: {max_profit}")
    print(f"Selected items (indices): {selected_items}")

    # Show selected items details
    print("\nSelected items details:")
    total_weight = 0
    for idx in selected_items:
        print(f"Item {idx}: Value={items[idx][0]}, Weight={items[idx][1]}")
        total_weight += items[idx][1]
    print(f"Total weight: {total_weight} / {capacity}")
