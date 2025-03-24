# Algorithm Templates

> A curated collection of essential algorithm patterns and templates for problem solving. Each template includes implementation, time/space complexity, and common applications.

## Table of Contents

- [Algorithm Templates](#algorithm-templates)
  - [Table of Contents](#table-of-contents)
  - [1. Two Pointers](#1-two-pointers)
  - [2. Sliding Window](#2-sliding-window)
    - [Fixed Size Window](#fixed-size-window)
    - [Flexible Size - Find Longest](#flexible-size---find-longest)
    - [Flexible Size - Find Shortest](#flexible-size---find-shortest)
  - [3. Breadth First Search (BFS)](#3-breadth-first-search-bfs)
    - [Tree BFS](#tree-bfs)
    - [Graph BFS](#graph-bfs)
    - [BFS with Level Tracking](#bfs-with-level-tracking)
  - [4. Depth First Search (DFS)](#4-depth-first-search-dfs)
    - [Tree DFS](#tree-dfs)
    - [Graph DFS](#graph-dfs)
  - [5. Backtracking](#5-backtracking)
    - [Basic Template](#basic-template)
    - [Aggregation Template](#aggregation-template)
    - [Common Aggregation Patterns](#common-aggregation-patterns)
  - [6. Binary Search](#6-binary-search)
  - [7. Heap](#7-heap)
  - [8. Matrix as Graph](#8-matrix-as-graph)
  - [9. Monotonic Stack](#9-monotonic-stack)
  - [10. Topological Sort](#10-topological-sort)
  - [11. Trie](#11-trie)
  - [12. Union Find (Disjoint Set)](#12-union-find-disjoint-set)
    - [Basic Implementation](#basic-implementation)
    - [Optimized with Rank](#optimized-with-rank)
  - [13. Kadane's Algorithm](#13-kadanes-algorithm)
  - [14. Prefix Sums](#14-prefix-sums)
  - [15. Fast \& Slow Pointers](#15-fast--slow-pointers)
  - [16. Linked List Reversal](#16-linked-list-reversal)
  - [17. Dijkstra's Algorithm](#17-dijkstras-algorithm)
  - [18. 0/1 Knapsack Pattern](#18-01-knapsack-pattern)
  - [19. Unbounded Knapsack Pattern](#19-unbounded-knapsack-pattern)
  - [20. Longest Common Subsequence (LCS) Pattern](#20-longest-common-subsequence-lcs-pattern)
  - [21. Fibonacci Sequence Pattern](#21-fibonacci-sequence-pattern)
  - [22. Subsets Pattern](#22-subsets-pattern)
  - [23. Constraint Satisfaction Pattern](#23-constraint-satisfaction-pattern)
  - [24. Top K Elements Pattern](#24-top-k-elements-pattern)
  - [25. Two Heaps Pattern](#25-two-heaps-pattern)
  - [26. Bit Manipulation](#26-bit-manipulation)
  - [27. Greedy Algorithms](#27-greedy-algorithms)

---

## 1. Two Pointers

A technique where two pointers iterate through data structures in a coordinated way.

**When to use**:

- Processing arrays or linked lists in linear time
- Finding pairs with certain constraints
- Merging sorted arrays

```python
def two_pointers(arr):
    left, right = 0, len(arr) - 1
    result = []

    while left < right:
        if condition(arr[left], arr[right]):
            # Process result
            result.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif needs_left_increment(arr[left], arr[right]):
            left += 1
        else:
            right -= 1

    return result
```

**Time Complexity**: O(n) for most implementations
**Space Complexity**: O(1) excluding output storage

**Example Use Cases**:

- Two Sum problems
- Container with most water
- Remove duplicates from sorted array

---

## 2. Sliding Window

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

## 5. Backtracking

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

| Problem Type          | Initial Value | Aggregation Function |
| --------------------- | ------------- | -------------------- |
| Existence/Possibility | False         | OR (∥)              |
| Count ways            | 0             | Addition (+)         |
| Optimize (max/min)    | 0/-∞/∞      | max()/min()          |

**Time Complexity**: O(k^n) where k is the branching factor and n is the depth
**Space Complexity**: O(n) for recursion stack

**Example Use Cases**:

- N-Queens
- Subset/Combination Sum problems
- Permutations

---

## 6. Binary Search

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

## 7. Heap

A specialized tree-based data structure that satisfies the heap property.

**When to use**:

- Priority queue implementation
- Finding k largest/smallest elements
- Efficient median tracking

```python
import heapq

def heap_operations():
    # Min heap (default in Python)
    min_heap = []
    heapq.heappush(min_heap, 5)
    heapq.heappush(min_heap, 3)
    heapq.heappush(min_heap, 7)

    # Get smallest element without removing
    smallest = min_heap[0]

    # Remove and return smallest element
    smallest = heapq.heappop(min_heap)

    # Max heap (negate values)
    max_heap = []
    heapq.heappush(max_heap, -5)
    heapq.heappush(max_heap, -3)
    heapq.heappush(max_heap, -7)

    # Get largest element without removing
    largest = -max_heap[0]

    # Remove and return largest element
    largest = -heapq.heappop(max_heap)

    # Convert list to heap in-place
    arr = [5, 3, 7, 1, 9]
    heapq.heapify(arr)  # Now arr is a min heap

    # K largest elements
    k_largest = heapq.nlargest(3, arr)

    # K smallest elements
    k_smallest = heapq.nsmallest(3, arr)
```

**Time Complexity**:

- Push/Pop: O(log n)
- Peek: O(1)
- Heapify: O(n)
- K largest/smallest: O(n + k log n)

**Space Complexity**: O(n)

**Example Use Cases**:

- Dijkstra's algorithm
- K closest points
- Merge k sorted lists

---

## 8. Matrix as Graph

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

## 9. Monotonic Stack

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

## 10. Topological Sort

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

## 11. Trie

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

## 12. Union Find (Disjoint Set)

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

---

## 13. Kadane's Algorithm

A dynamic programming approach to find the maximum subarray sum.

**When to use**:

- Finding maximum/minimum sum subarray
- Requiring contiguous elements with optimal value
- When greedy approach with local/global optimal values works

```python
def kadanes_algorithm(arr):
    # Handle the case of all negative numbers
    if all(x < 0 for x in arr):
        return max(arr)

    max_so_far = 0
    max_ending_here = 0

    for num in arr:
        max_ending_here = max(0, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Variation that handles all negative arrays
def kadanes_general(arr):
    if not arr:
        return 0

    max_so_far = arr[0]
    max_ending_here = arr[0]

    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

**Example Use Cases**:

- Maximum sum subarray
- Maximum product subarray
- Circular array maximum sum

---

## 14. Prefix Sums

A preprocessing technique for efficient range sum queries.

**When to use**:

- Range sum queries
- Cumulative operations on arrays
- Checking for specific sum conditions over subarrays

```python
def prefix_sums(arr):
    prefix = [0] * (len(arr) + 1)

    for i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]

    return prefix

def range_sum(prefix, left, right):
    # Sum of elements from index left to right (inclusive)
    return prefix[right + 1] - prefix[left]

# Example using prefix sums to find subarrays with sum equal to k
def count_subarrays_with_sum(arr, k):
    prefix_sum = 0
    count = 0
    sum_counts = {0: 1}  # Empty subarray has sum 0

    for num in arr:
        prefix_sum += num
        # If (prefix_sum - k) exists, there is a subarray with sum k
        if prefix_sum - k in sum_counts:
            count += sum_counts[prefix_sum - k]

        # Increment count of current prefix sum
        sum_counts[prefix_sum] = sum_counts.get(prefix_sum, 0) + 1

    return count
```

**Time Complexity**:
- Preprocessing: O(n)
- Range queries: O(1)

**Space Complexity**: O(n) for storing prefix sums

**Example Use Cases**:

- Range sum queries
- Subarray sum equals K
- Count number of subarrays with specific properties

---

## 15. Fast & Slow Pointers

A two-pointer technique where one pointer moves faster than the other.

**When to use**:

- Cycle detection problems
- Finding middle element in a linked list
- Finding nth element from the end
- Detecting palindrome linked lists

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_cycle(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head

    # If there is a cycle, fast will eventually catch up to slow
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:  # Cycle detected
            return True

    return False

def find_cycle_start(head):
    if not head or not head.next:
        return None

    # Phase 1: Detect cycle
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:  # Cycle detected
            break

    # No cycle found
    if not fast or not fast.next:
        return None

    # Phase 2: Find entrance to cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # Cycle start node

def find_middle(head):
    if not head:
        return None

    slow = head
    fast = head

    # When fast reaches the end, slow is at the middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow  # Middle node
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

**Example Use Cases**:

- Detect cycle in linked list
- Find cycle start point
- Find middle of linked list
- Palindrome linked list

---

## 16. Linked List Reversal

A common pattern for manipulating linked list orders.

**When to use**:

- Problems requiring reversal of all or part of a linked list
- Problems involving K-groups or alternative reverse operations

```python
def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_temp = current.next  # Store next node
        current.next = prev       # Reverse pointer
        prev = current            # Move prev forward
        current = next_temp       # Move current forward

    return prev  # New head

def reverse_sublist(head, start, end):
    # Create a dummy node for easier handling of edge cases
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move prev to the node just before the start position
    for _ in range(1, start):
        prev = prev.next

    current = prev.next  # Node at start position

    # Reverse nodes from start to end
    for _ in range(end - start):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    return dummy.next  # New head

def reverse_k_group(head, k):
    count = 0
    curr = head

    # Count k nodes
    while curr and count < k:
        curr = curr.next
        count += 1

    # If we have k nodes, reverse them
    if count == k:
        # Reverse k nodes
        prev = reverse_k_group(curr, k)  # Reverse next k-group and get its head

        # Connect current k-group to the reversed next k-group
        while count > 0:
            next_temp = head.next
            head.next = prev
            prev = head
            head = next_temp
            count -= 1

        return prev  # New head of reversed k-group

    return head  # Less than k nodes left, return as is
```

**Time Complexity**: O(n)
**Space Complexity**: O(1) for iterative solutions, O(n) for recursive solutions

**Example Use Cases**:

- Reverse linked list
- Reverse nodes in K-group
- Reverse alternating K elements

---

## 17. Dijkstra's Algorithm

A greedy algorithm for finding the shortest path in a weighted graph.

**When to use**:

- Finding shortest path in weighted graph with non-negative weights
- Optimizing distance between nodes
- Pathfinding with cost considerations
- Network routing problems with weights

```python
import heapq

def dijkstra(graph, start):
    # Initialize distances with infinity for all nodes except start
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Priority queue to process nodes by current distance
    priority_queue = [(0, start)]

    # Track visited nodes
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if we've already processed this node
        if current_node in visited:
            continue

        # Mark as visited
        visited.add(current_node)

        # Process all neighbors
        for neighbor, weight in graph[current_node].items():
            # Skip visited neighbors
            if neighbor in visited:
                continue

            # Calculate distance to neighbor through current node
            distance = current_distance + weight

            # If we found a shorter path, update distance
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph representation (adjacency list with weights)
# graph = {
#     'A': {'B': 1, 'C': 4},
#     'B': {'A': 1, 'C': 2, 'D': 5},
#     'C': {'A': 4, 'B': 2, 'D': 1},
#     'D': {'B': 5, 'C': 1}
# }
```

**Time Complexity**: O((V + E) log V) with binary heap implementation
**Space Complexity**: O(V)

**Example Use Cases**:

- Network routing
- GPS navigation
- Flight scheduling
- Network Delay Time

---

## 18. 0/1 Knapsack Pattern

A dynamic programming approach for selecting items with maximum value under a weight constraint.

**When to use**:

- Discrete items with values/weights
- Binary decisions (include/exclude)
- Maximizing/minimizing value with constraints

```python
def knapsack_01(values, weights, capacity):
    n = len(values)
    # Initialize DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # If current item weight is more than capacity, skip it
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Max of including or excluding current item
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],  # Include item
                    dp[i-1][w]  # Exclude item
                )

    return dp[n][capacity]

# Space-optimized version
def knapsack_01_optimized(values, weights, capacity):
    n = len(values)
    # Use 1D array since we only need previous row
    dp = [0 for _ in range(capacity + 1)]

    # Fill DP table
    for i in range(n):
        # Process in reverse to avoid overwriting values we still need
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    return dp[capacity]
```

**Time Complexity**: O(n * C) where n is items, C is capacity
**Space Complexity**: O(n * C), can be optimized to O(C)

**Example Use Cases**:

- 0/1 Knapsack
- Subset Sum
- Equal Subset Sum Partition
- Minimum Subset Sum Difference

---

## 19. Unbounded Knapsack Pattern

A variation of the knapsack problem where items can be used multiple times.

**When to use**:

- Items can be used multiple times
- Selecting repeated elements with constraints
- Max/min value problems with unlimited supply

```python
def unbounded_knapsack(values, weights, capacity):
    # Initialize DP table
    dp = [0] * (capacity + 1)

    # Fill DP table
    for w in range(1, capacity + 1):
        for i in range(len(values)):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]

# Coin change problem (minimizing number of coins)
def coin_change(coins, amount):
    # Initialize with infinity for all amounts except 0
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

# Coin change (count number of ways)
def count_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1  # There is 1 way to make amount 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]
```

**Time Complexity**: O(n * C) where n is item types, C is capacity
**Space Complexity**: O(C)

**Example Use Cases**:

- Coin Change (min coins)
- Coin Change II (number of ways)
- Rod Cutting
- Maximum ribbon cut

---

## 20. Longest Common Subsequence (LCS) Pattern

A dynamic programming approach for finding common elements between sequences.

**When to use**:

- Problems comparing sequences
- Finding common elements or differences between strings
- Edit distance variations

```python
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)

    # Create DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]

# Variation: Edit distance
def edit_distance(word1, word2):
    m, n = len(word1), len(word2)

    # Create DP table
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )

    return dp[m][n]
```

**Time Complexity**: O(m * n) where m, n are string lengths
**Space Complexity**: O(m * n)

**Example Use Cases**:

- Longest Common Subsequence
- Shortest Common Supersequence
- Edit Distance
- Longest Palindromic Subsequence

---

## 21. Fibonacci Sequence Pattern

A dynamic programming pattern where the current state depends on previous states.

**When to use**:

- Problems with recursive relation f(n) = f(n-1) + f(n-2)
- Current state depends on 1-2 previous states
- Counting distinct ways to reach a target

```python
# Basic Fibonacci (Top-down with memoization)
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

# Bottom-up approach (tabulation)
def fibonacci_tabulation(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

# Space-optimized version
def fibonacci_optimized(n):
    if n <= 1:
        return n

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b

    return b

# Example: Climbing stairs problem
def climb_stairs(n):
    if n <= 2:
        return n

    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b

    return b
```

**Time Complexity**: O(n)
**Space Complexity**: O(n) can be optimized to O(1)

**Example Use Cases**:

- Fibonacci Numbers
- Climbing Stairs
- House Thief (non-adjacent elements)
- Jump Game variations

---

## 22. Subsets Pattern

A backtracking approach for generating combinations of elements.

**When to use**:

- Generating all possible subsets/combinations/permutations
- Need to explore multiple choices at each step
- Building combinations with specific constraints

```python
def generate_subsets(nums):
    result = []

    def backtrack(start, current):
        # Add the current subset to the result
        result.append(current[:])

        # Try including each remaining element
        for i in range(start, len(nums)):
            # Include nums[i]
            current.append(nums[i])
            # Recurse with next position
            backtrack(i + 1, current)
            # Backtrack (exclude nums[i])
            current.pop()

    backtrack(0, [])
    return result

def generate_permutations(nums):
    result = []

    def backtrack(start):
        # If we've used all numbers, add permutation to result
        if start == len(nums):
            result.append(nums[:])
            return

        # Try each number at the current position
        for i in range(start, len(nums)):
            # Swap to place nums[i] at position start
            nums[start], nums[i] = nums[i], nums[start]
            # Recurse with next position
            backtrack(start + 1)
            # Backtrack (restore original order)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    return result

def combination_sum(candidates, target):
    result = []

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return
        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])  # Can reuse same element
            current.pop()

    backtrack(0, [], target)
    return result
```

**Time Complexity**: O(2^n) for subsets, O(n!) for permutations
**Space Complexity**: O(n) for recursion stack

**Example Use Cases**:

- Generate Subsets/Powerset
- Permutations
- Combinations
- Letter Combinations of Phone Number

---

## 23. Constraint Satisfaction Pattern

A backtracking approach for problems with complex constraints.

**When to use**:

- Problems with complex constraints
- Search space can be pruned early
- Need to find all valid solutions or one valid solution

```python
# Example: Sudoku Solver
def solve_sudoku(board):
    # Find an empty cell
    def find_empty():
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    return r, c
        return None

    # Check if num can be placed at (row, col)
    def is_valid(row, col, num):
        # Check row
        for c in range(9):
            if board[row][c] == num:
                return False

        # Check column
        for r in range(9):
            if board[r][col] == num:
                return False

        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if board[r][c] == num:
                    return False

        return True

    def backtrack():
        # Find an empty cell
        empty = find_empty()
        if not empty:
            return True  # Solved

        row, col = empty

        # Try each possible number
        for num in '123456789':
            if is_valid(row, col, num):
                # Place number
                board[row][col] = num

                # Recurse
                if backtrack():
                    return True

                # Backtrack
                board[row][col] = '.'

        return False  # No solution

    backtrack()
    return board

# Example: N-Queens
def solve_n_queens(n):
    result = []

    # Initialize empty board
    board = [['.' for _ in range(n)] for _ in range(n)]

    # Check if a queen can be placed at (row, col)
    def is_safe(row, col):
        # Check column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True

    def backtrack(row):
        if row == n:
            # Add current board state to result
            result.append([''.join(row) for row in board])
            return

        for col in range(n):
            if is_safe(row, col):
                # Place queen
                board[row][col] = 'Q'

                # Recurse to next row
                backtrack(row + 1)

                # Backtrack
                board[row][col] = '.'

    backtrack(0)
    return result
```

**Time Complexity**: Exponential, but pruning reduces actual runtime
**Space Complexity**: O(n) for recursion stack

**Example Use Cases**:

- N-Queens
- Sudoku Solver
- Word Search
- Palindrome Partitioning

---

## 24. Top K Elements Pattern

A heap-based pattern for finding the most frequent or largest elements.

**When to use**:

- Finding top/smallest K elements
- Stream processing with limited memory
- Maintaining a running set of maximum/minimum elements

```python
import heapq

def find_k_largest(nums, k):
    # Use a min heap of size k
    min_heap = []

    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    return min_heap

def top_k_frequent(nums, k):
    # Count frequency
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1

    # Use min heap to keep track of k most frequent elements
    min_heap = []

    for num, count in counter.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (count, num))
        elif count > min_heap[0][0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, (count, num))

    # Extract result
    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap)[1])

    # Reverse to get highest frequency first
    return result[::-1]

def k_closest_points(points, k):
    # Use max heap to keep k closest points
    max_heap = []

    for x, y in points:
        # Calculate distance (no need for square root)
        dist = x*x + y*y

        if len(max_heap) < k:
            # Negate distance for max heap
            heapq.heappush(max_heap, (-dist, [x, y]))
        elif -dist > max_heap[0][0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-dist, [x, y]))

    # Extract result
    return [point for _, point in max_heap]
```

**Time Complexity**: O(n log k) for processing n elements with heap of size k
**Space Complexity**: O(k) for the heap

**Example Use Cases**:

- Kth Largest Element
- K Closest Points to Origin
- Top K Frequent Elements
- Sort K-sorted Array

---

## 25. Two Heaps Pattern

A pattern for problems requiring tracking of median elements.

**When to use**:

- Median calculation problems
- Balancing elements on either side of a midpoint
- Processing stream data with statistics

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max-heap for smaller half
        self.large = []  # Min-heap for larger half

    def addNum(self, num):
        # Add to max_heap
        heapq.heappush(self.small, -num)

        # Balance heaps: ensure max of small <= min of large
        # Move largest element from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Ensure small has at least as many elements as large
        if len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2.0

class SlidingWindowMedian:
    def __init__(self):
        self.max_heap = []  # For smaller half
        self.min_heap = []  # For larger half

    def find_sliding_window_median(self, nums, k):
        result = []

        for i, num in enumerate(nums):
            # Add new element
            self.add_num(num)

            # Remove element outside window
            if i >= k:
                self.remove_num(nums[i - k])

            # Calculate median once window is full
            if i >= k - 1:
                result.append(self.find_median())

        return result

    def add_num(self, num):
        # Add to max_heap
        heapq.heappush(self.max_heap, -num)

        # Balance heaps
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Ensure max_heap has at least as many elements as min_heap
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def remove_num(self, num):
        # Remove from proper heap
        if num <= -self.max_heap[0]:
            self.max_heap.remove(-num)
            heapq.heapify(self.max_heap)
        else:
            self.min_heap.remove(num)
            heapq.heapify(self.min_heap)

        # Rebalance if needed
        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def find_median(self):
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
```

**Time Complexity**: O(log n) per element insertion
**Space Complexity**: O(n) for storing all elements

**Example Use Cases**:

- Find Median from Data Stream
- Sliding Window Median
- IPO (maximize capital)

---

## 26. Bit Manipulation

A set of techniques for manipulating individual bits in integers.

**When to use**:

- Problems involving binary representation
- XOR, AND, OR operations
- Problems requiring space optimization
- Numeric problems that can exploit bit properties

```python
# Common bit manipulation operations
def bit_operations():
    # Basic operations
    a = 5   # 101 in binary
    b = 3   # 011 in binary

    # Bitwise AND
    bit_and = a & b       # 001 = 1

    # Bitwise OR
    bit_or = a | b        # 111 = 7

    # Bitwise XOR (exclusive OR)
    bit_xor = a ^ b       # 110 = 6

    # Bitwise NOT (complement)
    bit_not = ~a          # ...11010 = -6 (depends on bit width)

    # Left shift
    left_shift = a << 1   # 1010 = 10

    # Right shift
    right_shift = a >> 1  # 10 = 2

    return bit_and, bit_or, bit_xor, bit_not, left_shift, right_shift

# Counting bits in a number
def count_bits(n):
    count = 0
    while n:
        count += n & 1  # Check if least significant bit is 1
        n >>= 1         # Right shift by 1
    return count

# Power of two check
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# XOR to find single number among duplicates
def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Setting, clearing, and checking bits
def set_bit(num, i):
    return num | (1 << i)

def clear_bit(num, i):
    return num & ~(1 << i)

def toggle_bit(num, i):
    return num ^ (1 << i)

def check_bit(num, i):
    return (num >> i) & 1
```

**Time Complexity**: O(1) to O(n) depending on problem
**Space Complexity**: Usually O(1)

**Example Use Cases**:

- Counting bits
- Finding single number among duplicates
- Power set generation via bits
- Bit manipulation tricks

---

## 27. Greedy Algorithms

A technique where local optima are chosen at each step to find a global optimum.

**When to use**:

- Local optimal choice leads to global optimum
- Problems where you can make choices without reconsidering
- Optimization problems with "obvious" next steps

```python
# Activity selection problem
def activity_selection(start, finish):
    # Sort activities by finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    selected = [activities[0]]
    last_finish = activities[0][1]

    for i in range(1, len(activities)):
        # If current activity starts after the finish of last selected activity
        if activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]

    return selected

# Minimum number of intervals to remove to make rest non-overlapping
def erase_overlap_intervals(intervals):
    if not intervals:
        return 0

    # Sort by end time
    intervals.sort(key=lambda x: x[1])

    end = intervals[0][1]
    count = 1  # Count of non-overlapping intervals

    for i in range(1, len(intervals)):
        if intervals[i][0] >= end:
            # Current interval doesn't overlap with previous
            end = intervals[i][1]
            count += 1

    # Return number of intervals to remove
    return len(intervals) - count

# Jump Game - determine if you can reach the end
def can_jump(nums):
    max_reach = 0

    for i in range(len(nums)):
        # If current position is beyond max reach, we can't get here
        if i > max_reach:
            return False

        # Update max reach from current position
        max_reach = max(max_reach, i + nums[i])

        # If we can reach the end, return early
        if max_reach >= len(nums) - 1:
            return True

    return max_reach >= len(nums) - 1
```

**Time Complexity**: Usually O(n log n) due to sorting
**Space Complexity**: Usually O(1) or O(n)

**Example Use Cases**:

- Activity selection
- Huffman coding
- Fractional knapsack
- Interval scheduling
