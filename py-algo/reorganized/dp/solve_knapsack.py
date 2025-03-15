"""
Solve_knapsack

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



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to solve_knapsack
    print(solve_knapsack([]))
