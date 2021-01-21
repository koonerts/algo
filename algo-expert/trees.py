from collections import deque
import math

# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


class BST:
    def __init__(self, value):
        self.value = value
        self.left: 'BST' = None
        self.right: 'BST' = None

    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def contains(self, value):
        if self.value == value:
            return True
        elif value < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(value)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(value)

    def remove(self, value, parent=None):
        if not parent and self.value == value:
            if self.is_leaf():
                return
            elif not self.right:
                self.value = self.left.value
                self.left = self.left.left
            else:
                if self.right.left:
                    prev = self.right
                    node = self.right.left
                    while node.left:
                        prev = node
                        node = node.left

                    self.value = node.value
                    prev.left = None
                else:
                    self.value = self.right.value
                    self.right = self.right.right
        else:
            if value < self.value and self.left:
                self.left.remove(value, self)
            elif value > self.value and self.right:
                self.right.remove(value, self)
            else:
                if self.is_leaf():
                    if parent.left == self:
                        parent.left = None
                    else:
                        parent.right = None
                elif not self.right:
                    if parent.left == self:
                        parent.left = self.left
                    else:
                        parent.right = self.left
                else:
                    if self.right.left:
                        prev = self.right
                        node = self.right.left
                        while node.left:
                            prev = node
                            node = node.left
                        self.value = node.value
                        prev.left = None
                    else:
                        if parent.left == self:
                            parent.left.value = self.right.value
                            parent.left.right = parent.left.right.right
                        else:
                            parent.right.value = self.right.value
                            parent.right.right = parent.right.right.right

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

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []


def create_binary_tree_from_map(bt_map) -> BinaryTree:
    if 'tree' in bt_map:
        tree = bt_map['tree']
    else:
        tree = bt_map

    node_map = {}
    root: BinaryTree
    for n in tree['nodes']:
        node_map[n['id']] = BinaryTree(n['value'])
        if n['id'] == tree['root']:
            root = node_map[n['id']]

    for n in tree['nodes']:
        node = node_map[n['id']]

        if n['left']:
            node.left = node_map[n['left']]
            node.left.parent = node

        if n['right']:
            node.right = node_map[n['right']]
            node.right.parent = node

    return root


def create_bst_from_map(bst_map) -> BST:
    if 'tree' in bst_map:
        tree = bst_map['tree']
    else:
        tree = bst_map

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


def topologicalSort(jobs, deps):
    if not jobs or not deps: return jobs

    graph, in_degree = {i:[] for i in jobs}, {i:0 for i in jobs}
    for pre_req, job in deps:
        if job not in graph: graph[pre_req] = [job]
        else: graph[pre_req].append(job)
        in_degree[job] = in_degree.get(job, 0) + 1

    q = deque()
    for job in in_degree:
        if in_degree[job] == 0:
            q.append(job)

    result = []
    while q:
        job = q.pop()
        result.append(job)
        for child in graph[result[-1]]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                q.append(child)
    return result if len(result) == len(jobs) else []


def iterativeInOrderTraversal(tree, callback):
    node = tree
    while node.parent:
        node = node.parent

    prev = None
    while node:
        if node.left and prev != node.left:
            prev = node
            node = node.left
        else:
            callback(node)
            if node.right:
                prev = node
                node = node.right
            else:
                while node.parent and node.parent.right == node:
                    node = node.parent

                prev = node
                node = node.parent


def flattenBinaryTree(root):
    head, stk = None, []
    node, prev = root, None
    while stk or node:
        while node:
            stk.append(node)
            node = node.left

        node = stk.pop()
        if not head:
            head = node

        if prev:
            prev.right = node
            node.left = prev
        prev = node
        node = node.right
    return head


def maxPathSum(tree):
    if not tree: return 0
    elif not tree.left and not tree.right: return tree.value

    def dfs_sum(node):
        nonlocal max_path_sum
        if not node:
            return 0
        else:
            l_sum = dfs_sum(node.left)
            r_sum = dfs_sum(node.right)

            max_path_sum = max(max_path_sum, l_sum + r_sum + node.value, l_sum + node.value, r_sum + node.value)
            return max(l_sum, r_sum) + node.value

    max_path_sum = float('-inf')
    dfs_sum(tree)
    return max_path_sum


def sameBsts(arrayOne, arrayTwo):
    if arrayOne[0] != arrayTwo[1] or len(arrayOne) != len(arrayTwo):
        return False


def getLowestCommonManager(topManager: OrgChart, reportOne: OrgChart, reportTwo: OrgChart):
    pass


def rightSiblingTree(root):
    if not root: return root

    q = deque([root.left, root.right])

    while q:
        prev = None
        q_len = len(q)
        for i in range(q_len):
            left, right = q.popleft()
            pass


def allKindsOfNodeDepths(root):

    def depths(node, level=0):
        nonlocal total_sum
        if not node:
            return
        else:
            for i in range(1,level+1):
                total_sum += i
            depths(node.left, level+1)
            depths(node.right, level+1)

    total_sum=0
    depths(root)
    return total_sum


def cycleInGraph(edges):
    in_degrees = {i:0 for i in range(len(edges))}
    for node, children in enumerate(edges):
        for child in children:
            in_degrees[child] += 1

    q = deque()
    for node in in_degrees:
        if in_degrees[node] == 0:
            q.append(node)

    node_cnt = 0
    while q:
        node = q.popleft()
        node_cnt += 1

        for child in edges[node]:
            in_degrees[child] -= 1
            if in_degrees[child] == 0:
                q.append(child)
    return True if node_cnt != len(edges) else False


print(cycleInGraph([[1, 3], [2, 3, 4], [0], [], [2, 5], []]))