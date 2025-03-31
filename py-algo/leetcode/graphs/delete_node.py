"""
Node

"""


def deleteNode(root: TreeNode, key: int) -> TreeNode:
    if not root or root.val == key:
        return None

    node = root
    prev = None
    while node:
        if node.val > key:
            prev = node
            node = node.left
        elif node.val < key:
            prev = node
            node = node.right


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to deleteNode
    print(deleteNode([]))
