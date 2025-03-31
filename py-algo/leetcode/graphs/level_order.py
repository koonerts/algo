"""
Binary Tree Level Order Traversal

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

Time Complexity: O(n) where n is the number of nodes in the tree
Space Complexity: O(n) to store the result and the queue
"""

from typing import List, Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    """
    Given the root of a binary tree, return its level order traversal.

    Level order traversal visits nodes level by level, from left to right.
    This implementation offers two approaches:
    1. A recursive approach using DFS with level tracking
    2. An iterative approach using a queue (BFS)

    Args:
        root (Optional[TreeNode]): Root of the binary tree

    Returns:
        List[List[int]]: Level order traversal of the tree's values

    Time Complexity: O(n) where n is the number of nodes in the tree
    Space Complexity: O(n) to store the result and the recursion stack/queue
    """
    # Base case: empty tree
    if not root:
        return []

    # Iterative BFS approach using queue
    result = []
    queue = deque([root])

    # Process level by level
    while queue:
        # Get number of nodes at current level
        level_size = len(queue)
        level_nodes = []

        # Process all nodes at current level
        for _ in range(level_size):
            # Get the next node from the queue
            node = queue.popleft()
            level_nodes.append(node.val)

            # Add child nodes to queue for next level processing
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # Add current level's nodes to result
        result.append(level_nodes)

    return result

    # Alternative recursive DFS implementation:
    # def dfs(node, level):
    #     # Start the current level if needed
    #     if len(result) == level:
    #         result.append([])
    #
    #     # Add the current node value
    #     result[level].append(node.val)
    #
    #     # Process child nodes for the next level
    #     if node.left:
    #         dfs(node.left, level + 1)
    #     if node.right:
    #         dfs(node.right, level + 1)
    #
    # result = []
    # if root:
    #     dfs(root, 0)
    # return result


# Example usage
if __name__ == "__main__":
    # Create a binary tree: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(levelOrder(root))  # Output: [[3],[9,20],[15,7]]
