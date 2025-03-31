"""
Search_bitonic_array

Given a Bitonic array, find if a given ‘key’ is present in it.
    An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
    Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
    Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

    Example 1:
    Input: [1, 3, 8, 4, 3], key=4
    Output: 3

    Example 2:
    Input: [3, 8, 3, 1], key=8
    Output: 1

    Example 3:
    Input: [1, 3, 8, 12], key=12
    Output: 3

    Example 4:
    Input: [10, 9, 8], key=10
    Output: 0
"""
def search_bitonic_array(arr, key):
    """
    Given a Bitonic array, find if a given ‘key’ is present in it.
    An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
    Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].
    Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

    Example 1:
    Input: [1, 3, 8, 4, 3], key=4
    Output: 3

    Example 2:
    Input: [3, 8, 3, 1], key=8
    Output: 1

    Example 3:
    Input: [1, 3, 8, 12], key=12
    Output: 3

    Example 4:
    Input: [10, 9, 8], key=10
    Output: 0
    """
def b_search(start, end, is_ascending) -> int:
        while start <= end:
            mid = (start + end)//2
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
        return -1

    max_index = find_index_of_max_in_bitonic_array(arr)
    if key == arr[max_index]:
        return max_index
    else:
        i = b_search(0, max_index - 1, True)

        # search descending half
        if i == -1 and key < arr[max_index]:
            i = b_search(max_index+1, len(arr)-1, False)

        return i


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to search_bitonic_array
    print(search_bitonic_array([]))
