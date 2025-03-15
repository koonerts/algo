"""
Of Ways To Make Change

"""
def numberOfWaysToMakeChange(n, denoms):
    memo = [0 for i in range(n + 1)]
    memo[0] = 1

    for denom in denoms:
        for i in range(1, n + 1):
            if denom <= i:
                memo[i] += memo[i - denom]
    return memo[-1]



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to numberOfWaysToMakeChange
    print(numberOfWaysToMakeChange([]))
