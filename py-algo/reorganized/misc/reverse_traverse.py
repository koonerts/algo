"""
Reverse_traverse

"""


from collections import deque
def reverse_traverse(root: TreeNode) -> deque:
    if not root: return deque()

    q = deque([root])
    result = deque()
    while q:
        level_size = len(q)
        level_result = []

        while level_size > 0:
            node = q.popleft()
            level_result.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            level_size -= 1

        result.appendleft(level_result)
    return result



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to reverse_traverse
    print(reverse_traverse([]))
