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


def inorder_successor_bst(root: BinaryTreeNode, d: int):
    """
    TODO: -> https://www.educative.io/module/lesson/data-structures-in-python/g7wVBVxqGJG
    """
    successor = None

    def dfs_inorder(root_node: BinaryTreeNode, successor: int):
        if not root_node:
            return

        if root_node.data > d:
            successor = root_node.data
        pass
    return None