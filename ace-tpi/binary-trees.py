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
    def __init__(self, root: BinaryTreeNode):
        self.stack = [root]

    def hasNext(self):
        return len(self.stack) > 0

    def getNext(self):



def inorder_using_iterator(root: BinaryTreeNode):
    iter = InorderIterator(root)
    result = ""
    while iter.hasNext():
        ptr = iter.getNext()
        result += str(ptr.data) + " "
    return result


def inorder_iterative(root: BinaryTreeNode):
    result = ""

    return result