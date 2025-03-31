"""
Find_index_of_max_in_bitonic_array

Find the maximum value in a given Bitonic array.
    An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
    Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

    Example 1:
    Input: [1, 3, 8, 12, 4, 2]
    Output: 12
    Explanation: The maximum number in the input bitonic array is '12'.

    Example 2:
    Input: [3, 8, 3, 1]
    Output: 8

    Example 3:
    Input: [1, 3, 8, 12]
    Output: 12

    Example 4:
    Input: [10, 9, 8]
    Output: 10
"""


def find_index_of_max_in_bitonic_array(arr) -> int:
    """
    Find the maximum value in a given Bitonic array.
    An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
    Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

    Example 1:
    Input: [1, 3, 8, 12, 4, 2]
    Output: 12
    Explanation: The maximum number in the input bitonic array is '12'.

    Example 2:
    Input: [3, 8, 3, 1]
    Output: 8

    Example 3:
    Input: [1, 3, 8, 12]
    Output: 12

    Example 4:
    Input: [10, 9, 8]
    Output: 10
    """
    if len(arr) <= 2:
        return 0

    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if mid + 1 <= len(arr) - 1 and arr[mid] < arr[mid + 1]:
            start = mid + 1
        elif end - 1 >= 0 and arr[mid] < arr[mid - 1]:
            end = mid - 1
        else:
            return mid


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_index_of_max_in_bitonic_array
    print(find_index_of_max_in_bitonic_array([]))
