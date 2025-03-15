"""
Traverse_using_queue

Given a binary tree, populate an array to represent its level-by-level traversal by using a queue.
    You should populate the values of all nodes of each level from left to right in separate sub-arrays.
"""


from collections import deque
def traverse_using_queue(root: TreeNode) -> list[list[int]]:
    """
    Given a binary tree, populate an array to represent its level-by-level traversal by using a queue.
    You should populate the values of all nodes of each level from left to right in separate sub-arrays.
    """
    if not root: return []
    result = []
    q = deque([root])

    while q:
        level_size = len(q)
        level_result = []

        while level_size > 0:
            node = q.popleft()
            level_result.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            level_size -= 1

        result.append(level_result)

    return result



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to traverse_using_queue
    print(traverse_using_queue([]))
