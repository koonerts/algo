"""
Connect_all_siblings

Given a binary tree, connect each node with its level order successor.
    The last node of each level should point to the first node of the next level.
"""

from collections import deque


def connect_all_siblings(root: TreeNode):
    """
    Given a binary tree, connect each node with its level order successor.
    The last node of each level should point to the first node of the next level.
    """
    if not root:
        return root
    q = deque([root])

    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if q:
                node.next = q[0]
    return


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to connect_all_siblings
    print(connect_all_siblings([]))
