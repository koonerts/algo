"""
Connect

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
        Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
        Initially, all next pointers are set to NULL.

        Ex: Input: root = [1,2,3,4,5,6,7]
            Output: [1,#,2,3,#,4,5,6,7,#]
            Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node.
                         The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
"""

import collections


def connect(root: Node) -> Node:
    """
    You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
    Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
    Initially, all next pointers are set to NULL.

    Ex: Input: root = [1,2,3,4,5,6,7]
        Output: [1,#,2,3,#,4,5,6,7,#]
        Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node.
                     The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
    """
    if not root:
        return root

    q = collections.deque([root])
    while q:
        length = len(q)
        for i in range(length):
            node = q.popleft()
            if i < length - 1:
                node.next = q[0]

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return root


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to connect
    print(connect([]))
