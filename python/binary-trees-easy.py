from typing import List
import enum


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


class BinaryTreesEasy:
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
        self.recurse(root, out, TraversalType.POSTORDER)
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
