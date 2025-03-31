"""
Binary Tree Preorder Traversal

Given the root of a binary tree, return the preorder traversal of its nodes' values.

Example:
    Input: root = [1,null,2,3]
    Output: [1,2,3]

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(n) for the output list and recursion stack
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: Optional[TreeNode]) -> List[int]:
    """
    Given the root of a binary tree, return the preorder traversal of its nodes' values.

    Args:
        root (Optional[TreeNode]): Root of the binary tree

    Returns:
        List[int]: The preorder traversal of the tree's values

    Time Complexity: O(n) where n is the number of nodes in the tree
    Space Complexity: O(n) for the output list and recursion stack
    """
    result = []

    def traverse(node):
        if node:
            result.append(node.val)
            traverse(node.left)
            traverse(node.right)

    traverse(root)
    return result


# Example usage
if __name__ == "__main__":
    # Create a binary tree: [1,null,2,3]
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)

    print(preorderTraversal(root))  # Output: [1, 2, 3]
