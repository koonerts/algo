"""
Serialize

Encodes a tree to a single string.
"""

import json
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    Performs an inorder traversal of the tree and returns the values.
    """
    result = []

    def traverse(node):
        if node:
            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

    traverse(root)
    return result


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    Performs a preorder traversal of the tree and returns the values.
    """
    result = []

    def traverse(node):
        if node:
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)

    traverse(root)
    return result


def serialize(root: Optional[TreeNode]) -> str:
    """
    Encodes a tree to a single string.
    """
    if not root:
        return ""

    inorder = inorderTraversal(root)
    preorder = preorderTraversal(root)
    return json.dumps({"inorder": inorder, "preorder": preorder})


# Example usage
if __name__ == "__main__":
    # Create a sample tree
    #     3
    #    / \
    #   9  20
    #     /  \
    #    15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    # Serialize the tree
    serialized = serialize(root)
    print(f"Serialized tree: {serialized}")
