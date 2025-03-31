"""
Sorted Arrays

"""


def mergeSortedArrays(arrays):
    min_heap = []
    for i in range(len(arrays)):
        min_heap.append((arrays[i][0], 0, i))
    heapify(min_heap)

    result = []
    while min_heap:
        num, idx, list_id = heappop(min_heap)
        result.append(num)

        if idx < len(arrays[list_id]) - 1:
            heappush(min_heap, (arrays[list_id][idx + 1], idx + 1, list_id))
    return result


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to mergeSortedArrays
    print(mergeSortedArrays([]))
