"""
Connect_level_order_siblings

"""

from collections import deque


def connect_level_order_siblings(root: TreeNode):
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
            if i != level_size - 1:
                node.next = q[0]
    return


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to connect_level_order_siblings
    print(connect_level_order_siblings([]))
