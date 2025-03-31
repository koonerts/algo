"""
Subtract

"""


def subtract(head: ListNode) -> ListNode:
    lo, hi = 0, 0
    last = head
    while last and last.next:
        last = last.next
        hi += 1

    n = hi - lo + 1
    # 1->2->3->4->5
    node = head
    lo, mid = 0, n // 2
    while lo <= mid:
        node = node.next
        lo += 1

    prev = None
    while node:
        temp = node.next
        node.next = prev
        prev = node
        node = temp

    left, right = head, prev
    while node:
        left.val = right.val - left.val
        if left.next:
            left = left.next
        right = right.next

    node = prev
    prev = None
    while node:
        temp = node.next
        node.next = prev
        prev = node
        node = temp
    left.next = prev
    return head


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to subtract
    print(subtract([]))
