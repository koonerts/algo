"""
Find_paths

"""
def find_paths(root: TreeNode, sum: int):
    all_paths = []
def dfs(node:TreeNode, curr_path: [], curr_sum: int):
        if not node: return
        curr_sum -= node.val
        curr_path.append(node.val)

        # is leaf
        if curr_sum == 0 and not (node.left and node.right):
            all_paths.append(list(curr_path))
        else:
            dfs(node.left, curr_path, curr_sum)
            dfs(node.right, curr_path, curr_sum)

        del curr_path[-1]

    dfs(root, [], sum)

    return all_paths


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_paths
    print(find_paths([]))
