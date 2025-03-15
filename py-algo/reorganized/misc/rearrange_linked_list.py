"""
Linked List

"""
def rearrangeLinkedList(head, k):
    low_head, low_tail, k_head, k_tail, hi_head, hi_tail = None, None, None, None, None, None
    node = head
    while node:
        if node.value < k:
            if not low_head:
                low_head, low_tail = node, node
            else:
                low_tail.next = node
                low_tail = low_tail.next
        elif node.value > k:
            if not hi_head:
                hi_head, hi_tail = node, node
            else:
                hi_tail.next = node
                hi_tail = hi_tail.next
        else:
            if not k_head:
                k_head, k_tail = node, node
            else:
                k_tail.next = node
                k_tail = k_tail.next
        node = node.next

    new_head = low_head or k_head or hi_head
    if low_tail:
        if k_head:
            low_tail.next = k_head
        else:
            low_tail.next = hi_head
    if k_tail:
        k_tail.next = hi_head
    if hi_tail:
        hi_tail.next = None
    return new_head



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to rearrangeLinkedList
    print(rearrangeLinkedList([]))
