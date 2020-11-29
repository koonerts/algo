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
        heappush(min_heap, (lists[i], i, 0))

    iterated_list_cnt = 0
    while iterated_list_cnt < len(lists):
        num, list_index, index = min_heap[0], min_heap[1], min_heap[2]

    number = -1
    return number


def main():
    print("Kth smallest number is: " +
          str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5)))


main()


