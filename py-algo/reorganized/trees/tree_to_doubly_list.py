"""
To Doubly List

"""


def treeToDoublyList(root: Node) -> Node:
    if not root:
        return root
    stk = []
    node = root

    head, tail, prev = None, None, None
    while stk or node:
        while node:
            stk.append(node)
            node = node.left

        node = stk.pop()
        if not head:
            head = node

        if not node.right and not stk:
            tail = node

        node.left = prev
        if prev:
            prev.right = node
        prev = node
        node = node.right

    head.left = tail
    tail.right = head
    return head


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to treeToDoublyList
    print(treeToDoublyList([]))
