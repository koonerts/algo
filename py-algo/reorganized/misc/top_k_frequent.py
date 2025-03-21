"""
K Frequent

"""


def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq_map = {}
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    min_heap = []
    for num in freq_map:
        if len(min_heap) < k:
            heappush(min_heap, (freq_map[num], num))
        elif freq_map[num] > min_heap[0][0]:
            heappushpop(min_heap, (freq_map[num], num))
    return [item[1] for item in min_heap]


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to topKFrequent
    print(topKFrequent([]))
