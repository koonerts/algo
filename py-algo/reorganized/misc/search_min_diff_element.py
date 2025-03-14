"""
Search_min_diff_element

Given an array of numbers sorted in ascending order, find the element in the array
    that has the minimum difference with the given ‘key’.

    Example 1:
    Input: [4, 6, 10], key = 7
    Output: 6
    Explanation: The difference between the key '7' and '6' is minimum than any other number in the array

    Example 2:
    Input: [4, 6, 10], key = 4
    Output: 4

    Example 3:
    Input: [1, 3, 8, 10, 15], key = 12
    Output: 10

    Example 4:
    Input: [4, 6, 10], key = 17
    Output: 10
"""


def search_min_diff_element(arr: list[int], key: int) -> int:
    """
    Given an array of numbers sorted in ascending order, find the element in the array
    that has the minimum difference with the given ‘key’.

    Example 1:
    Input: [4, 6, 10], key = 7
    Output: 6
    Explanation: The difference between the key '7' and '6' is minimum than any other number in the array

    Example 2:
    Input: [4, 6, 10], key = 4
    Output: 4

    Example 3:
    Input: [1, 3, 8, 10, 15], key = 12
    Output: 10

    Example 4:
    Input: [4, 6, 10], key = 17
    Output: 10
    """
    if key <= arr[0]:
        return arr[0]
    elif key >= arr[len(arr) - 1]:
        return arr[len(arr) - 1]

    start, end = 0, len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == key:
            return key
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1

    start_diff = abs(key - arr[start])
    end_diff = abs(key - arr[end])

    if start_diff <= end_diff:
        return arr[start]
    else:
        return arr[end]


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to search_min_diff_element
    print(search_min_diff_element([]))
