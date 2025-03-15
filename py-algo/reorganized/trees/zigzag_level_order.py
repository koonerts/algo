"""
Level Order

"""

from collections import deque


def zigzagLevelOrder(root: TreeNode) -> list[list[int]]:
    if not root:
        return []

    direction = 1  # 1 left->right, -1 right->left
    result = []
    q = deque([root])

    while q:
        level_result = deque([])
        for _ in range(len(q)):
            node = q.popleft()

            if direction == 1:
                level_result.append(node.val)
            else:
                level_result.appendleft(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(list(level_result))
        direction *= -1
    return result


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to zigzagLevelOrder
    print(zigzagLevelOrder([]))
