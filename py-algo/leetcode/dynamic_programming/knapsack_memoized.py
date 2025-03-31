"""
Knapsack_memoized

"""


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
        profit1 = profits[currentIndex] + knapsack_memoized(
            dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1
        )

    # recursive call after excluding the element at the currentIndex
    profit2 = knapsack_memoized(dp, profits, weights, capacity, currentIndex + 1)

    dp[currentIndex][capacity] = max(profit1, profit2)
    return dp[currentIndex][capacity]


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to knapsack_memoized
    print(knapsack_memoized([]))
