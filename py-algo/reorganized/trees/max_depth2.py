"""
Depth2

"""

from max_depth import TreeNode

def maxDepth2(root: TreeNode) -> int:
    if not root:
        return 0
    left_depth = maxDepth2(root.left)
    right_depth = maxDepth2(root.right)
    return max(left_depth, right_depth) + 1


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to maxDepth2
    # Create a binary tree: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(maxDepth2(root))  # Output: 3
