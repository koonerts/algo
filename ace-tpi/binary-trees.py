from collections import deque

class BinaryTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def are_identical(root1: BinaryTreeNode, root2: BinaryTreeNode):
    if root1 is None and root2 is None:
        return True

    if root1 and root2:
        return root1.data == root2.data and \
               are_identical(root1.left, root2.left) and \
               are_identical(root1.right, root2.right)
    else:
        return False


class InorderIterator:
    """
    TODO: Come back to -> https://www.educative.io/module/lesson/data-structures-in-python/m7wOjD0DlBO
    """
    def __init__(self, root: BinaryTreeNode):
        self.stack = []
        self.populate_stack(root)

    def populate_stack(self, root: BinaryTreeNode):
        while root:
            self.stack.append(root)
            root = root.left

    def hasNext(self):
        return len(self.stack) > 0

    def getNext(self):
        if not self.hasNext(): return None

        val = self.stack.pop()
        self.populate_stack(val.right)
        return val


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

    def populate_stack(node: BinaryTreeNode):
        while node:
            stk.append(node)
            node = node.left

    stk = []
    populate_stack(root)
    while stk:
        node = stk.pop()
        result += str(node.data) + " "
        populate_stack(node.right)
    return result


def inorder_successor_bst(root: BinaryTreeNode, d):
    if not root:
        return None
    successor = None


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
    root = BinaryTreeNode(100)
    root.left = BinaryTreeNode(50)
    root.right = BinaryTreeNode(200)
    root.left.left = BinaryTreeNode(25)
    root.left.right = BinaryTreeNode(75)
    root.left.left.right = BinaryTreeNode(35)
    print(inorder_iterative(root))


main()
