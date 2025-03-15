"""
Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3
    
Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree (for recursion stack)
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def __init__(self, val=0, left=None, right=None) -> None:
    """
Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Args:
    root (Optional[TreeNode]): Root of the binary tree
    
Returns:
    int: The maximum depth of the tree
    
Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(h) where h is the height of the tree (for recursion stack)
"""
    self.val = val
    self.left = left
    self.right = right




# Example usage
if __name__ == "__main__":
    # Create a binary tree: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    print(maxDepth(root))  # Output: 3
