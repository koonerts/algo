"""
Find_path

Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
"""
def find_path(root: TreeNode, sequence: list[int]):
    """
    Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.
    """
def dfs(node: TreeNode, path) -> bool:
        if not node: return False
        if not node.left and not node.right:
            return path + [node.val] == sequence
        else:
            return dfs(node.left, path + [node.val]) or dfs(node.right, path + [node.val])

    return dfs(root, [])


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_path
    print(find_path([]))
