"""
Number_of_options2

"""
def number_of_options2(a, b, c, d, target):
    sources = [a, b, c, d]
    dp = [[0] * (target + 1) for _ in range(5)]
    dp[4][0] = 1

    for i in range(3, -1, -1):
        for j in range(target + 1)[::-1]:
            if dp[i + 1][j]:
                for v in sources[i]:
                    if j + v <= target:
                        dp[i][v + j] += dp[i + 1][j]

    return sum(dp[0])



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to number_of_options2
    print(number_of_options2([]))
