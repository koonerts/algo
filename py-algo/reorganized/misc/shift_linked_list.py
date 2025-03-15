"""
Linked List

"""
def shiftLinkedList(head, k):
    ll_len = 0
    node = head
    while node:
        ll_len += 1
        node = node.next

    k %= ll_len
    if k == 0:
        return head

    node, prev = head, None
    for _ in range(ll_len - k):
        prev = node
        node = node.next
    new_head = node
    prev.next = None

    while node:
        if not node.next:
            node.next = head
            break
        node = node.next
    return new_head



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to shiftLinkedList
    print(shiftLinkedList([]))
