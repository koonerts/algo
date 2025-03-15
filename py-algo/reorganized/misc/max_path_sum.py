"""
Path Sum

"""
def maxPathSum(tree):
    if not tree: return 0
    elif not tree.left and not tree.right: return tree.value
def dfs_sum(node):
        nonlocal max_path_sum
        if not node:
            return 0
        else:
            l_sum = dfs_sum(node.left)
            r_sum = dfs_sum(node.right)

            max_path_sum = max(max_path_sum, l_sum + r_sum + node.value, l_sum + node.value, r_sum + node.value)
            return max(l_sum, r_sum) + node.value

    max_path_sum = float('-inf')
    dfs_sum(tree)
    return max_path_sum



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to maxPathSum
    print(maxPathSum([]))
