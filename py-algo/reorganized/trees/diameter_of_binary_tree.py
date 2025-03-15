"""
Of Binary Tree

"""
def diameterOfBinaryTree(root: TreeNode) -> int:
        if not root: return 0
def depth(node):
            nonlocal diameter
            if not node: return 0

            left = depth(node.left)
            right = depth(node.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1

        diameter = 0
        depth(root)
        return diameter


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to diameterOfBinaryTree
    print(diameterOfBinaryTree([]))
