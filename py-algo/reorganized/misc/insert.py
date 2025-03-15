"""
Insert

Given a list of non-overlapping intervals sorted by their start time, insert a given interval at
    the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

    Example 1:
    Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
    Output: [[1,3], [4,7], [8,12]]
    Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

    Example 2:
    Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
    Output: [[1,3], [4,12]]
    Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

    Example 3:
    Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
    Output: [[1,4], [5,7]]
    Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""


def insert(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    """
    Given a list of non-overlapping intervals sorted by their start time, insert a given interval at
    the correct position and merge all necessary intervals to produce a list that has only mutually exclusive intervals.

    Example 1:
    Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
    Output: [[1,3], [4,7], [8,12]]
    Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

    Example 2:
    Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
    Output: [[1,3], [4,12]]
    Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

    Example 3:
    Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
    Output: [[1,4], [5,7]]
    Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
    """
    merged_intervals = []
    start, end = 0, 1
    inserted = False

    for interval in intervals:
        if interval[end] < new_interval[start]:
            merged_intervals.append(interval)
        elif interval[start] > new_interval[end]:
            if not inserted:
                merged_intervals.append(new_interval)
                inserted = True
            merged_intervals.append(interval)
        else:
            new_interval[end] = max(new_interval[end], interval[end])

    if not inserted:
        merged_intervals.append(new_interval)

    return merged_intervals


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to insert
    print(insert([]))
