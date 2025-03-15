"""
Tree_right_view

"""


from collections import deque
def tree_right_view(root: TreeNode):
    if not root: return []
    result = []
    q = deque([root])

    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            if i == level_size - 1:
                result.append(node)
    return result



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to tree_right_view
    print(tree_right_view([]))
