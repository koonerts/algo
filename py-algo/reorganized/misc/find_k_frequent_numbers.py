"""
Find_k_frequent_numbers

Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

    Example 1:
    Input: [1, 3, 5, 12, 11, 12, 11], K = 2
    Output: [12, 11]
    Explanation: Both '11' and '12' appeared twice.

    Example 2:
    Input: [5, 12, 11, 3, 11], K = 2
    Output: [11, 5] or [11, 12] or [11, 3]
    Explanation: Only '11' appeared twice, all other numbers appeared once.
"""


def find_k_frequent_numbers(nums, k):
    """
    Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

    Example 1:
    Input: [1, 3, 5, 12, 11, 12, 11], K = 2
    Output: [12, 11]
    Explanation: Both '11' and '12' appeared twice.

    Example 2:
    Input: [5, 12, 11, 3, 11], K = 2
    Output: [11, 5] or [11, 12] or [11, 3]
    Explanation: Only '11' appeared twice, all other numbers appeared once.
    """
    freq_map = {}
    heap = []

    for num in nums:
        if num not in freq_map:
            freq_map[num] = 1
        else:
            freq_map[num] += 1

    for num, freq in freq_map.items():
        if len(heap) < k:
            heappush(heap, (freq, num))
        elif freq > heap[0][0]:
            heappushpop(heap, (freq, num))

    return [item[1] for item in heap]


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_k_frequent_numbers
    print(find_k_frequent_numbers([]))
