

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
    memo = [float('-inf') for i in range(n+1)]
    memo[0] = 1
    for i in range(len(denoms)):
        for j in range(len(memo)):
            if denoms[i] <= j:
                pass


def minNumberOfCoinsForChange(n, denoms):
    min_coins = [float('inf') for i in range(n+1)]
    min_coins[0] = 0

    for i in range(len(denoms)):
        for j in range(len(min_coins)):
            if denoms[i] <= j:
                min_coins[j] = min(min_coins[j], min_coins[j-denoms[i]] + 1)
    return min_coins[-1] if min_coins[-1] < float('inf') else -1