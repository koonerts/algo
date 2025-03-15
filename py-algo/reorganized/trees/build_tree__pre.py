"""
Tree_Pre

Given inorder and preorder traversal of a tree, construct the binary tree.
Note: You may assume that duplicates do not exist in the tree.

Ex:
inorder = [9,3,15,20,7]
preorder = [3,9,20,15,7]
Return the following binary tree:
    3
   / \
  9  20
    /  \
   15   7
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree_Pre(inorder: List[int], preorder: List[int]) -> Optional[TreeNode]:
    """
    Given inorder and preorder traversal of a tree, construct the binary tree.
    Note: You may assume that duplicates do not exist in the tree.

    Ex:
    inorder = [9,3,15,20,7]
    preorder = [3,9,20,15,7]
    Return the following binary tree:
        3
       / \
      9  20
        /  \
       15   7
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


# Example usage
if __name__ == "__main__":
    # Create a sample tree
    inorder = [9, 3, 15, 20, 7]
    preorder = [3, 9, 20, 15, 7]
    tree = buildTree_Pre(inorder, preorder)

    # Print the tree structure
    def print_tree(node, level=0):
        if node:
            print("  " * level + str(node.val))
            print_tree(node.left, level + 1)
            print_tree(node.right, level + 1)

    print_tree(tree)
