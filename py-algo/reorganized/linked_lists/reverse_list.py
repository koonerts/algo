"""
List

"""


def reverseList(head: ListNode) -> ListNode:
    prev = None
    while head:
        head.next, prev, head = prev, head, head.next
    return prev


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to reverseList
    print(reverseList([]))
