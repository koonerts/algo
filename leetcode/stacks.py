from typing import List
import collections

class MyQueueStack:
    """
    Implement a last in first out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal queue (push, top, pop, and empty).

    Implement the MyStack class:
    void push(int x) Pushes element x to the top of the stack.
    int pop() Removes the element on the top of the stack and returns it.
    int top() Returns the element on the top of the stack.
    boolean empty() Returns true if the stack is empty, false otherwise.

    Notes:
    You must use only standard operations of a queue, which means only push to back, peek/pop from front, size, and is empty operations are valid.
    Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue),
    as long as you use only a queue's standard operations.

    Follow-up:
    Can you implement the stack such that each operation is amortized O(1) time complexity?
    In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = collections.deque()
        self.q2 = collections.deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.q2:
            self.q2.append(self.q1.popleft())
        return self.q2.popleft()


    def top(self) -> int:
        """
        Get the top element.
        """
        if not self.q2:
            self.q2.append(self.q1.popleft())
        return self.q2[0]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not (self.q1 and self.q2)


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self) -> None:
        if self.min_stack[-1] == self.stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Stacks:

    def isValid(self, s: str) -> bool:
        """
        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        An input string is valid if:
          - Open brackets must be closed by the same type of brackets.
          - Open brackets must be closed in the correct order.

        Ex:
            Input: s = "{[]}", Output: true
            Input: s = "([)]", Output: false
        """
        if not s or len(s) <= 1:
            return False

        stack = []
        map_ = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c not in map_:
                stack.append(c)
            else:
                if not stack: return False
                if stack.pop() != map_[c]:
                    return False

        if not stack:
            return True
        return False

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to
        wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

        For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].
        Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
        """
        pass

    def evalRPN(self, tokens: List[str]) -> int:
        """
        Evaluate the value of an arithmetic expression in Reverse Polish Notation.
        Valid operators are +, -, *, /. Each operand may be an integer or another expression.

        Note:
        Division between two integers should truncate toward zero.
        The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.

        Example 1:
        Input: ["2", "1", "+", "3", "*"]
        Output: 9
        Explanation: ((2 + 1) * 3) = 9

        Example 2:
        Input: ["4", "13", "5", "/", "+"]
        Output: 6
        Explanation: (4 + (13 / 5)) = 6

        Example 3:
        Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        Output: 22
        Explanation:
          ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
        = ((10 * (6 / (12 * -11))) + 17) + 5
        = ((10 * (6 / -132)) + 17) + 5
        = ((10 * 0) + 17) + 5
        = (0 + 17) + 5
        = 17 + 5
        = 22
        """

        def execute(n1: int, n2: int, operand: str) -> int:
            if operand == '*': return n1 * n2
            if operand == '+': return n1 + n2
            if operand == '-': return n1 - n2
            if operand == '/': return int(n1 / n2)

        operands = ['*', '+', '-', '/']
        stack = []
        for t in tokens:
            if t in operands:
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(execute(n1, n2, t))
            else:
                stack.append(int(t))

        return stack[0]

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
        You may assume all four edges of the grid are all surrounded by water.

        Example 1:
        Input: grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        Output: 1

        Example 2:
        Input: grid = [
          ["1","1","0","0","0"],
          ["1","1","0","0","0"],
          ["0","0","1","0","0"],
          ["0","0","0","1","1"]
        ]
        Output: 3
        """
        if not grid:
            return 0

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        rows = len(grid)
        cols = len(grid[0])

        def dfs(grid, r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                grid[r][c] = "0"
                for x, y in dirs:
                    dfs(grid, r + x, c + y)

        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    islands += 1
                    dfs(grid, row, col)
        return islands

    def cloneGraph(self, node: Node) -> Node:
        """
        Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
        Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

        Test case format:
        For simplicity sake, each node's value is the same as the node's index (1-indexed).
        For example, the first node with val = 1, the second node with val = 2, and so on.
        The graph is represented in the test case using an adjacency list. An adjacency list is a collection of unordered lists used to represent a finite graph.
        Each list describes the set of neighbors of a node in the graph. The given node will always be the first node with val = 1.
        You must return the copy of the given node as a reference to the cloned graph.

        Ex1:
        Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
        Output: [[2,4],[1,3],[2,4],[1,3]]
        Explanation: There are 4 nodes in the graph.
        1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
        2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
        3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
        4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

        Ex2:
        Input: adjList = [[]]
        Output: [[]]
        Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and it does not have any neighbors.

        Ex3:
        Input: adjList = []
        Output: []
        Explanation: This an empty graph, it does not have any nodes.

        Ex4:
        Input: adjList = [[2],[1]]
        Output: [[2],[1]]
        """
        if not node: return node

        seen = {}

        def dfs(node: Node) -> Node:
            if node.val not in seen:
                clone = Node(node.val)
                seen[node.val] = clone
                for neighbor in node.neighbors:
                    clone.neighbors.append(dfs(neighbor))
                return clone
            else:
                return seen[node.val]

        return dfs(node)

    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        """
        You are given a list of non-negative integers, a1, a2, ..., an, and a target S.
        For each integer, you should choose either + or - as its new symbol.
        Find out how many ways to assign symbols to make sum of integers equal to target S.

        Example 1:
        Input: nums is [1, 1, 1, 1, 1], S is 3.
        Output: 5

        Explanation:
        -1+1+1+1+1 = 3
        +1-1+1+1+1 = 3
        +1+1-1+1+1 = 3
        +1+1+1-1+1 = 3
        +1+1+1+1-1 = 3
        There are 5 ways to assign symbols to make the sum of nums be target 3.
        """
        pass

    def decodeString(self, s: str) -> str:
        """
        Given an encoded string, return its decoded string.
        The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.
        Note that k is guaranteed to be a positive integer. You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
        Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k.
        For example, there won't be input like 3a or 2[4].

        Example 1:
        Input: s = "3[a]2[bc]"
        Output: "aaabcbc"

        Example 2:
        Input: s = "3[a2[c]]"
        Output: "accaccacc"

        Example 3:
        Input: s = "2[abc]3[cd]ef"
        Output: "abcabccdcdcdef"

        Example 4:
        Input: s = "abc3[cd]xyz"
        Output: "abccdcdcdxyz"
        """
        if not s: return s

        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
            else:
                enc_str = ''
                while stack and stack[-1] != '[':
                    enc_str = stack.pop() + enc_str
                stack.pop()

                multiplier = ''
                while stack and stack[-1].isnumeric():
                    multiplier = stack.pop() + multiplier

                stack.extend(list(enc_str*(int(multiplier))))
        return ''.join(stack)


print(Stacks().decodeString("3[a2[c]]"))