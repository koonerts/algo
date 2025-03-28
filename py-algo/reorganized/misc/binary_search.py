"""
Binary_search

Given a sorted array of numbers, find if a given number ‘key’ is present in the array.
    Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order.
    You should assume that the array can have duplicates.
    Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

    Example 1:
    Input: [4, 6, 10], key = 10
    Output: 2

    Example 2:
    Input: [1, 2, 3, 4, 5, 6, 7], key = 5
    Output: 4

    Example 3:
    Input: [10, 6, 4], key = 10
    Output: 0

    Example 4:
    Input: [10, 6, 4], key = 4
    Output: 2
"""


def binary_search(arr: list[int], key: int) -> int:
    """
    Given a sorted array of numbers, find if a given number ‘key’ is present in the array.
    Though we know that the array is sorted, we don’t know if it’s sorted in ascending or descending order.
    You should assume that the array can have duplicates.
    Write a function to return the index of the ‘key’ if it is present in the array, otherwise return -1.

    Example 1:
    Input: [4, 6, 10], key = 10
    Output: 2

    Example 2:
    Input: [1, 2, 3, 4, 5, 6, 7], key = 5
    Output: 4

    Example 3:
    Input: [10, 6, 4], key = 10
    Output: 0

    Example 4:
    Input: [10, 6, 4], key = 4
    Output: 2
    """
    if not arr:
        return -1

    start, end = 0, len(arr) - 1
    is_ascending = True if len(arr) > 1 and arr[0] < arr[1] else False

    while start <= end:
        mid = int((start + end) / 2)

        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            if is_ascending:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if is_ascending:
                end = mid - 1
            else:
                start = mid + 1

    return False


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to binary_search
    print(binary_search([]))
