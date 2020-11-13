from typing import List


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

        root = Node(node.val)
        seen = {f'{str(root.val)}':root}

        def dfs(node: Node):
            if str(node.val) not in seen:
                
                seen[str(node.val)] =




g = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
print(Stacks().numIslands(g))
