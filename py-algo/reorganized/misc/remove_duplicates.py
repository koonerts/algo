"""
Remove_duplicates

Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space.
    After removing the duplicates in-place return the length of the subarray that has no duplicate in it.

    Example 1:
    Input: [2, 3, 3, 3, 6, 9, 9]
    Output: 4
    Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

    Example 2:
    Input: [2, 2, 2, 11]
    Output: 2
    Explanation: The first two elements after removing the duplicates will be [2, 11].
"""


def remove_duplicates(arr: list[int]) -> int:
    """
    Given an array of sorted numbers, remove all duplicates from it. You should not use any extra space.
    After removing the duplicates in-place return the length of the subarray that has no duplicate in it.

    Example 1:
    Input: [2, 3, 3, 3, 6, 9, 9]
    Output: 4
    Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

    Example 2:
    Input: [2, 2, 2, 11]
    Output: 2
    Explanation: The first two elements after removing the duplicates will be [2, 11].
    """
    switch_index, i = 1, 1

    while i < len(arr):
        if arr[switch_index - 1] != arr[i]:
            arr[switch_index] = arr[i]
            switch_index += 1
        i += 1

    print(arr)
    return switch_index


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to remove_duplicates
    print(remove_duplicates([]))
