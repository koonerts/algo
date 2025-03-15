from heapq import *


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value


def merge_lists(lists: list[ListNode]):
    """
    Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

    Example 1:
    Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
    Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]

    Example 2:
    Input: L1=[5, 8, 9], L2=[1, 7]
    Output: [1, 5, 7, 8, 9]
    """
    min_heap = []

    for i in range(len(lists)):
        heappush(min_heap, lists[i])

    result_head, curr, prev = None, None, None
    while min_heap:
        curr = heappop(min_heap)

        if not result_head:
            result_head = curr

        if prev:
            prev.next = curr

        if curr.next:
            heappush(min_heap, curr.next)

        prev = curr

    return result_head


def find_Kth_smallest(lists, k):
    """
    Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

    Example 1:
    Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
    Output: 4
    Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged
    list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]

    Example 2:
    Input: L1=[5, 8, 9], L2=[1, 7], K=3
    Output: 7
    Explanation: The 3rd smallest number among all the arrays is 7.
    """
    min_heap = []

    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], i, 1))

    num_count = 0
    while min_heap:
        num, list_index, next_index = heappop(min_heap)
        num_count += 1

        if num_count == k:
            return num
        elif next_index < len(lists[list_index]):
            heappush(
                min_heap, (lists[list_index][next_index], list_index, next_index + 1)
            )


def find_Kth_smallest(matrix: list[list[int]], k: int):
    """
    Given an N * NN∗N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

    Example 1:
    Input: Matrix=[
        [2, 6, 8],
        [3, 7, 10],
        [5, 8, 11]
      ],
      K=5
    Output: 7
    Explanation: The 5th smallest number in the matrix is 7.
    """
    # TODO: Come back to (same answer as above.. or can be improved by doing a complex 2d binary search)
    number = -1
    return number


def find_smallest_range(lists):
    """
    Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.

    Example 1:
    Input: L1=[1, 5, 8], L2=[4, 12], L3=[7, 8, 10]
    Output: [4, 7]
    Explanation: The range [4, 7] includes 5 from L1, 4 from L2 and 7 from L3.

    Example 2:
    Input: L1=[1, 9], L2=[4, 12], L3=[7, 10, 16]
    Output: [9, 12]
    Explanation: The range [9, 12] includes 9 from L1, 12 from L2 and 10 from L3.
    """
    # TODO: Come back to
    return [-1, -1]


def find_k_largest_pairs(nums1, nums2, k):
    """
    Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair consists of numbers from both the arrays.

    Example 1:
    Input: L1=[9, 8, 2], L2=[6, 3, 1], K=3
    Output: [9, 3], [9, 6], [8, 6]
    Explanation: These 3 pairs have the largest sum. No other pair has a sum larger than any of these.

    Example 2:
    Input: L1=[5, 2, 1], L2=[2, -1], K=3
    Output: [5, 2], [5, -1], [2, 2]
    """
    # TODO: come back to
    result = []
    return result
