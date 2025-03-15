"""
Meeting Rooms

"""


def minMeetingRooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    elif len(intervals) == 1:
        return 1

    start, end = 0, 1
    intervals.sort(key=lambda x: x[start])

    max_concurrent_meetings = 0
    min_end_times = []

    for iv in intervals:
        if not min_end_times:
            heappush(min_end_times, iv[end])
        else:
            while min_end_times and min_end_times[0] <= iv[start]:
                heappop(min_end_times)
            heappush(min_end_times, iv[end])
        max_concurrent_meetings = max(max_concurrent_meetings, len(min_end_times))
    return max_concurrent_meetings


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to minMeetingRooms
    print(minMeetingRooms([]))
