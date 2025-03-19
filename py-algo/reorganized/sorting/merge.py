"""
Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
    
Time Complexity: O(n log n) due to sorting, where n is the number of intervals
Space Complexity: O(n) for the result array
"""


def merge(intervals: list[list[int]]) -> list[list[int]]:
    """
    Merge overlapping intervals.

    Args:
        intervals (List[List[int]]): List of intervals where each interval is [start, end]

    Returns:
        List[List[int]]: Merged non-overlapping intervals

    Time Complexity: O(n log n) due to sorting, where n is the number of intervals
    Space Complexity: O(n) for the result array
    """
    if not intervals:
        return []

    # Sort intervals by start time
    start, end = 0, 1
    intervals.sort(key=lambda x: x[start])

    prev = intervals[0]
    result = [prev]

    for i in range(1, len(intervals)):
        curr = intervals[i]
        # If current interval's start is after previous interval's end, add it as a new interval
        if prev[end] < curr[start]:
            result.append(curr)
            prev = curr
        # Otherwise merge the intervals by taking the maximum end time
        else:
            prev[end] = max(prev[end], curr[end])

    return result


# Example usage
if __name__ == "__main__":
    test_cases = [
        # Output: [[1, 6], [8, 10], [15, 18]]
        [[1, 3], [2, 6], [8, 10], [15, 18]],
        [[1, 4], [4, 5]],                      # Output: [[1, 5]]
        [[1, 4], [0, 4]],                      # Output: [[0, 4]]
        [[1, 4], [2, 3]],                      # Output: [[1, 4]]
    ]

    for intervals in test_cases:
        print(f"Input: {intervals}")
        result = merge(intervals)
        print(f"Output: {result}")
        print()
