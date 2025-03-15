"""
Preorder_traverse_iterative

"""


def preorder_traverse_iterative(root: TreeNode) -> list[int]:
    out = []
    if root is None:
        return out

    stack = [root]
    while len(stack) > 0:
        node = stack.pop()
        out.append(node.val)

        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)

    return out


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to preorder_traverse_iterative
    print(preorder_traverse_iterative([]))
