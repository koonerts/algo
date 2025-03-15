from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # level order traversal using 'next' pointer
    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None
            while current:
                print(str(current.val) + " ", end="")
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next
            print()

    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end="")
        current = self
        while current:
            print(str(current.val) + " ", end="")
            current = current.next


def traverse_using_recursion(root: TreeNode) -> list[list[int]]:
    result = []
    if not root:
        return result

    def level_order_traverse(node: TreeNode, level: int):
        if node:
            if len(result) < level:
                result.append([node.val])
            else:
                result[level - 1].append(node.val)

            level_order_traverse(node.left, level + 1)
            level_order_traverse(node.right, level + 1)

    level_order_traverse(root, 1)
    return result


def traverse_using_queue(root: TreeNode) -> list[list[int]]:
    """
    Given a binary tree, populate an array to represent its level-by-level traversal by using a queue.
    You should populate the values of all nodes of each level from left to right in separate sub-arrays.
    """
    if not root:
        return []
    result = []
    q = deque([root])

    while q:
        level_size = len(q)
        level_result = []

        while level_size > 0:
            node = q.popleft()
            level_result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            level_size -= 1

        result.append(level_result)

    return result


def reverse_traverse(root: TreeNode) -> deque:
    if not root:
        return deque()

    q = deque([root])
    result = deque()
    while q:
        level_size = len(q)
        level_result = []

        while level_size > 0:
            node = q.popleft()
            level_result.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            level_size -= 1

        result.appendleft(level_result)
    return result


def zigzag_traverse(root: TreeNode) -> list[list[int]]:
    """
    Given a binary tree, populate an array to represent its level-by-level traversal by using a queue.
    You should populate the values of all nodes of each level from left to right in separate sub-arrays.
    """
    if not root:
        return []
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

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            level_size -= 1

        result.append(list(level_result))
        forward = not forward

    return result


def find_level_averages(root: TreeNode):
    """
    Given a binary tree, populate an array to represent the averages of all of its levels.
    """
    if not root:
        return []
    result = []
    q = deque([root])

    while q:
        level_size = len(q)
        level_sum = 0

        for _ in range(level_size):
            node = q.popleft()
            level_sum += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level_sum / level_size)

    return result


def find_minimum_depth(root: TreeNode) -> int:
    """
    Find the minimum depth of a binary tree.
    The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
    """
    if not root:
        return -1
    level = 1
    q = deque([root])
    while q:
        level_size = len(q)
        for _ in range(level_size):
            node = q.popleft()
            if not node.left and not node.right:
                return level
            else:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        level += 1


def find_successor(root: TreeNode, key: int):
    """
    Given a binary tree and a node, find the level order successor of the given node in the tree.
    The level order successor is the node that appears right after the given node in the level order traversal.
    """
    if not root:
        return None
    q = deque([root])

    while q:
        level_size = len(q)
        key_found = False
        for i in range(level_size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

            if key_found:
                return node
            elif node.val == key:
                if i == level_size - 1:
                    return q[0]
                else:
                    key_found = True

    return None


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


def tree_right_view(root: TreeNode):
    if not root:
        return []
    result = []
    q = deque([root])

    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if i == level_size - 1:
                result.append(node)
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end="")


main()
