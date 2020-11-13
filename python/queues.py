import collections
from typing import List


class MyStackQueue:
    """
    Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

    Implement the MyQueue class:
    void push(int x) Pushes element x to the back of the queue.
    int pop() Removes the element from the front of the queue and returns it.
    int peek() Returns the element at the front of the queue.
    boolean empty() Returns true if the queue is empty, false otherwise.

    Notes:
    You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
    Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you
    use only a stack's standard operations.

    Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity?
    In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """


    def peek(self) -> int:
        """
        Get the front element.
        """


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.__queue = [0] * k
        self.__start: int = 0
        self.__end: int = 0
        self.__size: int = 0

    @property
    def size(self) -> int:
        return self.__size

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False

        if self.isEmpty():
            self.__queue[0] = value
            self.__start, self.__end = 0, 0

        elif self.__end == len(self.__queue) - 1:
            self.__queue[0] = value
            self.__end = 0

        else:
            self.__queue[self.__end + 1] = value
            self.__end += 1

        self.__size += 1
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.__queue[self.__start] = 0
        if self.__start == len(self.__queue) - 1:
            self.__start = 0
        else:
            self.__start += 1

        self.__size -= 1
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.__queue[self.__start]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        else:
            return self.__queue[self.__end]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.__size == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.__size == len(self.__queue)


class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.__que = collections.deque(maxlen=size)

    def next(self, val: int) -> float:
        """
        Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
        Ex: MovingAverage m = new MovingAverage(3);
            m.next(1) = 1
            m.next(10) = (1 + 10) / 2
            m.next(3) = (1 + 10 + 3) / 3
            m.next(5) = (10 + 3 + 5) / 3
        """
        self.__que.append(val)
        return sum(self.__que) / len(self.__que)


class Queues:
    ROOM = 2 ** 31 - 1
    GATE = 0
    WALL = -1

    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        You are given a m x n 2D grid initialized with these three possible values.

        -1 - A wall or an obstacle.
        0 - A gate.
        INF - 2**31 - 1 = 2147483647

        Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.
        Example:

        Given the 2D grid:
        INF  -1  0  INF
        INF INF INF  -1
        INF  -1 INF  -1
          0  -1 INF INF

        After running your function, the 2D grid should be:
          3  -1   0   1
          2   2   1  -1
          1  -1   2  -1
          0  -1   3   4
        """
        if not rooms: return

        q = collections.deque()
        rows = len(rooms)
        cols = len(rooms[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for row in range(rows):
            for col in range(cols):
                if rooms[row][col] == self.GATE:
                    q.append((row, col))

        while len(q) > 0:
            row, col = q.popleft()
            for x, y in directions:
                if row + x < 0 or row + x >= rows or col + y < 0 or col + y >= cols or rooms[row + x][col + y] != self.ROOM:
                    continue
                rooms[row + x][col + y] = rooms[row + x][col + y] + 1
                q.append((row + x, col + y))

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

        q = collections.deque()
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        count = 0
        rows = len(grid)
        cols = len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    count += 1
                    q.append((row, col))
                    while len(q) > 0:
                        r, c = q.popleft()
                        for x, y in directions:
                            r_next, c_next = r + x, c + y
                            if 0 <= r_next < rows and 0 <= c_next < cols and grid[r_next][c_next] == "1":
                                grid[r_next][c_next] = "0"
                                q.append((r_next, c_next))
        return count

    def openLock(self, deadends: List[str], target: str) -> int:
        """
        You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'.
        The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'.
        Each move consists of turning one wheel one slot. The lock initially starts at '0000', a string representing the state of the 4 wheels.

        You are given a list of deadends dead ends, meaning if the lock displays any of these codes,
        the wheels of the lock will stop turning and you will be unable to open it.

        Given a target representing the value of the wheels that will unlock the lock,
        return the minimum total number of turns required to open the lock, or -1 if it is impossible.

        Ex1:
        Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
        Output: 6
        Explanation: A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
                     Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
                     because the wheels of the lock become stuck after the display becomes the dead end "0102".

        Ex2:
        Input: deadends = ["8888"], target = "0009"
        Output: 1
        Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009"
        """
        def neighbors(node):
            for i in range(4):
                x = int(node[i])
                for d in [-1, 1]:
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i+1:]

    def numSquares(self, n: int) -> int:
        """
        Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

        Example 1:
        Input: n = 12
        Output: 3
        Explanation: 12 = 4 + 4 + 4.

        Input: n = 13
        Output: 2
        Explanation: 13 = 4 + 9.
        """
        a = [1]
        a.__reversed__()

print(Queues().numSquares(12))