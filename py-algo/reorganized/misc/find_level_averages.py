"""
Find_level_averages

Given a binary tree, populate an array to represent the averages of all of its levels.
"""


from collections import deque
def find_level_averages(root: TreeNode):
    """
    Given a binary tree, populate an array to represent the averages of all of its levels.
    """
    if not root: return []
    result = []
    q = deque([root])

    while q:
        level_size = len(q)
        level_sum = 0

        for _ in range(level_size):
            node = q.popleft()
            level_sum += node.val
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

        result.append(level_sum/level_size)

    return result



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_level_averages
    print(find_level_averages([]))
