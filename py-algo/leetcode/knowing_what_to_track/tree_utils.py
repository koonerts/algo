"""
Tree utility classes and functions

This module provides common tree-related classes and utility functions
used by various tree algorithms.
"""

from enum import Enum


class TraversalType(Enum):
    """Enum for different tree traversal orders"""

    PREORDER = 1
    INORDER = 2
    POSTORDER = 3


class TreeNode:
    """Binary tree node with left and right children"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


class Node:
    """Node with left, right, and next pointers (for specific problems)"""

    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return f"Node({self.val})"


class Robot:
    """Robot interface for clean room problem"""

    def move(self) -> bool:
        """Move the robot one step forward. Returns True if successful."""
        pass

    def turnLeft(self):
        """Turn the robot 90 degrees left."""
        pass

    def turnRight(self):
        """Turn the robot 90 degrees right."""
        pass

    def clean(self):
        """Clean the current cell."""
        pass
