"""
Subset Sum No Adjacent

"""
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


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to maxSubsetSumNoAdjacent
    print(maxSubsetSumNoAdjacent([]))
