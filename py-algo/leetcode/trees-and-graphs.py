from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: 'TreeNode' = left
        self.right: 'TreeNode' = right

class Robot:
    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """



class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stk = []
        self.populate_stack(root)

    def populate_stack(self, node):
        while node:
            self.stk.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stk.pop()
        if node.right:
            self.populate_stack(node.right)
        return node.val

    def hasNext(self) -> bool:
        return len(self.stk) > 0


def listToNode(nums) -> Node:
    node_map = {}
    for i, num in enumerate(nums):
        if num is None:
            node_map[i] = None
        else:
            node = Node(num)
            node_map[i] = node

    for i, num in enumerate(nums):
        left = 2*i + 1
        right = left + 1
        if left < len(nums) and left in node_map:
            node_map[i].left = node_map[left]
        if right < len(nums) and right in node_map:
            node_map[i].right = node_map[right]
    return node_map[0]

def listToTreeNode(nums) -> TreeNode:
    node_map = {}
    for i, num in enumerate(nums):
        if num is None:
            node_map[i] = None
        else:
            node = TreeNode(num)
            node_map[i] = node

    for i, num in enumerate(nums):
        left = 2*i + 1
        right = left + 1
        if left < len(nums) and left in node_map:
            node_map[i].left = node_map[left]
        if right < len(nums) and right in node_map:
            node_map[i].right = node_map[right]
    return node_map[0]

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root:
            if root.val == val:
                return root
            elif root.val > val:
                root = root.left
            else:
                root = root.right
        return None

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return TreeNode(val)

        node = root
        while node:
            if node.val > val:
                if node.left:
                    node = node.left
                else:
                    node.left = TreeNode(val)
                    break
            else:
                if node.right:
                    node = node.right
                else:
                    node.right = TreeNode(val)
                    break
        return root

    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root or root.val == key: return None

        node = root
        prev = None
        while node:
            if node.val > key:
                prev = node
                node = node.left
            elif node.val < key:
                prev = node
                node = node.right

    def inorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        if not root: return result

        def traverse(node):
            if not node:
                return

            if node.left:
                traverse(node.left)
            result.append(node.val)

            if node.right:
                traverse(node.right)

        traverse(root)
        return result

    def inorderTraversal_iterative(self, root: TreeNode) -> list[int]:
        result = []
        stack = [root]

        while root or stack:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            result.append(root.val)
            root = root.right
        return result

    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        if not root: return []

        direction = 1  # 1 left->right, -1 right->left
        result = []
        q = deque([root])

        while q:
            level_result = deque([])
            for _ in range(len(q)):
                node = q.popleft()

                if direction == 1:
                    level_result.append(node.val)
                else:
                    level_result.appendleft(node.val)

                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            result.append(list(level_result))
            direction *= -1
        return result

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stk = []
        cntr = 0
        while root or stk:
            while root:
                stk.append(root)
                root = root.left

            root = stk.pop()
            cntr += 1

            if cntr == k:
                return root.val
            else:
                root = root.right

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        successor = None
        while root:
            if root.val == p.val:
                if root.right:
                    successor = root.right
                    while successor and successor.left:
                        successor = successor.left
                    return successor
                else:
                    return successor
            elif root.val > p.val:
                successor = root
                root = root.left
            else:
                root = root.right
        return successor


    def numIslands(self, grid: list[list[str]]) -> int:
        LAND, WATER = '1', '0'
        rows, cols = len(grid), len(grid[0])
        cnt = 0

        def sink_island(row, col):
            if not (0 <= row < rows) or not (0 <= col < cols) or grid[row][col] == WATER:
                return

            grid[row][col] = WATER
            sink_island(row, col+1)
            sink_island(row, col-1)
            sink_island(row+1, col)
            sink_island(row-1, col)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == LAND:
                    cnt += 1
                    sink_island(r, c)

        for row in grid:
            print(row)

        return cnt

    def letterCombinations(self, digits: str) -> list[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        results = []

        def dfs(curr_str, digit_index):
            if len(curr_str) == len(digits):
                results.append(curr_str)
            else:
                for letter in phone[digits[digit_index]]:
                    dfs(curr_str+letter, digit_index+1)

        dfs('', 0)
        return results

    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        if n <= 0: return result

        def add_parenthesis(curr_str, open_cnt, closed_cnt):
            if closed_cnt == n:
                result.append(curr_str)
            else:
                if open_cnt < n:
                    add_parenthesis(curr_str+'(', open_cnt+1, closed_cnt)
                if closed_cnt < open_cnt:
                    add_parenthesis(curr_str+')', open_cnt, closed_cnt+1)

        add_parenthesis('', 0, 0)
        return result

    def permute(self, nums: list[int]) -> list[list[int]]:
        if not nums or len(nums) == 1: return []

        res = []
        q = deque([[]])
        for i in range(0, len(nums)):
            curr = q.popleft()
            for j in range(len(curr)+1):
                copy_curr = curr.copy()
                copy_curr.insert(j, nums[i])

                if len(copy_curr) < len(nums):
                    q.append(copy_curr)
                else:
                    res.append(copy_curr)
        return res

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        in_degree_map = {i:0 for i in range(numCourses)}
        adj_graph = {i:[] for i in range(numCourses)}

        for parent, child in prerequisites:
            in_degree_map[child] += 1
            adj_graph[parent].append(child)

        q = deque()
        for course, in_degree in in_degree_map.items():
            if in_degree == 0:
                q.append(course)

        cnt = 0
        while q:
            parent_course = q.popleft()
            cnt += 1

            for child_course in adj_graph[parent_course]:
                in_degree_map[child_course] -= 1
                if in_degree_map[child_course] == 0:
                    q.append(child_course)
        return cnt >= numCourses

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca_node: TreeNode or None = None
        pass

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0

        def depth(node):
            nonlocal diameter
            if not node: return 0

            left = depth(node.left)
            right = depth(node.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1

        diameter = 0
        depth(root)
        return diameter

    def floodFill(self, image: list[list[int]], sr: int, sc: int, new_color: int) -> list[list[int]]:
        if not image: return image

        def fill(x, y, orig_color):
            if x >= len(image) \
                    or x < 0 \
                    or y >= len(image[x]) \
                    or y < 0 \
                    or image[x][y] != orig_color \
                    or new_color == orig_color:
                return
            else:
                image[x][y] = new_color
                fill(x, y+1, orig_color)
                fill(x, y-1, orig_color)
                fill(x-1, y, orig_color)
                fill(x+1, y, orig_color)

        fill(sr, sc, image[sr][sc])
        return image

    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        if not matrix: return 0

        def traverse(i, j, prev):
            nonlocal max_increasing_path_len

            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and (matrix[i][j] > prev or prev == float('-inf')):
                if memo[i][j] == float('-inf'):
                    left = traverse(i, j+1, matrix[i][j]) + 1
                    right = traverse(i, j-1, matrix[i][j]) + 1
                    up = traverse(i+1, j, matrix[i][j]) + 1
                    down = traverse(i-1, j, matrix[i][j]) + 1
                    memo[i][j] = max(left, right, up, down)

                max_increasing_path_len = max(max_increasing_path_len, memo[i][j])
                return memo[i][j]
            else:
                return 0

        max_increasing_path_len = 0
        memo = [[float('-inf') for j in range(len(matrix[0]))] for i in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                traverse(i, j, float('-inf'))
        return max_increasing_path_len

    def calcEquation(self, equations: list[list[str]], values: list[float], queries: list[list[str]]) -> list[float]:
        pass

    def cleanRoom(self, robot: Robot):
        """
        :type robot: Robot
        :rtype: None
        """

    def alienOrder(self, words: list[str]) -> str:
        in_deg = {c:0 for word in words for c in word}
        adj_graph = {c:[] for word in words for c in word}
        for i in range(len(words)):
            for l in range(i+1, len(words)):
                word = words[i]
                next_word = words[l]
                if word == next_word:
                    continue
                j, k = 0, 0
                while j < len(word) and k < len(next_word):
                    if word[j] == next_word[k]:
                        j += 1
                        k += 1
                        if k >= len(next_word):
                            return ""
                    elif next_word[k] not in adj_graph[word[j]]:
                        adj_graph[word[j]].append(next_word[k])
                        in_deg[next_word[k]] += 1
                        break
                    else:
                        break

        que = deque([])
        for char, in_degree in in_deg.items():
            if in_degree == 0:
                que.append(char)

        result = ""
        while que:
            char = que.popleft()
            result += char
            for child in adj_graph[char]:
                in_deg[child] -= 1
                if in_deg[child] == 0:
                    que.append(child)

        if len(result) != len(in_deg):
            return ""
        return result

    def treeToDoublyList(self, root: Node) -> Node:
        if not root:
            return root
        stk = []
        node = root

        head, tail, prev = None, None, None
        while stk or node:
            while node:
                stk.append(node)
                node = node.left

            node = stk.pop()
            if not head:
                head = node

            if not node.right and not stk:
                tail = node

            node.left = prev
            if prev:
                prev.right = node
            prev = node
            node = node.right

        head.left = tail
        tail.right = head
        return head

    # TODO: Come back to
    def isBipartite(self, graph: list[list[int]]) -> bool:
        if not graph: return True
        s1, s2 = set(), set()

        set_number = 1
        q = deque([0])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if set_number == 1:
                    s1.add(node)
                else:
                    s2.add(node)

                for child in graph[node]:
                    if child not in s1 and child not in s2:
                        q.append(child)
            set_number *= -1
        print(s1)
        print(s2)
        return s1.isdisjoint(s2)


class UnionFind:
    def __init__(self):
        self.f = {}

    def find(self, x):
        y = self.f.get(x, x)
        if y != x:
            self.f[x] = y = self.find(y)
        return y

    def union(self, x, y):
        self.f[self.find(x)] = self.find(y)


uf = UnionFind()
uf.union(1,2)
print(uf.find(1))
print(uf.find(2))
uf.union(1,4)
uf.union(3,4)
