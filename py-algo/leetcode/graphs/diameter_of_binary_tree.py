"""
Of Binary Tree

"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def diameterOfBinaryTree(root: TreeNode) -> int:
    diameter = 0

    def depth(node):
        nonlocal diameter
        if not node:
            return 0

        left = depth(node.left)
        right = depth(node.right)
        diameter = max(diameter, left + right)
        return max(left, right) + 1

    depth(root)
    return diameter


# Example usage
if __name__ == "__main__":
    # Example calls to diameterOfBinaryTree
    # Assuming TreeNode creation and linking is done elsewhere
    # For demonstration, let's create a simple binary tree
    #     1
    #    / \
    #   2   3
    #  / \
    # 4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    print(diameterOfBinaryTree(root))  # Expected output: 3
