"""
Reverse_alternate_k_elements

Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.
    If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

    Ex:
    Input: 1->2->3->4->5->6->7->8->None, k = 2
    Output: 2->1->3->4->6->5->7->8->None
"""
def reverse_alternate_k_elements(head: Node, k: int) -> Node:
    """
    Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.
    If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.

    Ex:
    Input: 1->2->3->4->5->6->7->8->None, k = 2
    Output: 2->1->3->4->6->5->7->8->None
    """
    node, prev, sublist_tail, non_reverse_tail = head, None, head, None
    k_cntr, should_reverse, is_head_set = k, True, False

    while node:
        if should_reverse:
            node.next, prev, node = prev, node, node.next
            k_cntr -= 1

            if k_cntr == 0 or not node:
                if not is_head_set:
                    head = prev
                    is_head_set = True

                if non_reverse_tail:
                    non_reverse_tail.next = prev

                if sublist_tail:
                    sublist_tail.next = node

                prev = None
        else:
            node = node.next
            k_cntr -= 1
            if k_cntr > 0:
                non_reverse_tail = node
            else:
                sublist_tail = node

        if k_cntr == 0:
            should_reverse = not should_reverse
            k_cntr = k

    return head



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to reverse_alternate_k_elements
    print(reverse_alternate_k_elements([]))
