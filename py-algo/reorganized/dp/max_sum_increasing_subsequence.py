"""
Sum Increasing Subsequence

"""


def maxSumIncreasingSubsequence(array):
    if not array:
        return 0, []
    sums = [num for num in array]
    prev_indexes = [None] * len(array)

    max_idx = 0
    for i in range(1, len(array)):
        for j in range(i):
            if array[j] < array[i] and sums[i] < sums[j] + array[i]:
                sums[i] = sums[j] + array[i]
                prev_indexes[i] = j

        if sums[i] > sums[max_idx]:
            max_idx = i

    print(max_idx)
    print_matrix([array, sums, prev_indexes])
    max_sum = sums[max_idx]
    nums = []

    while max_idx is not None:
        nums.append(array[max_idx])
        max_idx = prev_indexes[max_idx]
    nums.reverse()
    return max_sum, nums


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to maxSumIncreasingSubsequence
    print(maxSumIncreasingSubsequence([]))
