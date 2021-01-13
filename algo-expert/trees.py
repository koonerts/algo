from collections import deque


# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        # Write your code here.
        pass

    def remove(self, value, parent=None):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self

    def is_leaf(self):
        return not self.left and not self.right


class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


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

    def breadthFirstSearch(self, array):
        q = deque([self])
        while q:
            node = q.popleft()
            array.append(node.name)
            for child in node.children:
                q.append(child)
        return array


def create_bst_from_map(bst_map) -> BST:
    tree = bst_map['tree']
    node_map = {}
    root: BST
    for n in tree['nodes']:
        node_map[n['id']] = BST(n['value'])
        if n['id'] == tree['root']:
            root = node_map[n['id']]

    for n in tree['nodes']:
        node = node_map[n['id']]
        if n['left']: node.left = node_map[n['left']]
        if n['right']: node.right = node_map[n['right']]
    return root


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


def validateBst(tree: BST, low_limit=float('-inf'), high_limit=float('inf')):
    if not tree:
        return True
    else:
        return low_limit <= tree.value < high_limit \
               and validateBst(tree.left, low_limit, tree.value) \
               and validateBst(tree.right, tree.value, high_limit)


def minHeightBst(array):
    def construct_bst(low, high):
        if low > high:
            return None

        mid = (low+high)//2
        root = BST(array[mid])
        root.left = construct_bst(low, mid-1)
        root.right = construct_bst(mid+1, high)
        return root
    return construct_bst(0, len(array)-1)


def invertBinaryTree(tree):
    if tree:
        tree.left, tree.right = tree.right, tree.left
        invertBinaryTree(tree.left)
        invertBinaryTree(tree.right)
    return tree


def binaryTreeDiameter(tree):
    if not tree: return 0

    def find_depths(node):
        nonlocal max_diameter
        if not node:
            return 0
        else:
            left_depth = find_depths(node.left)
            right_depth = find_depths(node.right)
            max_diameter = max(max_diameter, left_depth+right_depth)
            return max(left_depth, right_depth) + 1
    max_diameter = 0
    find_depths(tree)
    return max_diameter


def findSuccessor(tree: BinaryTree, node: BinaryTree):
    if node.right:
        temp = node.right
        while temp.left:
            temp = temp.left
        return temp
    else:
        temp = node
        while temp.parent and temp.parent.right == temp:
            temp = temp.parent
        return temp.parent


def getYoungestCommonAncestor(topAncestor: AncestralTree, descendantOne: AncestralTree, descendantTwo: AncestralTree):
    d1_depth, d2_depth = 0, 0
    node1 = descendantOne
    while node1 != topAncestor:
        d1_depth += 1
        node1 = node1.ancestor

    node2 = descendantTwo
    while node2 != topAncestor:
        d2_depth += 1
        node2 = node2.ancestor

    depth_diff = abs(d1_depth-d2_depth)
    for _ in range(depth_diff):
        if d1_depth > d2_depth:
            descendantOne = descendantOne.ancestor
        else:
            descendantTwo = descendantTwo.ancestor

    while descendantOne != descendantTwo:
        descendantOne = descendantOne.ancestor
        descendantTwo = descendantTwo.ancestor
    return descendantOne


x = {
    "tree": {
        "nodes": [
            {"id": "1", "left": "3", "right": "2", "value": 1},
            {"id": "3", "left": "7", "right": "4", "value": 3},
            {"id": "7", "left": "8", "right": None, "value": 7},
            {"id": "8", "left": "9", "right": None, "value": 8},
            {"id": "9", "left": None, "right": None, "value": 9},
            {"id": "4", "left": None, "right": "5", "value": 4},
            {"id": "5", "left": None, "right": "6", "value": 5},
            {"id": "6", "left": None, "right": None, "value": 6},
            {"id": "2", "left": None, "right": None, "value": 2}
        ],
        "root": "1"
    }
}
root = create_bst_from_map(x)
print(binaryTreeDiameter(root))