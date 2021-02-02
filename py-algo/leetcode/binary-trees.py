from enum import Enum
import collections
import json
from collections import defaultdict, deque


class TraversalType(Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    LEVELORDER = 4


class RelationshipToParent(Enum):
    LEFT = 1,
    RIGHT = 2


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        out = []
        self.recurse(root, out, TraversalType.PREORDER)
        return out

    def inorderTraversal(self, root: TreeNode) -> list[int]:
        out = []
        self.recurse(root, out, TraversalType.INORDER)
        return out

    def postorderTraversal(self, root: TreeNode) -> list[int]:
        out = []
        if root:
            out += self.postorderTraversal(root.left)
            out += self.postorderTraversal(root.right)
            out.append(root.val)
        else:
            out.append(None)
        return out

    def reverse_postorderTraversal(self, root: TreeNode) -> list[int]:
        out = []
        if root:
            out += self.postorderTraversal(root.right)
            out += self.postorderTraversal(root.left)
            out.append(root.val)
        else:
            out.append(None)
        return out

    def levelOrder(self, root: TreeNode) -> list[list[int]]:
        levels = []
        if not root:
            return levels

        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels

    def recurse(self, root: TreeNode, out, traversal_type: TraversalType):
        if root is None:
            return

        if traversal_type == TraversalType.PREORDER:
            out.append(root.val)
            self.recurse(root.left, out, traversal_type)
            self.recurse(root.right, out, traversal_type)
        elif traversal_type == TraversalType.INORDER:
            self.recurse(root.left, out, traversal_type)
            out.append(root.val)
            self.recurse(root.right, out, traversal_type)
        elif traversal_type == TraversalType.POSTORDER:
            self.recurse(root.left, out, traversal_type)
            self.recurse(root.right, out, traversal_type)
            out.append(root.val)

    def preorder_traverse_iterative(self, root: TreeNode) -> list[int]:
        out = []
        if root is None:
            return out

        stack = [root]
        while len(stack) > 0:
            node = stack.pop()
            out.append(node.val)

            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

        return out

    def maxDepth(self, root: TreeNode) -> int:
        """
        Given a binary tree, find its maximum depth.
        The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
        Note: A leaf is a node with no children.

        Ex:
        Given binary tree [3,9,20,null,null,15,7], depth = 3
            3
           / \
          9  20
            /  \
           15   7
        :param root:
        :return:
        """
        if not root:
            return 0
        return self.max_depth_recurse(1, root)

    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth2(root.left)
        right_depth = self.maxDepth2(root.right)
        return max(left_depth, right_depth) + 1

    def max_depth_recurse(self, curr_depth: int, node: TreeNode) -> int:
        if not node:
            return curr_depth

        l_depth, r_depth = curr_depth, curr_depth
        if node.left:
            l_depth = self.max_depth_recurse(l_depth + 1, node.left)
        if node.right:
            r_depth = self.max_depth_recurse(r_depth + 1, node.right)
        return max(curr_depth, l_depth, r_depth)

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True

        def isMirror(n1: TreeNode, n2: TreeNode) -> bool:
            if not n1 and not n2:
                return True
            elif (not n1 and n2) or (n1 and not n2) or (n1.val != n2.val):
                return False
            else:
                return isMirror(n1.left, n2.right) and isMirror(n1.right, n2.left)

        return isMirror(root.left, root.right)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
        Note: A leaf is a node with no children.

        Example: Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
        return true, as there exist a root-to-leaf path 5->4->11->2 which sums to 22
        """
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:
            return sum == 0

        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    def buildTree_Post(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        """
        Given inorder and postorder traversal of a tree, construct the binary tree.
        Note: You may assume that duplicates do not exist in the tree.

        Ex:
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]
        Return the following binary tree:
            3
           / \
          9  20
            /  \
           15   7
        """

        def build(bound=None):
            if not inorder or inorder[-1] == bound: return None
            root = TreeNode(postorder.pop())
            root.right = build(root.val)
            inorder.pop()
            root.left = build(bound)
            return root

        return build()

    def buildTree_Pre(self, inorder: list[int], preorder: list[int]) -> TreeNode:
        """
        Given inorder and postorder traversal of a tree, construct the binary tree.
        Note: You may assume that duplicates do not exist in the tree.

        Ex:
        inorder = [9,3,15,20,7]
        preorder = [3,9,20,15,7]
        Return the following binary tree:
            3
           / \
          9  20
            /  \
           15   7
        """

        def build(bound=None):
            if not inorder or inorder[0] == bound: return None
            root = TreeNode(preorder.pop(0))
            root.left = build(root.val)
            inorder.pop(0)
            root.right = build(bound)
            return root

        return build()

    def connect(self, root: Node) -> Node:
        """
        You are given a perfect binary tree where all leaves are on the same level, and every parent has two children.
        Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
        Initially, all next pointers are set to NULL.

        Ex: Input: root = [1,2,3,4,5,6,7]
            Output: [1,#,2,3,#,4,5,6,7,#]
            Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node.
                         The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
        """
        if not root: return root

        q = collections.deque([root])
        while q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                if i < length - 1:
                    node.next = q[0]

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

        return root

    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        inorder = self.inorderTraversal(root)
        preorder = self.preorderTraversal(root)
        return json.dumps({'inorder':inorder, 'preorder':preorder})

    def deserialize(self, data: str) -> TreeNode:
        """
        Decodes your encoded data to tree.
        """
        map = json.loads(data)
        return self.buildTree_Pre(map.inorder, map.preorder)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pass

    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            else:
                return low < node.val < high and validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root)

    def maxPathSum(self, root: TreeNode) -> int:
        def find_max_sum(node: TreeNode):
            nonlocal max_sum

            if not node:
                return 0
            else:
                left_gain = max(find_max_sum(node.left), 0)
                right_gain = max(find_max_sum(node.right), 0)
                total_gain = left_gain + right_gain + node.val

                max_sum = max(max_sum, total_gain)
                return node.val + max(left_gain, right_gain)

        max_sum = float('-inf')
        find_max_sum(root)
        return max_sum

    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        q = collections.deque([beginWord])
        visited = set()
        word_set = set(wordList)

        ladder_len = 0
        while q:
            ladder_len += 1
            for _ in range(len(q)):
                curr_word = q.popleft()
                if curr_word == endWord:
                    return ladder_len
                else:
                    visited.add(curr_word)
                    for word in (w for w in word_set-visited):
                        char_diff = 0
                        for i in range(len(word)):
                            if word[i] != curr_word[i]:
                                char_diff += 1
                                if char_diff > 1: break
                        if char_diff == 1:
                            q.append(word)
        return 0

    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        if not prerequisites: return list(range(numCourses))

        in_degree, graph = {i:0 for i in range(numCourses)}, {i:[] for i in range(numCourses)}
        for course, pre_req in prerequisites:
            in_degree[course] += 1
            graph[pre_req].append(course)
            if pre_req not in in_degree:
                in_degree[pre_req] = 0

        q = deque()
        for c in (c for c in in_degree if in_degree[c] == 0):
            q.append(c)

        result = []
        while q:
            for _ in range(len(q)):
                course = q.popleft()
                result.append(course)
                for child in graph[course]:
                    in_degree[child] -= 1
                    if in_degree[child] == 0:
                        q.append(child)
        return result if len(result) == numCourses else []

    def removeLeafNodes(self, root: TreeNode, target: int) -> TreeNode:
        if not root or (not root.left and not root.right and root.val == target): return None

        def remove(node: TreeNode, parent: TreeNode, rel: RelationshipToParent):
            if not node:
                return
            else:
                remove(node.left, node, RelationshipToParent.LEFT)
                remove(node.right, node, RelationshipToParent.RIGHT)

                if node.val == target and not node.left and not node.right:
                    if rel == RelationshipToParent.LEFT:
                        parent.left = None
                    else:
                        parent.right = None
        remove(root, None, None)

        if (not root.left and not root.right and root.val == target):
            return None
        else:
            return root


node = TreeNode(1)
node.left = TreeNode(2)
node.left.left = TreeNode(2)
node.right = TreeNode(3)
node.right.left = TreeNode(2)
node.right.right = TreeNode(4)
print(Solution().removeLeafNodes(node, 2))
print(node)
