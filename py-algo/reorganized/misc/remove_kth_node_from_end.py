"""
Kth Node From End

"""
def removeKthNodeFromEnd(head: LinkedList, k):
    k_ahead = head
    for _ in range(k):
        k_ahead = k_ahead.next

    node, prev = head, None
    while k_ahead:
        prev = node
        node = node.next
        k_ahead = k_ahead.next

    if prev:
        prev.next = node.next
    else:
        node = head
        while node:
            node.value = node.next.value
            if not node.next.next.next:
                node.next = None
                node = None
                break
            node = node.next



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to removeKthNodeFromEnd
    print(removeKthNodeFromEnd([]))
