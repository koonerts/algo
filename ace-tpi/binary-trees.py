from collections import deque

class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def are_identical(root1: BinaryTreeNode, root2: BinaryTreeNode):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        return (root1.data == root2.data and
                are_identical(root1.left, root2.left) and
                are_identical(root1.right, root2.right))

    return False


class InorderIterator:
    """
    TODO: Come back to -> https://www.educative.io/module/lesson/data-structures-in-python/m7wOjD0DlBO
    """
    def __init__(self, root: BinaryTreeNode):
        self.stack = []

    def populate_stack(self, root: BinaryTreeNode):
        pass

    def hasNext(self):
        return len(self.stack) > 0

    def getNext(self):
        pass


def inorder_using_iterator(root: BinaryTreeNode):
    iter = InorderIterator(root)
    result = ""
    while iter.hasNext():
        ptr = iter.getNext()
        result += str(ptr.data) + " "
    return result


def inorder_iterative(root: BinaryTreeNode):
    result = ""
    if not root:
        return result

    stk = []
    while stk or root:
        if root:
            stk.append(root)
            root = root.left
        else:
            node = stk.pop()
            result += str(node.data) + " "
            root = node.right

    return str(result)


def inorder_successor_bst(root: BinaryTreeNode, d):
    if not root:
        return None

    successor = None

    while root:
        if root.data < d:
            root = root.right
        elif root.data > d:
            successor = root
            root = root.left
        else:
            if root.right:
                while root.left:
                    root = root.left
                successor = root
            break
    return successor


def level_order_traversal(root: BinaryTreeNode):
    result = ""
    que = deque([root])

    while que:
        level_result = ""
        for _ in range(len(que)):
            node = que.popleft()
            level_result += str(node.data) + " "
            if node.left: que.append(node.left)
            if node.right: que.append(node.right)
        result += level_result.rstrip() + "\n"
    return result


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def traverse(root):
    result = deque()
    # TODO: Write your code here
    return result


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))


main()
