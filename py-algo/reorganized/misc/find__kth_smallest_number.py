"""
Kth_smallest_number

Given an unsorted array of numbers, find Kth smallest number in it.
    Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

    Example 1:
    Input: [1, 5, 12, 2, 11, 5], K = 3
    Output: 5
    Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

    Example 2:
    Input: [1, 5, 12, 2, 11, 5], K = 4
    Output: 5
    Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].

    Example 3:
    Input: [5, 12, 11, -1, 12], K = 3
    Output: 11
    Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].
"""
def find_Kth_smallest_number(nums, k):
    """
    Given an unsorted array of numbers, find Kth smallest number in it.
    Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

    Example 1:
    Input: [1, 5, 12, 2, 11, 5], K = 3
    Output: 5
    Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

    Example 2:
    Input: [1, 5, 12, 2, 11, 5], K = 4
    Output: 5
    Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].

    Example 3:
    Input: [5, 12, 11, -1, 12], K = 3
    Output: 11
    Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].
    """
    min_heap = []
    for num in nums:
        if len(min_heap) < k:
            heappush(min_heap, num)
        elif num > min_heap[0]:
            heappushpop(min_heap, num)
    return min_heap[0]



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_Kth_smallest_number
    print(find_Kth_smallest_number([]))
