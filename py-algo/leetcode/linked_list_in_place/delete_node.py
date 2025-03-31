"""
Node

:type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
"""


def deleteNode(node):
    """
    :type node: ListNode
    :rtype: void Do not return anything, modify node in-place instead.
    """
    prev = node
    curr = node.next
    while curr:
        prev.val = curr.val

        if not curr.next:
            prev.next = None
            break

        prev = curr
        curr = curr.next


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to deleteNode
    print(deleteNode([]))
