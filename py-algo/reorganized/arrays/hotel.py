"""
Hotel

"""


def hotel(arrive, depart, K):
    if K == 0:
        return False

    n = len(arrive)
    intervals = []
    for i in range(n):
        if arrive[i] == depart[i]:
            continue
        intervals.append([arrive[i], depart[i]])
    intervals.sort(key=lambda interval: (interval[0], interval[1]))
    print(intervals)
    heap = []
    for i in range(len(intervals)):
        while heap and heap[0] < intervals[i][0]:
            heappop(heap)

        if len(heap) == K:
            return False

        heappush(heap, intervals[i][1])
    return True


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to hotel
    print(hotel([]))
