

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            self.depthFirstSearch(array)
        return array


def findClosestValueInBst(tree: BST, target: int):
    node = tree
    closest_val = node.value
    while node:
        if node.value == target:
            return node.value
        elif node.value > target:
            node = node.left
        else:
            node = node.right

        if abs(node.value - target) < abs(closest_val - target):
            closest_val = node.value
    return closest_val


def branchSums(root: BinaryTree):
    results = []
    if not root: return results

    def recurse(node: BinaryTree, curr_sum=0):
        if not node:
            return
        else:
            if not node.left and not node.right:
                results.append(curr_sum + node.value)
            else:
                recurse(node.left, curr_sum + node.value)
                recurse(node.right, curr_sum + node.value)

    recurse(root)
    return results


def nodeDepths(root: BinaryTree):

    def sum_depths(node: BinaryTree, level=0):
        nonlocal depth_sum
        if not node:
            return
        else:
            depth_sum += level
            sum_depths(node.left, level+1)
            sum_depths(node.right, level+1)
    depth_sum = 0
    sum_depths(root)
    return depth_sum


node = BinaryTree(1)
node.left = BinaryTree(2)
node.left.left = BinaryTree(4)
node.left.left.left = BinaryTree(8)
node.left.left.right = BinaryTree(9)
node.left.right = BinaryTree(5)
node.left.right.left = BinaryTree(10)
node.right = BinaryTree(3)
node.right.right = BinaryTree(7)
node.right.left = BinaryTree(6)
print(nodeDepths(node))