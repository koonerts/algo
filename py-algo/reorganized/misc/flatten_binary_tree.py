"""
Binary Tree

"""


def flattenBinaryTree(root):
    head, stk = None, []
    node, prev = root, None
    while stk or node:
        while node:
            stk.append(node)
            node = node.left

        node = stk.pop()
        if not head:
            head = node

        if prev:
            prev.right = node
            node.left = prev
        prev = node
        node = node.right
    return head


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to flattenBinaryTree
    print(flattenBinaryTree([]))
