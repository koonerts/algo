"""
Max_depth_recurse

A recursive function to find the maximum depth of a binary tree.
This implementation tracks the current depth during traversal.
"""

from typing import Optional
from max_depth import TreeNode


def max_depth_recurse(curr_depth: int, node: Optional[TreeNode]) -> int:
    """
    Calculate the maximum depth of a binary tree starting from a given depth.

    Args:
        curr_depth (int): The current depth in the traversal
        node (Optional[TreeNode]): The current node being processed

    Returns:
        int: The maximum depth found in the tree
    """
    if not node:
        return curr_depth

    l_depth, r_depth = curr_depth, curr_depth
    if node.left:
        l_depth = max_depth_recurse(curr_depth + 1, node.left)
    if node.right:
        r_depth = max_depth_recurse(curr_depth + 1, node.right)
    return max(l_depth, r_depth)


# Example usage
if __name__ == "__main__":
    # Create a binary tree: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(max_depth_recurse(0, root))  # Output: 3
