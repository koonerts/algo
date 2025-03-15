"""
Smallest_subarray_with_given_sum

Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray
    whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

    Example 1:
    Input: [2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

    Example 2:
    Input: [2, 1, 5, 2, 8], S=7
    Output: 1
    Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

    Example 3:
    Input: [3, 4, 1, 1, 6], S=8
    Output: 3
    Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
"""


def smallest_subarray_with_given_sum(s: int, arr: list[int]) -> int:
    """
    Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray
    whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

    Example 1:
    Input: [2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

    Example 2:
    Input: [2, 1, 5, 2, 8], S=7
    Output: 1
    Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

    Example 3:
    Input: [3, 4, 1, 1, 6], S=8
    Output: 3
    Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].
    """
    start, curr_sum, min_length = 0, 0, len(arr) + 1
    for window_end in range(0, len(arr)):
        curr_sum += arr[window_end]  # add the next element

        # shrink the window as small as possible until the 'curr_sum' is smaller than 's'
        while curr_sum >= s:
            min_length = min(min_length, window_end - start + 1)
            curr_sum -= arr[start]
            start += 1
    if min_length > len(arr):
        return 0
    return min_length


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to smallest_subarray_with_given_sum
    print(smallest_subarray_with_given_sum([]))
