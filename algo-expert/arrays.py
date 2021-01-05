
def getNthFib(n):
    if n <= 1: return 1

    memo = [-1 for _ in range(n)]
    memo[0], memo[1] = 0, 1

    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[-1]


def productSum(array):
    # Write your code here.
    pass

print(getNthFib(5))