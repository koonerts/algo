"""
Traversal

"""


def preorderTraversal(root: TreeNode) -> list[int]:
    out = []
    self.recurse(root, out, TraversalType.PREORDER)
    return out


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to preorderTraversal
    print(preorderTraversal([]))
