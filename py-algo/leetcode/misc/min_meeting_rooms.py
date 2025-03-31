"""
Min_meeting_rooms

"""

from heapq import *


def min_meeting_rooms(meetings: list[Meeting]):
    if not meetings:
        return 0

    max_rooms = 0
    meetings.sort(key=lambda x: x.start)
    end_times = []

    for meeting in meetings:
        while end_times and end_times[0] <= meeting.start:
            heapq.heappop(end_times)

        heapq.heappush(end_times, meeting.end)
        max_rooms = max(max_rooms, len(end_times))
    return max_rooms


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to min_meeting_rooms
    print(min_meeting_rooms([]))
