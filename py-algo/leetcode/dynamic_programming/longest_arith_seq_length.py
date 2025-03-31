"""
Arith Seq Length

"""
def longestArithSeqLength(A):
    ret = 1
def maxSeqHelper(d):
        memo, ans = dict(), 1
        for num in A:
            if num - d in memo:
                memo[num] = memo[num - d] + 1
            else:
                memo[num] = 1
            ans = max(ans, memo[num])
        print(memo)
        return ans

    for d in range(-500, 501): ret = max(ret, maxSeqHelper(d))
    return ret


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to longestArithSeqLength
    print(longestArithSeqLength([]))
