"""
Shortest_window_sort

Minimum Window Sort (medium) #
    Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

    Example 1:
    Input: [1, 2, 5, 3, 7, 10, 9, 12]
    Output: 5
    Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

    Example 2:
    Input: [1, 3, 2, 0, -1, 7, 10]
    Output: 5
    Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

    Example 3:
    Input: [1, 2, 3]
    Output: 0
    Explanation: The array is already sorted

    Example 4:
    Input: [3, 2, 1]
    Output: 3
    Explanation: The whole array needs to be sorted.
"""
def shortest_window_sort(arr: list[int]) -> int:
    """
    Minimum Window Sort (medium) #
    Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

    Example 1:
    Input: [1, 2, 5, 3, 7, 10, 9, 12]
    Output: 5
    Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

    Example 2:
    Input: [1, 3, 2, 0, -1, 7, 10]
    Output: 5
    Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

    Example 3:
    Input: [1, 2, 3]
    Output: 0
    Explanation: The array is already sorted

    Example 4:
    Input: [3, 2, 1]
    Output: 3
    Explanation: The whole array needs to be sorted.
    """
    start, end = 0, len(arr) - 1
    while start < end:
        if arr[start] > arr[start + 1] and arr[end] < arr[end - 1]:
            break

        if arr[start] <= arr[start + 1]:
            start += 1

        if arr[end] >= arr[end - 1]:
            end -= 1

    if start >= end: return 0

    min_, max_ = float('inf'), float('-inf')
    for i in range(start, end + 1):
        min_ = min(min_, arr[i])
        max_ = max(max_, arr[i])

    while start > 0 and arr[start-1] > min_: start -= 1
    while end < len(arr) - 1 and arr[end + 1] < max_: end += 1

    return end - start + 1



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to shortest_window_sort
    print(shortest_window_sort([]))
