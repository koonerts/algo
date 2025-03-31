"""
Max_sub_array_of_size_k

Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

    Example 1:
    Input: [2, 1, 5, 1, 3, 2], k=3
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].

    Example 2:
    Input: [2, 3, 4, 1, 5], k=2
    Output: 7
    Explanation: Subarray with maximum sum is [3, 4].
"""


def max_sub_array_of_size_k(k: int, arr: list[int]) -> int:
    """
    Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

    Example 1:
    Input: [2, 1, 5, 1, 3, 2], k=3
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].

    Example 2:
    Input: [2, 3, 4, 1, 5], k=2
    Output: 7
    Explanation: Subarray with maximum sum is [3, 4].
    """
    start, max_sum, curr_sum = 0, 0, 0
    for i in range(len(arr)):
        if i - start + 1 <= k:
            curr_sum += arr[i]
        else:
            curr_sum -= arr[start]
            start += 1
            curr_sum += arr[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

    return max_sum


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to max_sub_array_of_size_k
    print(max_sub_array_of_size_k([]))
