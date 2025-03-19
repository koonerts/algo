"""
Validate Binary Search Tree

Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows: The left subtree of a node contains only nodes with keys less than the node's key. The right subtree of a node contains only nodes with keys greater than the node's key. Both the left and right subtrees must also be binary search trees.

Example:
    Input: root = [2,1,3]
    Output: true

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree (for recursion stack)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root):
    """
    Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows: The left subtree of a node contains only nodes with keys less than the node's key. The right subtree of a node contains only nodes with keys greater than the node's key. Both the left and right subtrees must also be binary search trees.

    Args:
        root (Optional[TreeNode]): Root of the binary tree

    Returns:
        bool: True if the tree is a valid BST, False otherwise

    Time Complexity: O(n) where n is the number of nodes in the tree
    Space Complexity: O(h) where h is the height of the tree (for recursion stack)
    """
    def validate(node, lower=float('-inf'), upper=float('inf')):
        if not node:
            return True

        if node.val <= lower or node.val >= upper:
            return False

        return validate(node.left, lower, node.val) and validate(node.right, node.val, upper)

    return validate(root)


# Example usage
if __name__ == "__main__":
    # Create a valid BST: [2,1,3]
    valid_bst = TreeNode(2)
    valid_bst.left = TreeNode(1)
    valid_bst.right = TreeNode(3)

    # Create an invalid BST: [5,1,4,null,null,3,6]
    invalid_bst = TreeNode(5)
    invalid_bst.left = TreeNode(1)
    invalid_bst.right = TreeNode(4)
    invalid_bst.right.left = TreeNode(3)
    invalid_bst.right.right = TreeNode(6)

    print(isValidBST(valid_bst))  # Output: True
    print(isValidBST(invalid_bst))  # Output: False
