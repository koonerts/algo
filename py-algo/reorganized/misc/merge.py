"""
Merge

Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

    Example 1:
    Intervals: [[1,4], [2,5], [7,9]]
    Output: [[1,5], [7,9]]
    Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].

    Example 2:
    Intervals: [[6,7], [2,4], [5,9]]
    Output: [[2,4], [5,9]]
    Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

    Example 3:
    Intervals: [[1,4], [2,6], [3,5]]
    Output: [[1,6]]
    Explanation: Since all the given intervals overlap, we merged them into one.
"""


def merge(intervals: list[Interval]) -> list[Interval]:
    """
    Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

    Example 1:
    Intervals: [[1,4], [2,5], [7,9]]
    Output: [[1,5], [7,9]]
    Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into one [1,5].

    Example 2:
    Intervals: [[6,7], [2,4], [5,9]]
    Output: [[2,4], [5,9]]
    Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

    Example 3:
    Intervals: [[1,4], [2,6], [3,5]]
    Output: [[1,6]]
    Explanation: Since all the given intervals overlap, we merged them into one.
    """
    intervals.sort(key=lambda x: x.start)
    merged_intervals = []

    start = intervals[0].start
    end = intervals[0].end
    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:  # overlapping intervals, adjust the 'end'
            end = max(interval.end, end)
        else:  # non-overlapping interval, add the previous interval and reset
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end

    # add the last interval
    merged_intervals.append(Interval(start, end))
    return merged_intervals


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to merge
    print(merge([]))
