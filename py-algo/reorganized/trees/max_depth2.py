"""
Depth2

"""
def maxDepth2(root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth2(root.left)
        right_depth = self.maxDepth2(root.right)
        return max(left_depth, right_depth) + 1


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to maxDepth2
    print(maxDepth2([]))
