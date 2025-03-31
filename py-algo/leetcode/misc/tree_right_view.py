"""
Tree_right_view

Returns the rightmost node values at each level of a binary tree.
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    """Binary tree node class."""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def tree_right_view(root: Optional[TreeNode]) -> List[int]:
    """
    Returns a list of values from the rightmost nodes at each level of the tree.

    Args:
        root: The root node of the binary tree

    Returns:
        A list of values from the rightmost nodes at each level
    """
    if not root:
        return []
    result = []
    q = deque([root])

    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if i == level_size - 1:
                result.append(node.val)  # Append the value, not the node
    return result


# Example usage
if __name__ == "__main__":
    # Create a sample tree:
    #       1
    #      / \
    #     2   3
    #    /     \
    #   4       5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)

    # Expected output: [1, 3, 5]
    print(tree_right_view(root))
