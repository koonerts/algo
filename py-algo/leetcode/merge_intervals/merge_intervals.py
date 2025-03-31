"""
Merge_intervals

Given two lists of intervals, find the intersection of these two lists.
    Each list consists of disjoint intervals sorted on their start time.

    Example 1:
    Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
    Output: [2, 3], [5, 6], [7, 7]
    Explanation: The output list contains the common intervals between the two lists.

    Example 2:
    Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
    Output: [5, 7], [9, 10]
    Explanation: The output list contains the common intervals between the two lists.
"""


def merge_intervals(
    intervals_a: list[list[int]], intervals_b: list[list[int]]
) -> list[list[int]]:
    """
    Given two lists of intervals, find the intersection of these two lists.
    Each list consists of disjoint intervals sorted on their start time.

    Example 1:
    Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
    Output: [2, 3], [5, 6], [7, 7]
    Explanation: The output list contains the common intervals between the two lists.

    Example 2:
    Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
    Output: [5, 7], [9, 10]
    Explanation: The output list contains the common intervals between the two lists.
    """
    result = []
    start, end = 0, 1
    index_a, index_b = 0, 0

    while index_a < len(intervals_a) and index_b < len(intervals_b):
        iv_a, iv_b = intervals_a[index_a], intervals_b[index_b]
        if (
            iv_b[start] <= iv_a[start] <= iv_b[end]
            or iv_a[start] <= iv_b[start] <= iv_a[end]
        ):
            result.append([max(iv_a[start], iv_b[start]), min(iv_a[end], iv_b[end])])

        if iv_a[end] == iv_b[end]:
            index_a += 1
            index_b += 1
        elif iv_a[end] < iv_b[end]:
            index_a += 1
        else:
            index_b += 1
    return result


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to merge_intervals
    print(merge_intervals([]))
