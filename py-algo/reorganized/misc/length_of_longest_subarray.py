"""
Length_of_longest_subarray

Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

    Example 1:
    Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
    Output: 6
    Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

    Example 2:
    Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
    Output: 9
    Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""
def length_of_longest_subarray(arr: list[int], k: int) -> int:
    """
    Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

    Example 1:
    Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
    Output: 6
    Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

    Example 2:
    Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
    Output: 9
    Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
    """
    start, max_subarray_len, max_repeat_cntr = 0, 0, 0
    bit_map = {}

    for i, v in enumerate(arr):
        bit_map[v] = bit_map.get(v, 0) + 1
        max_repeat_cntr = max(max_repeat_cntr, bit_map[v])
        window_len = i - start + 1

        if window_len - max_repeat_cntr > k:
            if bit_map[arr[start]] == 1:
                del bit_map[arr[start]]
            else:
                bit_map[arr[start]] -= 1

            start += 1
            window_len -= 1

        max_subarray_len = max(max_subarray_len, window_len)
    return max_subarray_len



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to length_of_longest_subarray
    print(length_of_longest_subarray([]))
