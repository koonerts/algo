"""
Reorder

Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the
    nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order.
    So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
    Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

    Example 1:
    Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
    Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null

    Example 2:
    Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
    Output: 2 -> 10 -> 4 -> 8 -> 6 -> null
"""


def reorder(head: Node):
    """
    Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the
    nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order.
    So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
    Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

    Example 1:
    Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
    Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null

    Example 2:
    Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
    Output: 2 -> 10 -> 4 -> 8 -> 6 -> null
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    end_to_mid = reverse_ll(slow)

    cntr = 0
    start = head
    while start.next:
        if cntr % 2 == 0:
            if start:
                next_start = start.next
                start.next = end_to_mid
                start = next_start
        else:
            if start:
                next_end_to_mid = end_to_mid.next
                end_to_mid.next = start
                end_to_mid = next_end_to_mid
            else:
                break
        cntr += 1

    return


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to reorder
    print(reorder([]))
