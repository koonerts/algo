"""
Find_minimum_depth

Find the minimum depth of a binary tree.
    The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
"""


from collections import deque
def find_minimum_depth(root: TreeNode) -> int:
    """
    Find the minimum depth of a binary tree.
    The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
    """
    if not root: return -1
    level = 1
    q = deque([root])
    while q:
        level_size = len(q)
        for _ in range(level_size):
            node = q.popleft()
            if not node.left and not node.right:
                return level
            else:
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
        level += 1



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_minimum_depth
    print(find_minimum_depth([]))
