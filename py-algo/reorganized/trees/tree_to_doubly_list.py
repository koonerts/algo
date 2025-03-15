"""
To Doubly List
Convert a binary search tree to a sorted circular doubly linked list.
"""


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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
    # Create a sample BST
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    # Convert to doubly linked list
    head = treeToDoublyList(root)

    # Print the linked list (will stop after one cycle)
    if head:
        current = head
        print(current.val, end=" ")
        current = current.right
        while current != head:
            print(current.val, end=" ")
            current = current.right
        print()  # Final newline
