"""
Deserialize

Decodes your encoded data to tree.
"""
import json
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree_Pre(inorder: list[int], preorder: list[int]) -> Optional[TreeNode]:
    """
    Given inorder and preorder traversal of a tree, construct the binary tree.
    Note: You may assume that duplicates do not exist in the tree.
    """
    if not inorder or not preorder:
        return None

    def build(bound=None):
        if not inorder or inorder[0] == bound:
            return None
        root = TreeNode(preorder.pop(0))
        root.left = build(root.val)
        inorder.pop(0)
        root.right = build(bound)
        return root

    return build()


def deserialize(data: str) -> Optional[TreeNode]:
    """
    Decodes your encoded data to tree.
    """
    if not data:
        return None

    try:
        parsed_data = json.loads(data)
        if isinstance(parsed_data, dict) and "inorder" in parsed_data and "preorder" in parsed_data:
            return buildTree_Pre(parsed_data["inorder"], parsed_data["preorder"])
        return None
    except json.JSONDecodeError:
        return None


# Example usage
if __name__ == "__main__":
    # Example: Create a serialized tree representation
    serialized_tree = json.dumps({"inorder": [9, 3, 15, 20, 7], "preorder": [3, 9, 20, 15, 7]})

    # Deserialize it back to a tree
    tree = deserialize(serialized_tree)

    # Print the tree structure (simple representation)
    def print_tree(node, level=0):
        if node:
            print("  " * level + str(node.val))
            print_tree(node.left, level + 1)
            print_tree(node.right, level + 1)

    print_tree(tree)
