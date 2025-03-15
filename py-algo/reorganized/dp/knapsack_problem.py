"""
Problem

"""
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



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to knapsackProblem
    print(knapsackProblem([]))
