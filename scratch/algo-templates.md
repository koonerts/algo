# Algorithm Templates

> A curated collection of essential algorithm patterns and templates for problem solving. Each template includes implementation, time/space complexity, and common applications.

## Table of Contents
1. [Backtracking](#1-backtracking)
2. [Binary Search](#2-binary-search)
3. [Breadth First Search (BFS)](#3-breadth-first-search-bfs)
4. [Depth First Search (DFS)](#4-depth-first-search-dfs)
5. [Matrix as Graph](#5-matrix-as-graph)
6. [Monotonic Stack](#6-monotonic-stack)
7. [Sliding Window](#7-sliding-window)
8. [Topological Sort](#8-topological-sort)
9. [Trie](#9-trie)
10. [Union Find (Disjoint Set)](#10-union-find-disjoint-set)

---

## 1. Backtracking

Backtracking is a systematic way to explore all potential solutions through recursive trial and error.

**When to use**: 
- Generating all possible combinations/permutations
- Finding paths through a maze
- Constraint satisfaction problems (like Sudoku)

### Basic Template
```python
def backtrack(start_index, path):
    if is_leaf(start_index):  # Base case
        report(path)
        return

    for choice in get_choices(start_index):
        path.append(choice)      # Make choice
        backtrack(start_index + 1, path)  # Explore
        path.pop()               # Undo choice
```

### Aggregation Template
```python
def backtrack(index, state):
    # Base case
    if is_leaf(index):
        return 1

    result = initial_value

    for choice in get_choices(index, state):
        # Make choice and update state
        update_state(state, choice)

        # Explore and aggregate results
        result = aggregate(result, backtrack(index + 1, state))

        # Undo choice
        revert_state(state, choice)

    return result
```

### Common Aggregation Patterns

| Problem Type | Initial Value | Aggregation Function |
|--------------|---------------|---------------------|
| Existence/Possibility | False | OR (∥) |
| Count ways | 0 | Addition (+) |
| Optimize (max/min) | 0/-∞/∞ | max()/min() |

**Time Complexity**: O(k^n) where k is the branching factor and n is the depth
**Space Complexity**: O(n) for recursion stack

**Example Use Cases**: 
- N-Queens
- Subset/Combination Sum problems
- Permutations

---

## 2. Binary Search

A divide-and-conquer algorithm that finds elements in a sorted array in logarithmic time.

**When to use**:
- Searching in sorted arrays
- Finding the boundary between two distinct regions
- Optimizing minimum/maximum values that satisfy a condition

```python
def binary_search(arr):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if condition(arr[mid]):
            result = mid       # Potential answer
            right = mid - 1    # Search left for better answer
        else:
            left = mid + 1     # Search right

    return result
```

**Time Complexity**: O(log n)
**Space Complexity**: O(1)

**Example Use Cases**:
- Finding element in sorted array
- Finding first/last occurrence
- Search in rotated sorted array

---

## 3. Breadth First Search (BFS)

Explores all neighbors at the current depth before moving to nodes at the next depth level.

**When to use**:
- Finding shortest path in unweighted graphs
- Level-order traversal of trees
- Connected components in graphs

### Tree BFS
```python
from collections import deque

def bfs(root):
    if not root:
        return

    queue = deque([root])
    while queue:
        node = queue.popleft()
        # Process node
        for child in node.children:
            queue.append(child)
```

### Graph BFS
```python
from collections import deque

def bfs(start, graph):
    queue = deque([start])
    visited = {start}

    while queue:
        node = queue.popleft()
        # Process node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### BFS with Level Tracking
```python
from collections import deque

def bfs_by_level(start, graph):
    queue = deque([start])
    visited = {start}
    level = 0

    while queue:
        # Process entire level
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            # Process node at current level
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        level += 1
```

**Time Complexity**: O(V + E) where V is vertices and E is edges
**Space Complexity**: O(V)

**Example Use Cases**:
- Shortest path in maze
- Word ladder
- Web crawler

---

## 4. Depth First Search (DFS)

Explores as far as possible along each branch before backtracking.

**When to use**:
- Pathfinding
- Topological ordering
- Exploring all possibilities in a graph

### Tree DFS
```python
def dfs(root):
    if not root:
        return

    # Process root
    dfs(root.left)
    dfs(root.right)
```

### Graph DFS
```python
def dfs(node, graph, visited=None):
    if visited is None:
        visited = set()

    visited.add(node)
    # Process node

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)
```

**Time Complexity**: O(V + E) where V is vertices and E is edges
**Space Complexity**: O(V) in worst case

**Example Use Cases**:
- Cycle detection
- Connected components
- Solving mazes

---

## 5. Matrix as Graph

Treating a 2D grid as a graph with neighboring cells as connected nodes.

**When to use**:
- Pathfinding in grids/mazes
- Island/connected region problems
- Game board traversals

```python
def get_neighbors(row, col, matrix):
    # Four directions: Up, Right, Down, Left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    neighbors = []

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        # Check bounds
        if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
            neighbors.append((new_row, new_col))

    return neighbors
```

**Example Use Cases**:
- Number of islands
- Flood fill
- Shortest path in maze

---

## 6. Monotonic Stack

A stack that maintains elements in either increasing or decreasing order.

**When to use**:
- Finding the next greater/smaller element
- Problems involving histograms
- Trapping rain water

```python
def monotonic_increasing_stack(arr):
    stack = []  # Will maintain increasing order

    for i, val in enumerate(arr):
        # Pop elements greater than current
        while stack and stack[-1] > val:
            popped = stack.pop()
            # Process popped element

        stack.append(val)

    # Process remaining elements in stack if needed
```

**Time Complexity**: O(n) as each element is pushed and popped at most once
**Space Complexity**: O(n)

**Example Use Cases**:
- Next greater element
- Largest rectangle in histogram
- Daily temperatures

---

## 7. Sliding Window

Efficiently processes array segments of dynamic or fixed size by sliding a window.

**When to use**:
- Finding subarrays that meet certain criteria
- String problems with substring constraints
- Maximum/minimum subarray of fixed size

### Fixed Size Window
```python
def fixed_window(arr, k):
    # Process first window
    window_sum = sum(arr[:k])
    result = window_sum

    # Slide window
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Add new, remove old
        result = max(result, window_sum)

    return result
```

### Flexible Size - Find Longest
```python
def longest_window(arr, target):
    left = 0
    current_sum = 0
    max_length = 0

    for right in range(len(arr)):
        # Expand window
        current_sum += arr[right]

        # Shrink window until valid
        while current_sum > target:
            current_sum -= arr[left]
            left += 1

        # Update result if valid
        max_length = max(max_length, right - left + 1)

    return max_length
```

### Flexible Size - Find Shortest
```python
def shortest_window(arr, target):
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(arr)):
        # Expand window
        current_sum += arr[right]

        # Shrink window while valid
        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    return min_length if min_length != float('inf') else 0
```

**Time Complexity**: O(n) for most implementations
**Space Complexity**: O(1) for numeric windows, O(k) for string/object windows

**Example Use Cases**:
- Maximum sum subarray of size k
- Longest substring with k distinct characters
- Minimum window substring

---

## 8. Topological Sort

Ordering of vertices in a directed acyclic graph where for each edge (u,v), u comes before v.

**When to use**:
- Task scheduling with prerequisites
- Course scheduling
- Dependency resolution

```python
from collections import deque

def topological_sort(graph):
    # Calculate in-degrees
    indegree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            indegree[neighbor] += 1

    # Start with nodes that have no dependencies
    queue = deque([node for node, count in indegree.items() if count == 0])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Check if cycle exists
    return result if len(result) == len(graph) else None
```

**Time Complexity**: O(V + E)
**Space Complexity**: O(V)

**Example Use Cases**:
- Course prerequisites
- Build systems
- Parallel job scheduling

---

## 9. Trie

A tree-like data structure for efficient string search operations.

**When to use**:
- Prefix matching
- Autocomplete functionality
- Spell checkers

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count
```

**Time Complexity**:
- Insert: O(m) where m is word length
- Search: O(m) where m is word length
- Space Complexity: O(n*m) where n is number of words and m is average length

**Example Use Cases**:
- Word dictionary
- Autocomplete
- IP routing tables

---

## 10. Union Find (Disjoint Set)

Data structure for tracking elements partitioned into disjoint sets.

**When to use**:
- Finding connected components
- Cycle detection in undirected graphs
- Kruskal's algorithm for minimum spanning trees

### Basic Implementation
```python
class UnionFind:
    def __init__(self, n=0):
        self.parent = {}  # Maps element to its parent

    def find(self, x):
        # If x not in set yet, add it as its own parent
        if x not in self.parent:
            self.parent[x] = x

        # Find root of the set containing x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Connect x's set to y's set
        self.parent[self.find(x)] = self.find(y)

    def connected(self, x, y):
        return self.find(x) == self.find(y)
```

### Optimized with Rank
```python
class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return

        # Union by rank
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            if self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
```

**Time Complexity**:
- With path compression and union by rank:
  - Amortized O(α(n)) per operation, where α is the inverse Ackermann function (nearly constant)
- Without optimizations:
  - O(n) worst case per operation

**Example Use Cases**:
- Network connectivity
- Image segmentation
- Friends circles