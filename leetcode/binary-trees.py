from typing import List
import enum
import collections
import json


class TraversalType(enum.Enum):
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3
    LEVELORDER = 4


# Definition for a binary tree node.


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


class BinaryTrees:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        out = []
        self.recurse(root, out, TraversalType.PREORDER)
        return out

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        out = []
        self.recurse(root, out, TraversalType.INORDER)
        return out

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        out = []
        if root:
            out += self.postorderTraversal(root.left)
            out += self.postorderTraversal(root.right)
            out.append(root.val)
        else:
            out.append(None)
        return out

    def reverse_postorderTraversal(self, root: TreeNode) -> List[int]:
        out = []
        if root:
            out += self.postorderTraversal(root.right)
            out += self.postorderTraversal(root.left)
            out.append(root.val)
        else:
            out.append(None)
        return out

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
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

    def preorder_traverse_iterative(self, root: TreeNode) -> List[int]:
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

    def buildTree_Post(self, inorder: List[int], postorder: List[int]) -> TreeNode:
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

    def buildTree_Pre(self, inorder: List[int], preorder: List[int]) -> TreeNode:
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
        def validate(node: TreeNode, low=float('-inf'), high=float('inf')) -> bool:
            if not node:
                return True
            elif not (low < node.val < high):
                return False
            else:
                return validate(node.left, low, node.val) and validate(node.left, node.val, high)
        return validate(root)