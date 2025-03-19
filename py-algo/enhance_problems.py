#!/usr/bin/env python3
"""
Script to enhance algorithm problem files with better documentation,
complexity analysis, and example test cases.

This script:
1. Processes Python files in the reorganized directory
2. Adds improved docstrings with detailed problem descriptions
3. Adds time and space complexity analysis
4. Adds example test cases to demonstrate usage
5. Prioritizes certain important problems
"""

import os
import re
import sys
from pathlib import Path

BASE_DIR = Path("/Users/koonerts/.proj/algo/py-algo/reorganized")

# List of high-priority problems to enhance first
PRIORITY_PROBLEMS = {
    "arrays": [
        "two_sum.py",
        "three_sum.py",
        "move_zeroes.py",
        "contains_duplicate.py",
        "max_profit.py",
        "is_valid_sudoku.py",
    ],
    "linked_lists": [
        "reverse.py",
        "merge_two_lists.py",
        "remove_nth_from_end.py",
        "has_cycle.py",
    ],
    "trees": [
        "max_depth.py",
        "inorder_traversal.py",
        "is_valid_bst.py",
        "level_order.py",
    ],
    "dp": [
        "climb_stairs.py",
        "coin_change.py",
        "longest_palindrome.py",
        "rob.py",
    ],
    "sorting": [
        "merge.py",
        "binary_search.py",
    ],
}

# Templates for different problem types
TEMPLATES = {
    "arrays": {
        "docstring": '''"""
{title}

{description}

Example:
    Input: {example_input}
    Output: {example_output}

Time Complexity: {time_complexity}
Space Complexity: {space_complexity}
"""''',
        "function_docstring": '''"""
{description}

Args:
    {args}

Returns:
    {returns}

Time Complexity: {time_complexity}
Space Complexity: {space_complexity}
"""''',
    },
    "linked_lists": {
        "docstring": '''"""
{title}

{description}

Example:
    Input: {example_input}
    Output: {example_output}

Time Complexity: {time_complexity}
Space Complexity: {space_complexity}
"""''',
        "function_docstring": '''"""
{description}

Args:
    {args}

Returns:
    {returns}

Time Complexity: {time_complexity}
Space Complexity: {space_complexity}
"""''',
    },
    "default": {
        "docstring": '''"""
{title}

{description}

Example:
    Input: {example_input}
    Output: {example_output}

Time Complexity: {time_complexity}
Space Complexity: {space_complexity}
"""''',
        "function_docstring": '''"""
{description}

Args:
    {args}

Returns:
    {returns}

Time Complexity: {time_complexity}
Space Complexity: {space_complexity}
"""''',
    },
}

# Problem-specific enhancements
PROBLEM_DATA = {
    # Arrays
    "two_sum.py": {
        "title": "Two Sum",
        "description": "Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.",
        "example_input": "nums = [2,7,11,15], target = 9",
        "example_output": "[0,1] (because nums[0] + nums[1] = 2 + 7 = 9)",
        "time_complexity": "O(n) where n is the length of the array",
        "space_complexity": "O(n) for the hash table",
        "imports": ["from typing import List"],
        "args": "nums (List[int]): Array of integers\ntarget (int): Target sum",
        "returns": "List[int]: Indices of the two numbers that add up to target",
        "examples": [
            "twoSum([2, 7, 11, 15], 9)  # Output: [0, 1]",
            "twoSum([3, 2, 4], 6)  # Output: [1, 2]",
            "twoSum([3, 3], 6)  # Output: [0, 1]",
        ],
    },
    "is_valid_sudoku.py": {
        "title": "Valid Sudoku",
        "description": "Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules: Each row must contain the digits 1-9 without repetition, each column must contain the digits 1-9 without repetition, and each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.",
        "example_input": '[\n  ["5","3",".",".","7",".",".",".","."],\n  ["6",".",".","1","9","5",".",".","."],\n  [".","9","8",".",".",".",".","6","."],\n  ["8",".",".",".","6",".",".",".","3"],\n  ["4",".",".","8",".","3",".",".","1"],\n  ["7",".",".",".","2",".",".",".","6"],\n  [".","6",".",".",".",".","2","8","."],\n  [".",".",".","4","1","9",".",".","5"],\n  [".",".",".",".","8",".",".","7","9"]\n]',
        "example_output": "true",
        "time_complexity": "O(1) since the board size is fixed (9x9)",
        "space_complexity": "O(1) since we use fixed-size data structures",
        "imports": ["from typing import List"],
        "args": "board (List[List[str]]): 9x9 Sudoku board",
        "returns": "bool: True if the board is valid, False otherwise",
        "examples": [
            'isValidSudoku([\n  ["5","3",".",".","7",".",".",".","."],\n  ["6",".",".","1","9","5",".",".","."],\n  [".","9","8",".",".",".",".","6","."],\n  ["8",".",".",".","6",".",".",".","3"],\n  ["4",".",".","8",".","3",".",".","1"],\n  ["7",".",".",".","2",".",".",".","6"],\n  [".","6",".",".",".",".","2","8","."],\n  [".",".",".","4","1","9",".",".","5"],\n  [".",".",".",".","8",".",".","7","9"]\n])  # Output: True',
            'isValidSudoku([\n  ["8","3",".",".","7",".",".",".","."],\n  ["6",".",".","1","9","5",".",".","."],\n  [".","9","8",".",".",".",".","6","."],\n  ["8",".",".",".","6",".",".",".","3"],\n  ["4",".",".","8",".","3",".",".","1"],\n  ["7",".",".",".","2",".",".",".","6"],\n  [".","6",".",".",".",".","2","8","."],\n  [".",".",".","4","1","9",".",".","5"],\n  [".",".",".",".","8",".",".","7","9"]\n])  # Output: False (duplicated 8 in first column)',
        ],
    },
    "three_sum.py": {
        "title": "Three Sum",
        "description": "Given an array of integers, find all unique triplets in the array that give the sum of zero.",
        "example_input": "[-1, 0, 1, 2, -1, -4]",
        "example_output": "[[-1, -1, 2], [-1, 0, 1]]",
        "time_complexity": "O(n²) where n is the length of the array",
        "space_complexity": "O(n) for the result (not counting the input)",
        "imports": ["from typing import List"],
        "args": "nums (List[int]): Array of integers",
        "returns": "List[List[int]]: List of triplets that sum to zero",
        "examples": [
            "threeSum([-1, 0, 1, 2, -1, -4])  # Output: [[-1, -1, 2], [-1, 0, 1]]",
            "threeSum([0, 0, 0])  # Output: [[0, 0, 0]]",
            "threeSum([1, 2, -2, -1])  # Output: []",
        ],
    },
    "move_zeroes.py": {
        "title": "Move Zeroes",
        "description": "Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.",
        "example_input": "[0, 1, 0, 3, 12]",
        "example_output": "[1, 3, 12, 0, 0]",
        "time_complexity": "O(n) where n is the length of the array",
        "space_complexity": "O(1) as we modify the array in-place",
        "imports": ["from typing import List"],
        "args": "nums (List[int]): Array of integers",
        "returns": "None: The array is modified in-place",
        "examples": [
            "arr1 = [0, 1, 0, 3, 12]\nmoveZeroes(arr1)\nprint(arr1)  # Output: [1, 3, 12, 0, 0]",
            "arr2 = [0, 0, 1]\nmoveZeroes(arr2)\nprint(arr2)  # Output: [1, 0, 0]",
        ],
    },
    "contains_duplicate.py": {
        "title": "Contains Duplicate",
        "description": "Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.",
        "example_input": "[1, 2, 3, 1]",
        "example_output": "true (because 1 appears twice)",
        "time_complexity": "O(n) where n is the length of the array",
        "space_complexity": "O(n) for the hash set",
        "imports": ["from typing import List"],
        "args": "nums (List[int]): Array of integers",
        "returns": "bool: True if the array contains duplicates, False otherwise",
        "examples": [
            "containsDuplicate([1, 2, 3, 1])  # Output: True",
            "containsDuplicate([1, 2, 3, 4])  # Output: False",
            "containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])  # Output: True",
        ],
    },
    "max_profit.py": {
        "title": "Best Time to Buy and Sell Stock",
        "description": "You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.",
        "example_input": "[7, 1, 5, 3, 6, 4]",
        "example_output": "5 (buy on day 2 when price = 1, sell on day 5 when price = 6, profit = 6-1 = 5)",
        "time_complexity": "O(n) where n is the number of days",
        "space_complexity": "O(1) using constant extra space",
        "imports": ["from typing import List"],
        "args": "prices (List[int]): Array of prices where prices[i] is the price on day i",
        "returns": "int: The maximum profit that can be achieved",
        "examples": [
            "maxProfit([7, 1, 5, 3, 6, 4])  # Output: 5",
            "maxProfit([7, 6, 4, 3, 1])  # Output: 0",
        ],
    },
    # Linked Lists
    "reverse.py": {
        "title": "Reverse Linked List",
        "description": "Reverse a singly linked list.",
        "example_input": "1->2->3->4->5->NULL",
        "example_output": "5->4->3->2->1->NULL",
        "time_complexity": "O(n) where n is the number of nodes in the list",
        "space_complexity": "O(1) as we only use a constant amount of extra space",
        "imports": [
            "from typing import Optional\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next"
        ],
        "args": "head (Optional[ListNode]): Head of the linked list",
        "returns": "Optional[ListNode]: New head of the reversed linked list",
        "examples": [
            "# Create a linked list: 1->2->3->4->5",
            "head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))",
            "# Reverse it",
            "new_head = reverse(head)",
            "# Print the reversed list",
            "while new_head:",
            '    print(new_head.val, end=" ")',
            "    new_head = new_head.next",
            "# Output: 5 4 3 2 1",
        ],
    },
    "has_cycle.py": {
        "title": "Linked List Cycle",
        "description": "Given head, the head of a linked list, determine if the linked list has a cycle in it. There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.",
        "example_input": "head = [3,2,0,-4], pos = 1 (pos denotes the index of the node that tail's next pointer is connected to)",
        "example_output": "true (there is a cycle in the linked list)",
        "time_complexity": "O(n) where n is the number of nodes in the list",
        "space_complexity": "O(1) as we only use two pointers regardless of list size",
        "imports": [
            "from typing import Optional\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next"
        ],
        "args": "head (Optional[ListNode]): Head of the linked list",
        "returns": "bool: True if the linked list has a cycle, False otherwise",
        "examples": [
            "# Create a linked list with a cycle: 3->2->0->-4->2...",
            "head = ListNode(3)",
            "node1 = ListNode(2)",
            "node2 = ListNode(0)",
            "node3 = ListNode(-4)",
            "head.next = node1",
            "node1.next = node2",
            "node2.next = node3",
            "node3.next = node1  # Creates a cycle",
            "",
            "print(hasCycle(head))  # Output: True",
            "",
            "# Create a linked list without a cycle: 1->2->3->None",
            "head2 = ListNode(1, ListNode(2, ListNode(3)))",
            "print(hasCycle(head2))  # Output: False",
        ],
    },
    "merge_two_lists.py": {
        "title": "Merge Two Sorted Lists",
        "description": "Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.",
        "example_input": "l1 = [1,2,4], l2 = [1,3,4]",
        "example_output": "[1,1,2,3,4,4]",
        "time_complexity": "O(n + m) where n and m are the lengths of the lists",
        "space_complexity": "O(1) as we only modify pointers",
        "imports": [
            "from typing import Optional\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next"
        ],
        "args": "l1 (Optional[ListNode]): Head of first sorted linked list\nl2 (Optional[ListNode]): Head of second sorted linked list",
        "returns": "Optional[ListNode]: Head of merged sorted linked list",
        "examples": [
            "# Create two sorted linked lists:",
            "# 1->2->4",
            "l1 = ListNode(1, ListNode(2, ListNode(4)))",
            "# 1->3->4",
            "l2 = ListNode(1, ListNode(3, ListNode(4)))",
            "",
            "# Merge them",
            "result = mergeTwoLists(l1, l2)",
            "",
            "# Print the merged list",
            "while result:",
            '    print(result.val, end=" ")',
            "    result = result.next",
            "# Output: 1 1 2 3 4 4",
        ],
    },
    "remove_nth_from_end.py": {
        "title": "Remove Nth Node From End of List",
        "description": "Given the head of a linked list, remove the nth node from the end of the list and return its head.",
        "example_input": "head = [1,2,3,4,5], n = 2",
        "example_output": "[1,2,3,5] (the 2nd node from the end, which is 4, is removed)",
        "time_complexity": "O(n) where n is the length of the list",
        "space_complexity": "O(1) as we only use a constant amount of extra space",
        "imports": [
            "from typing import Optional\n\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next"
        ],
        "args": "head (Optional[ListNode]): Head of the linked list\nn (int): Position from the end to remove (1-indexed)",
        "returns": "Optional[ListNode]: Head of the modified linked list",
        "examples": [
            "# Create a linked list: 1->2->3->4->5",
            "head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))",
            "",
            "# Remove the 2nd node from the end",
            "result = removeNthFromEnd(head, 2)",
            "",
            "# Print the result",
            "while result:",
            '    print(result.val, end=" ")',
            "    result = result.next",
            "# Output: 1 2 3 5",
        ],
    },
    # Trees
    "max_depth.py": {
        "title": "Maximum Depth of Binary Tree",
        "description": "Given the root of a binary tree, return its maximum depth. A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.",
        "example_input": "root = [3,9,20,null,null,15,7]",
        "example_output": "3",
        "time_complexity": "O(n) where n is the number of nodes in the tree",
        "space_complexity": "O(h) where h is the height of the tree (for recursion stack)",
        "imports": [
            "from typing import Optional\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right"
        ],
        "args": "root (Optional[TreeNode]): Root of the binary tree",
        "returns": "int: The maximum depth of the tree",
        "examples": [
            "# Create a binary tree: [3,9,20,null,null,15,7]",
            "root = TreeNode(3)",
            "root.left = TreeNode(9)",
            "root.right = TreeNode(20)",
            "root.right.left = TreeNode(15)",
            "root.right.right = TreeNode(7)",
            "",
            "print(maxDepth(root))  # Output: 3",
        ],
    },
    "level_order.py": {
        "title": "Binary Tree Level Order Traversal",
        "description": "Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).",
        "example_input": "root = [3,9,20,null,null,15,7]",
        "example_output": "[[3],[9,20],[15,7]]",
        "time_complexity": "O(n) where n is the number of nodes in the tree",
        "space_complexity": "O(n) to store the result and the queue",
        "imports": [
            "from typing import List, Optional, Deque\nfrom collections import deque\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right"
        ],
        "args": "root (Optional[TreeNode]): Root of the binary tree",
        "returns": "List[List[int]]: Level order traversal of the tree's values",
        "examples": [
            "# Create a binary tree: [3,9,20,null,null,15,7]",
            "root = TreeNode(3)",
            "root.left = TreeNode(9)",
            "root.right = TreeNode(20)",
            "root.right.left = TreeNode(15)",
            "root.right.right = TreeNode(7)",
            "",
            "print(levelOrder(root))  # Output: [[3],[9,20],[15,7]]",
        ],
    },
    "inorder_traversal.py": {
        "title": "Binary Tree Inorder Traversal",
        "description": "Given the root of a binary tree, return the inorder traversal of its nodes' values.",
        "example_input": "root = [1,null,2,3]",
        "example_output": "[1,3,2]",
        "time_complexity": "O(n) where n is the number of nodes in the tree",
        "space_complexity": "O(n) for the output list and recursion stack",
        "imports": [
            "from typing import List, Optional\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right"
        ],
        "args": "root (Optional[TreeNode]): Root of the binary tree",
        "returns": "List[int]: The inorder traversal of the tree's values",
        "examples": [
            "# Create a binary tree: [1,null,2,3]",
            "root = TreeNode(1)",
            "root.right = TreeNode(2)",
            "root.right.left = TreeNode(3)",
            "",
            "print(inorderTraversal(root))  # Output: [1, 3, 2]",
        ],
    },
    "is_valid_bst.py": {
        "title": "Validate Binary Search Tree",
        "description": "Given the root of a binary tree, determine if it is a valid binary search tree (BST). A valid BST is defined as follows: The left subtree of a node contains only nodes with keys less than the node's key. The right subtree of a node contains only nodes with keys greater than the node's key. Both the left and right subtrees must also be binary search trees.",
        "example_input": "root = [2,1,3]",
        "example_output": "true",
        "time_complexity": "O(n) where n is the number of nodes in the tree",
        "space_complexity": "O(h) where h is the height of the tree (for recursion stack)",
        "imports": [
            "from typing import Optional\n\nclass TreeNode:\n    def __init__(self, val=0, left=None, right=None):\n        self.val = val\n        self.left = left\n        self.right = right"
        ],
        "args": "root (Optional[TreeNode]): Root of the binary tree",
        "returns": "bool: True if the tree is a valid BST, False otherwise",
        "examples": [
            "# Create a valid BST: [2,1,3]",
            "valid_bst = TreeNode(2)",
            "valid_bst.left = TreeNode(1)",
            "valid_bst.right = TreeNode(3)",
            "",
            "# Create an invalid BST: [5,1,4,null,null,3,6]",
            "invalid_bst = TreeNode(5)",
            "invalid_bst.left = TreeNode(1)",
            "invalid_bst.right = TreeNode(4)",
            "invalid_bst.right.left = TreeNode(3)",
            "invalid_bst.right.right = TreeNode(6)",
            "",
            "print(isValidBST(valid_bst))    # Output: True",
            "print(isValidBST(invalid_bst))  # Output: False",
        ],
    },
    # DP
    "climb_stairs.py": {
        "title": "Climbing Stairs",
        "description": "You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?",
        "example_input": "n = 3",
        "example_output": "3 (There are three ways: 1+1+1, 1+2, 2+1)",
        "time_complexity": "O(n) where n is the number of steps",
        "space_complexity": "O(1) using constant extra space",
        "imports": [],
        "args": "n (int): Number of steps",
        "returns": "int: Number of distinct ways to climb to the top",
        "examples": [
            "climbStairs(2)  # Output: 2",
            "climbStairs(3)  # Output: 3",
            "climbStairs(5)  # Output: 8",
        ],
    },
    "longest_palindrome.py": {
        "title": "Longest Palindromic Substring",
        "description": "Given a string s, return the longest palindromic substring in s.",
        "example_input": "babad",
        "example_output": "bab (Note: aba is also a valid answer)",
        "time_complexity": "O(n²) where n is the length of the string",
        "space_complexity": "O(1) as we only need constant extra space",
        "imports": [],
        "args": "s (str): Input string",
        "returns": "str: Longest palindromic substring",
        "examples": [
            'longestPalindrome("babad")  # Output: "bab" or "aba"',
            'longestPalindrome("cbbd")  # Output: "bb"',
            'longestPalindrome("a")  # Output: "a"',
        ],
    },
    "rob.py": {
        "title": "House Robber",
        "description": "You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night. Given an array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.",
        "example_input": "[1, 2, 3, 1]",
        "example_output": "4 (Rob house 1 (1) and then rob house 3 (3). 1 + 3 = 4.)",
        "time_complexity": "O(n) where n is the number of houses",
        "space_complexity": "O(1) as we only use a constant amount of extra space",
        "imports": ["from typing import List"],
        "args": "nums (List[int]): Array of money in each house",
        "returns": "int: Maximum amount of money that can be robbed",
        "examples": [
            "rob([1, 2, 3, 1])  # Output: 4",
            "rob([2, 7, 9, 3, 1])  # Output: 12",
        ],
    },
    "coin_change.py": {
        "title": "Coin Change",
        "description": "You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money. Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.",
        "example_input": "coins = [1, 2, 5], amount = 11",
        "example_output": "3 (11 = 5 + 5 + 1)",
        "time_complexity": "O(amount * n) where n is the number of coin denominations",
        "space_complexity": "O(amount) for the DP array",
        "imports": ["from typing import List"],
        "args": "coins (List[int]): Array of coin denominations\namount (int): Target amount to make",
        "returns": "int: Fewest number of coins needed or -1 if impossible",
        "examples": [
            "coinChange([1, 2, 5], 11)  # Output: 3",
            "coinChange([2], 3)  # Output: -1",
            "coinChange([1], 0)  # Output: 0",
        ],
    },
    # Sorting and Searching
    "merge.py": {
        "title": "Merge Sorted Array",
        "description": "You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. Merge nums1 and nums2 into a single array sorted in non-decreasing order. The final sorted array should be stored inside nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.",
        "example_input": "nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3",
        "example_output": "[1,2,2,3,5,6]",
        "time_complexity": "O(m + n) where m and n are the lengths of the arrays",
        "space_complexity": "O(1) as we modify nums1 in-place",
        "imports": ["from typing import List"],
        "args": "nums1 (List[int]): First sorted array with extra space\nm (int): Number of elements in nums1\nnums2 (List[int]): Second sorted array\nn (int): Number of elements in nums2",
        "returns": "None: nums1 is modified in-place",
        "examples": [
            "nums1 = [1, 2, 3, 0, 0, 0]",
            "nums2 = [2, 5, 6]",
            "merge(nums1, 3, nums2, 3)",
            "print(nums1)  # Output: [1, 2, 2, 3, 5, 6]",
        ],
    },
    "binary_search.py": {
        "title": "Binary Search",
        "description": "Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.",
        "example_input": "nums = [-1,0,3,5,9,12], target = 9",
        "example_output": "4",
        "time_complexity": "O(log n) where n is the length of the array",
        "space_complexity": "O(1) as we use constant extra space",
        "imports": ["from typing import List"],
        "args": "nums (List[int]): Sorted array of integers\ntarget (int): Target value to search for",
        "returns": "int: Index of target if found, otherwise -1",
        "examples": [
            "binarySearch([-1, 0, 3, 5, 9, 12], 9)  # Output: 4",
            "binarySearch([-1, 0, 3, 5, 9, 12], 2)  # Output: -1",
        ],
    },
}


def enhance_file(file_path, problem_data):
    """
    Enhance a problem file with better documentation and examples

    Args:
        file_path (Path): Path to the problem file
        problem_data (dict): Dictionary containing problem information

    Returns:
        bool: True if enhancement was successful, False otherwise
    """
    try:
        with open(file_path, "r") as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

    # Extract existing parts
    function_name = os.path.basename(file_path).replace(".py", "")

    # Get the category from the path
    category = file_path.parent.name

    # Select appropriate template
    template = TEMPLATES.get(category, TEMPLATES["default"])

    # Try to find function definition
    function_match = re.search(r"def\s+([a-zA-Z0-9_]+)\s*\(", content)
    if function_match:
        function_name = function_match.group(1)

    # Create enhanced file content
    new_content = []

    # Add file docstring
    title = problem_data.get("title", " ".join(function_name.split("_")).title())
    description = problem_data.get("description", "")
    example_input = problem_data.get("example_input", "")
    example_output = problem_data.get("example_output", "")
    time_complexity = problem_data.get("time_complexity", "")
    space_complexity = problem_data.get("space_complexity", "")

    file_docstring = template["docstring"].format(
        title=title,
        description=description,
        example_input=example_input,
        example_output=example_output,
        time_complexity=time_complexity,
        space_complexity=space_complexity,
    )

    new_content.append(file_docstring)
    new_content.append("")

    # Add imports
    imports = problem_data.get("imports", [])
    if imports:
        for imp in imports:
            new_content.append(imp)
        new_content.append("")

    # Find function definition and add function docstring
    try:
        lines = content.splitlines()
        function_found = False

        for i, line in enumerate(lines):
            if not function_found and re.match(r"def\s+[a-zA-Z0-9_]+\s*\(", line):
                function_found = True
                new_content.append(line)

                # Add function docstring
                if "args" in problem_data:
                    indentation = len(line) - len(line.lstrip()) + 4
                    indent = " " * indentation

                    function_docstring = template["function_docstring"].format(
                        description=description,
                        args=problem_data.get("args", ""),
                        returns=problem_data.get("returns", ""),
                        time_complexity=time_complexity,
                        space_complexity=space_complexity,
                    )

                    # Indent docstring
                    function_docstring_lines = function_docstring.splitlines()
                    for j, doc_line in enumerate(function_docstring_lines):
                        if j == 0:
                            new_content.append(f"{indent}{doc_line}")
                        else:
                            new_content.append(f"{indent}{doc_line}")

                # Continue with function body
                in_docstring = False
                for j in range(i + 1, len(lines)):
                    line = lines[j]

                    # Skip existing docstring
                    if '"""' in line or "'''" in line:
                        if not in_docstring:
                            in_docstring = True
                        else:
                            in_docstring = False
                        continue

                    if in_docstring:
                        continue

                    new_content.append(line)
            elif not function_found:
                # Add lines before function definition
                if not (
                    line.startswith('"""')
                    or line.startswith("'''")
                    or in_docstring
                    or line.strip() == ""
                ):
                    new_content.append(line)

                # Track docstring state to skip existing docstring
                if line.startswith('"""') or line.startswith("'''"):
                    in_docstring = not in_docstring

        # Add example usage at the end if we have examples
        examples = problem_data.get("examples", [])
        if examples:
            if not new_content[-1].strip():
                new_content[-1] = "\n\n# Example usage"
            else:
                new_content.append("\n\n# Example usage")

            new_content.append('if __name__ == "__main__":')
            for example in examples:
                new_content.append(f"    # {example}")

            # Add assertion tests if available
            test_assertions = problem_data.get("test_assertions", [])
            if test_assertions:
                new_content.append("\n    # Run tests")
                for assertion in test_assertions:
                    new_content.append(f"    assert {assertion}")
                new_content.append("    print('All tests passed!')")

        # Write back to file
        try:
            with open(file_path, "w") as f:
                f.write("\n".join(new_content))
            print(f"Enhanced {file_path}")
            return True
        except Exception as e:
            print(f"Error writing to {file_path}: {e}")
            return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False


def main():
    """
    Main function to enhance problem files
    """
    print("Enhancing algorithm problem files...")

    # Check if base directory exists
    if not BASE_DIR.exists():
        print(f"Error: Base directory {BASE_DIR} does not exist")
        sys.exit(1)

    # Process high-priority problems first
    for category, problems in PRIORITY_PROBLEMS.items():
        category_dir = BASE_DIR / category
        if not category_dir.exists():
            print(f"Warning: Category directory {category_dir} does not exist")
            continue

        for problem_file in problems:
            file_path = category_dir / problem_file
            if not file_path.exists():
                print(f"Warning: Priority problem {file_path} does not exist")
                continue

            from inspect import currentframe, getframeinfo

            frameinfo = getframeinfo(currentframe())
            print(f"Processing {file_path} at {frameinfo.lineno}")

            # Check if we have specific data for this problem
            problem_data = {}
            if problem_file in globals().get("PROBLEM_DATA", {}):
                problem_data = globals()["PROBLEM_DATA"].get(problem_file, {})

            # Enhance the file
            enhance_file(file_path, problem_data)

    # Process remaining files
    try:
        for category_dir in [
            d
            for d in BASE_DIR.iterdir()
            if d.is_dir() and d.name not in [".git", "__pycache__"]
        ]:
            for file_path in category_dir.glob("*.py"):
                if file_path.name == "__init__.py":
                    continue

                # Skip already processed priority problems
                if (
                    category_dir.name in PRIORITY_PROBLEMS
                    and file_path.name in PRIORITY_PROBLEMS[category_dir.name]
                ):
                    continue

                # Check if we have specific data for this problem
                problem_data = {}
                if file_path.name in globals().get("PROBLEM_DATA", {}):
                    problem_data = globals()["PROBLEM_DATA"].get(file_path.name, {})

                # Enhance the file
                enhance_file(file_path, problem_data)
    except Exception as e:
        print(f"Error processing files: {e}")

    print("Enhancement complete!")


if __name__ == "__main__":
    main()
