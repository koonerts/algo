"""
Merge_lists

Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

    Example 1:
    Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
    Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]

    Example 2:
    Input: L1=[5, 8, 9], L2=[1, 7]
    Output: [1, 5, 7, 8, 9]
"""


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


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to merge_lists
    print(merge_lists([]))
