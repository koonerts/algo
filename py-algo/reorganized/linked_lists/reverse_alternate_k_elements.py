"""
Reverse_alternate_k_elements

Given the head of a LinkedList and a number 'k', reverse every alternating 'k' sized sub-list starting from the head.
    If, in the end, you are left with a sub-list with less than 'k' elements, reverse it too.

    Ex:
    Input: 1->2->3->4->5->6->7->8->None, k = 2
    Output: 2->1->3->4->6->5->7->8->None
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def __str__(self):
        result = []
        current = self
        while current:
            result.append(str(current.value))
            current = current.next
        return "->".join(result) + "->None"


def reverse_alternate_k_elements(head: Node, k: int) -> Node:
    """
    Given the head of a LinkedList and a number 'k', reverse every alternating 'k' sized sub-list starting from the head.
    If, in the end, you are left with a sub-list with less than 'k' elements, reverse it too.

    Ex:
    Input: 1->2->3->4->5->6->7->8->None, k = 2
    Output: 2->1->3->4->6->5->7->8->None
    """
    if not head or k <= 1:
        return head
        
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
    # Create linked list: 1->2->3->4->5->6->7->8->None
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    
    print("Original:", head)
    result = reverse_alternate_k_elements(head, 2)
    print("After reversing alternate k elements:", result)