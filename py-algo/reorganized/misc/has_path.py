"""
Has_path

"""
def has_path(root: TreeNode, sum: int) -> bool:
def dfs(node:TreeNode, curr_sum: int):
        if not node: return False
        curr_sum -= node.val

        # is leaf
        if not (node.left and node.right):
            if curr_sum == 0:
                return True
            else:
                return False
        else:
            return dfs(node.left, curr_sum) or dfs(node.right, curr_sum)

    return dfs(root, sum)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to has_path
    print(has_path([]))
