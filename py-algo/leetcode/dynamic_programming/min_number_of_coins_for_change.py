"""
Number Of Coins For Change

"""


def minNumberOfCoinsForChange(n, denoms):
    min_coins = [float("inf") for i in range(n + 1)]
    min_coins[0] = 0

    for i in range(len(denoms)):
        for j in range(len(min_coins)):
            if denoms[i] <= j:
                min_coins[j] = min(min_coins[j], min_coins[j - denoms[i]] + 1)
    return min_coins[-1] if min_coins[-1] < float("inf") else -1


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to minNumberOfCoinsForChange
    print(minNumberOfCoinsForChange([]))
