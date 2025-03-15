"""
Zigzag_traverse

Given a binary tree, populate an array to represent its level-by-level traversal by using a queue.
    You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""


from collections import deque
def zigzag_traverse(root: TreeNode) -> list[list[int]]:
    """
    Given a binary tree, populate an array to represent its level-by-level traversal by using a queue.
    You should populate the values of all nodes of each level from left to right in separate sub-arrays.
    """
    if not root: return []
    result = []
    q = deque([root])
    forward = True

    while q:
        level_size = len(q)
        level_result = deque()

        while level_size > 0:
            node = q.popleft()
            if forward:
                level_result.append(node.val)
            else:
                level_result.appendleft(node.val)

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            level_size -= 1

        result.append(list(level_result))
        forward = not forward

    return result



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to zigzag_traverse
    print(zigzag_traverse([]))
