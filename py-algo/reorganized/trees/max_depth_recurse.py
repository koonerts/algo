"""
Max_depth_recurse

"""


def max_depth_recurse(curr_depth: int, node: TreeNode) -> int:
    if not node:
        return curr_depth

    l_depth, r_depth = curr_depth, curr_depth
    if node.left:
        l_depth = self.max_depth_recurse(l_depth + 1, node.left)
    if node.right:
        r_depth = self.max_depth_recurse(r_depth + 1, node.right)
    return max(curr_depth, l_depth, r_depth)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to max_depth_recurse
    print(max_depth_recurse([]))
