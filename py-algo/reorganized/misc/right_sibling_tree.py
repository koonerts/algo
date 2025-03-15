"""
Sibling Tree

"""

from collections import deque


def rightSiblingTree(root):
    if not root:
        return root

    q = deque([root.left, root.right])

    while q:
        prev = None
        q_len = len(q)
        for i in range(q_len):
            left, right = q.popleft()
            pass


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to rightSiblingTree
    print(rightSiblingTree([]))
