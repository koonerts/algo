"""
Find_successor

Given a binary tree and a node, find the level order successor of the given node in the tree.
    The level order successor is the node that appears right after the given node in the level order traversal.
"""


from collections import deque
def find_successor(root: TreeNode, key: int):
    """
    Given a binary tree and a node, find the level order successor of the given node in the tree.
    The level order successor is the node that appears right after the given node in the level order traversal.
    """
    if not root: return None
    q = deque([root])

    while q:
        level_size = len(q)
        key_found = False
        for i in range(level_size):
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)

            if key_found:
                return node
            elif node.val == key:
                if i == level_size - 1:
                    return q[0]
                else:
                    key_found = True

    return None



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_successor
    print(find_successor([]))
