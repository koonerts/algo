# Algorithm Templates

> A curated collection of essential algorithm patterns and templates FOR problem solving. Each template includes implementation, time/space complexity, and common applications.

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
  - [15. LinkedList (Fast \& Slow Pointers)](#15-linkedlist-fast--slow-pointers)
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

    WHILE left < right:
        IF condition(arr[left], arr[right]):
            # Process result
            result.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif needs_left_increment(arr[left], arr[right]):
            left += 1
        ELSE:
            right -= 1

    RETURN result
```

**Time Complexity**: O(n) FOR most implementations
**Space Complexity**: O(1) excluding output storage

**Example Use Cases**:

- Two Sum problems

  ```python
  ALGORITHM TwoSum(nums, target)
    """
    Given a sorted array `nums` and a target `target`, find two numbers
    such that they add up to `target`. Returns indices (or values).
    """
    Sort array nums
    Set left pointer to beginning of array
    Set right pointer to end of array

    WHILE left < right DO
      Calculate sum = nums[left] + nums[right]

      IF sum equals target THEN
        RETURN pair (left, right)
      ELSE IF sum < target THEN
        Increment left pointer
      ELSE
        Decrement right pointer

    RETURN "No solution found"
  ```

- Container with most water

  ```python
  ALGORITHM MaxArea(heights)
    """
    Given an array `heights` representing vertical lines, find two lines
    that, together with the x-axis, form a container holding the most water.
    """
    Set left to 0
    Set right to length(heights) - 1
    Set maxArea to 0

    WHILE left < right DO
      Calculate height = MIN(heights[left], heights[right])
      Calculate width = right - left
      Calculate area = height × width
      Update maxArea IF area is larger

      IF heights[left] < heights[right] THEN
        Increment left
      ELSE
        Decrement right

    RETURN maxArea
  ```

- Remove duplicates from sorted array

  ```python
  ALGORITHM RemoveDuplicates(nums)
    """
    Given a sorted array `nums`, remove duplicates in-place such that each
    unique element appears only once. Returns the new length.
    """
    IF array is empty THEN
      RETURN 0

    Set writeIndex to 1

    FOR readIndex FROM 1 TO length(nums)-1 DO
      IF current element != previous element THEN
        Set nums[writeIndex] to current element
        Increment writeIndex

    RETURN writeIndex
  ```

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
    """Template: Find the maximum sum/value in a fixed-size sliding window of size k."""
    # Process first window
    window_sum = sum(arr[:k])
    result = window_sum

    # Slide window
    FOR i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]  # Add new, remove old
        result = max(result, window_sum)

    RETURN result
```

### Flexible Size - Find Longest

```python
def longest_window(arr, target):
    """Template: Find the longest flexible-size window satisfying a condition (e.g., sum <= target)."""
    left = 0
    current_sum = 0
    max_length = 0

    FOR right in range(len(arr)):
        # Expand window
        current_sum += arr[right]

        # Shrink window until valid
        WHILE current_sum > target:
            current_sum -= arr[left]
            left += 1

        # Update result IF valid
        max_length = max(max_length, right - left + 1)

    RETURN max_length
```

### Flexible Size - Find Shortest

```python
def shortest_window(arr, target):
    """Template: Find the shortest flexible-size window satisfying a condition (e.g., sum >= target)."""
    left = 0
    current_sum = 0
    min_length = float('inf')

    FOR right in range(len(arr)):
        # Expand window
        current_sum += arr[right]

        # Shrink window WHILE valid
        WHILE current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1

    RETURN min_length IF min_length != float('inf') ELSE 0
```

**Time Complexity**: O(n) FOR most implementations
**Space Complexity**: O(1) FOR numeric windows, O(k) FOR string/object windows

**Example Use Cases**:

- Maximum sum subarray of size k

  ```python
  ALGORITHM MaxSumSubarray(arr, k)
    """Find the maximum sum of a contiguous subarray of size k."""
    IF length(arr) < k THEN
      RETURN error

    Compute sum of first k elements
    Set maxSum to current sum

    FOR i FROM k TO length(arr)-1 DO
      Slide window by adding current element and removing oldest
      Update maxSum IF current sum is larger

    RETURN maxSum
  ```

- Longest substring with k distinct characters

  ```python
  ALGORITHM LongestSubstringKDistinct(s, k)
    """Find the length of the longest substring in s with at most k distinct characters."""
    Set left to 0
    Set maxLength to 0
    Initialize empty character frequency map

    FOR right FROM 0 TO length(s)-1 DO
      Add s[right] to frequency map

      WHILE number of distinct chars in map > k DO
        Decrease frequency of s[left] in map
        Remove s[left] from map IF frequency becomes 0
        Increment left

      Update maxLength IF current window length is larger

    RETURN maxLength
  ```

- Minimum window substring

  ```python
  ALGORITHM MinWindowSubstring(s, t)
    """Find the minimum window substring of s which contains all characters of t."""
    Create frequency map FOR characters in t
    Set left to 0
    Set minLength to infinity
    Track formed and required character counts

    FOR right FROM 0 TO length(s)-1 DO
      Add s[right] to window count
      Update formed count IF character is in t and matches required count

      WHILE all required characters are in current window DO
        Update result IF current window is smaller
        Remove leftmost character from window
        Update formed count IF necessary
        Increment left

    RETURN minimum window substring found
  ```


- Sliding Window Maximum

  ```python
  ALGORITHM SlidingWindowMaximum(nums, w)
    """Find the maximum value in each sliding window of size w in the array nums."""
    IF length(nums) equals 1 THEN
      RETURN nums

    Initialize result array
    Initialize deque to store indices

    // Process first window
    FOR i FROM 0 TO w-1 DO
      // Remove elements smaller than current element from back of deque
      WHILE deque is not empty AND nums[i] >= nums[deque.back()] DO
        Remove last element from deque

      Add i to deque

    // Add maximum of first window to result
    Add nums[deque.front()] to result

    // Process rest of the array
    FOR i FROM w TO length(nums)-1 DO
      // Remove elements smaller than current element from back
      WHILE deque is not empty AND nums[i] >= nums[deque.back()] DO
        Remove last element from deque

      // Remove elements outside current window from front
      WHILE deque is not empty AND deque.front() <= (i - w) DO
        Remove first element from deque

      Add i to deque

      // Front of deque is maximum of current window
      Add nums[deque.front()] to result

    RETURN result
  ```

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
    """Template: Perform a level-order traversal of a tree using BFS."""
    IF not root:
        RETURN

    queue = deque([root])
    WHILE queue:
        node = queue.popleft()
        # Process node
        FOR child in node.children:
            queue.append(child)
```

### Graph BFS

```python
from collections import deque

def bfs(start, graph):
    """Template: Perform a BFS traversal on a graph starting from a given node."""
    queue = deque([start])
    visited = {start}

    WHILE queue:
        node = queue.popleft()
        # Process node
        FOR neighbor in graph[node]:
            IF neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

### BFS with Level Tracking

```python
from collections import deque

def bfs_by_level(start, graph):
    """Template: Perform BFS traversal while tracking the level of each node."""
    queue = deque([start])
    visited = {start}
    level = 0

    WHILE queue:
        # Process entire level
        level_size = len(queue)
        FOR _ in range(level_size):
            node = queue.popleft()
            # Process node at current level
            FOR neighbor in graph[node]:
                IF neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        level += 1
```

**Time Complexity**: O(V + E) where V is vertices and E is edges
**Space Complexity**: O(V)

**Example Use Cases**:

- Shortest path in maze

  ```python
  ALGORITHM ShortestPathInMaze(maze, start, end)
    """Find the shortest path from start to end in an unweighted maze (grid) using BFS."""
    Initialize queue with start position
    Mark start as visited
    Set distance of start to 0

    WHILE queue is not empty DO
      Remove current position from queue

      IF current position is end THEN
        RETURN distance of current position

      FOR each adjacent cell (up, down, left, right) DO
        IF adjacent cell is valid AND not visited THEN
          Mark adjacent cell as visited
          Set distance of adjacent cell to current distance + 1
          Add adjacent cell to queue

    RETURN "No path found"
  ```

- Word ladder

  ```python
  ALGORITHM WordLadder(beginWord, endWord, wordList)
    """Find the shortest transformation sequence from beginWord to endWord using BFS."""
    Create a set from wordList FOR O(1) lookups
    Initialize queue with beginWord and distance 1
    Mark beginWord as visited

    WHILE queue is not empty DO
      Remove current word and its distance from queue

      IF current word equals endWord THEN
        RETURN distance

      FOR each position in current word DO
        FOR each letter in alphabet DO
          Form new word by replacing character at position

          IF new word exists in wordList AND not visited THEN
            Mark new word as visited
            Add new word to queue with distance + 1

    RETURN 0 (no transformation sequence exists)
  ```

- Web crawler

  ```python
  ALGORITHM WebCrawler(startUrl, maxDepth)
    """Crawl web pages starting from startUrl up to maxDepth using BFS."""
    Initialize queue with startUrl and depth 0
    Initialize visited set with startUrl
    Initialize result list with startUrl

    WHILE queue is not empty DO
      Remove current url and its depth from queue

      IF depth >= maxDepth THEN
        CONTINUE to next url

      Download and parse page at current url
      Extract all links from page

      FOR each link DO
        IF link not in visited set THEN
          Add link to visited set
          Add link to result list
          Add link to queue with depth + 1

    RETURN result list
  ```

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
    """Template: Perform a recursive DFS traversal (pre-order shown) on a tree."""
    IF not root:
        RETURN

    # Process root
    dfs(root.left)
    dfs(root.right)
```

### Graph DFS

```python
def dfs(node, graph, visited=None):
    """Template: Perform a recursive DFS traversal on a graph starting from a node."""
    IF visited is None:
        visited = set()

    visited.add(node)
    # Process node

    FOR neighbor in graph[node]:
        IF neighbor not in visited:
            dfs(neighbor, graph, visited)
```

**Time Complexity**: O(V + E) where V is vertices and E is edges
**Space Complexity**: O(V) in worst case

**Example Use Cases**:

- Cycle detection

  ```python
  ALGORITHM DetectCycle(graph)
    """Detect if a cycle exists in a directed graph using DFS."""
    Initialize visited set
    Initialize recursion stack set

    FOR each node in graph DO
      IF node is not visited THEN
        IF HasCycleDFS(node) THEN
          RETURN true

    FUNCTION HasCycleDFS(node)
      Add node to visited set
      Add node to recursion stack

      FOR each neighbor of node DO
        IF neighbor is not visited THEN
          IF HasCycleDFS(neighbor) THEN
            RETURN true
        ELSE IF neighbor is in recursion stack THEN
          RETURN true

      Remove node from recursion stack
      RETURN false

    RETURN false
  ```

- Connected components

  ```python
  ALGORITHM FindConnectedComponents(graph)
    """Find all connected components in an undirected graph using DFS."""
    Initialize visited array FOR all nodes
    Initialize components count to 0
    Initialize component assignment array

    FOR each node in graph DO
      IF node is not visited THEN
        Increment components count
        DFSUtil(node, components count)

    FUNCTION DFSUtil(node, componentId)
      Mark node as visited
      Assign node to current componentId

      FOR each neighbor of node DO
        IF neighbor is not visited THEN
          DFSUtil(neighbor, componentId)

    RETURN component assignment array and count
  ```

- Solving mazes

  ```python
  ALGORITHM SolveMazeWithDFS(maze, start, end)
    """Find a path (not necessarily shortest) from start to end in a maze using DFS."""
    Initialize visited matrix to track visited cells
    Initialize path array to store solution

    FUNCTION DFS(current)
      IF current is out of bounds OR is a wall OR is visited THEN
        RETURN false

      Mark current as visited
      Add current to path

      IF current equals end THEN
        RETURN true

      FOR each direction (up, down, left, right) DO
        IF DFS(neighbor in that direction) THEN
          RETURN true

      Remove current from path (backtrack)
      RETURN false

    RETURN DFS(start)
  ```

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
    """Template: Basic backtracking structure to explore all possibilities."""
    IF is_leaf(start_index):  # Base case
        report(path)
        RETURN

    FOR choice in get_choices(start_index):
        path.append(choice)      # Make choice
        backtrack(start_index + 1, path)  # Explore
        path.pop()               # Undo choice
```

### Aggregation Template

```python
def backtrack(index, state):
    """Template: Backtracking structure for aggregation problems (counting, optimization)."""
    # Base case
    IF is_leaf(index):
        RETURN 1

    result = initial_value

    FOR choice in get_choices(index, state):
        # Make choice and update state
        update_state(state, choice)

        # Explore and aggregate results
        result = aggregate(result, backtrack(index + 1, state))

        # Undo choice
        revert_state(state, choice)

    RETURN result
```

### Common Aggregation Patterns

| Problem Type          | Initial Value | Aggregation FUNCTION |
| --------------------- | ------------- | -------------------- |
| Existence/Possibility | False         | OR (∥)               |
| Count ways            | 0             | Addition (+)         |
| Optimize (max/min)    | 0/-∞/∞        | max()/min()          |

**Time Complexity**: O(k^n) where k is the branching factor and n is the depth
**Space Complexity**: O(n) FOR recursion stack

**Example Use Cases**:

- N-Queens

  ```python
  ALGORITHM SolveNQueens(n)
    """Find all distinct solutions to the N-Queens puzzle using backtracking."""
    Initialize empty board of size n×n
    Initialize solutions array

    FUNCTION Backtrack(row)
      IF row equals n THEN
        Add current board configuration to solutions
        RETURN

      FOR col FROM 0 TO n-1 DO
        IF isValid(row, col) THEN
          Place queen at (row, col)
          Backtrack(row + 1)
          Remove queen from (row, col)

    FUNCTION isValid(row, col)
      FOR prevRow FROM 0 TO row-1 DO
        IF queen in same column OR same diagonal THEN
          RETURN false
      RETURN true

    Backtrack(0)
    RETURN solutions
  ```

- Subset/Combination Sum problems

  ```python
  ALGORITHM CombinationSum(candidates, target)
    """Find all unique combinations in candidates where the numbers sum to target."""
    Sort candidates array
    Initialize results array

    FUNCTION Backtrack(start, current, remaining)
      IF remaining equals 0 THEN
        Add copy of current combination to results
        RETURN

      FOR i FROM start TO length(candidates)-1 DO
        IF candidates[i] > remaining THEN
          BREAK

        Add candidates[i] to current combination
        Backtrack(i, current, remaining - candidates[i])  // Note: i not i+1 to allow reuse
        Remove last element from current combination

    Backtrack(0, [], target)
    RETURN results
  ```

- Permutations

  ```python
  ALGORITHM GeneratePermutations(nums)
    """Generate all possible permutations of the elements in the array nums."""
    Initialize results array
    Initialize used array to track used elements

    FUNCTION Backtrack(current)
      IF length(current) equals length(nums) THEN
        Add copy of current permutation to results
        RETURN

      FOR i FROM 0 TO length(nums)-1 DO
        IF nums[i] is not used THEN
          Mark nums[i] as used
          Add nums[i] to current permutation
          Backtrack(current)
          Remove last element from current permutation
          Mark nums[i] as unused

    Backtrack([])
    RETURN results
  ```

---

## 6. Binary Search

A divide-and-conquer algorithm that finds elements in a sorted array in logarithmic time.

**When to use**:

- Searching in sorted arrays
- Finding the boundary between two distinct regions
- Optimizing minimum/maximum values that satisfy a condition

```python
def binary_search(arr):
    """Template: Binary search to find the first element satisfying a condition."""
    left, right = 0, len(arr) - 1
    result = -1

    WHILE left <= right:
        mid = (left + right) // 2
        IF condition(arr[mid]):
            result = mid       # Potential answer
            right = mid - 1    # Search left FOR better answer
        ELSE:
            left = mid + 1     # Search right

    RETURN result
```

**Time Complexity**: O(log n)
**Space Complexity**: O(1)

**Example Use Cases**:

- Finding element in sorted array

  ```python
  ALGORITHM BinarySearch(arr, target)
    """Find the index of target in a sorted array arr using binary search."""
    Set left to 0
    Set right to length(arr) - 1

    WHILE left <= right DO
      Calculate mid = (left + right) / 2

      IF arr[mid] equals target THEN
        RETURN mid
      ELSE IF arr[mid] < target THEN
        Set left to mid + 1
      ELSE
        Set right to mid - 1

    RETURN -1  // Element not found
  ```

- Finding first/last occurrence

  ```python
  ALGORITHM FindFirstOccurrence(arr, target)
    """Find the index of the first occurrence of target in a sorted array."""
    Set left to 0
    Set right to length(arr) - 1
    Set result to -1

    WHILE left <= right DO
      Calculate mid = (left + right) / 2

      IF arr[mid] equals target THEN
        Set result to mid  // Potential answer
        Set right to mid - 1  // CONTINUE searching left
      ELSE IF arr[mid] < target THEN
        Set left to mid + 1
      ELSE
        Set right to mid - 1

    RETURN result
  ```

- Search in rotated sorted array

  ```python
  ALGORITHM SearchRotatedArray(arr, target)
    """Search for target in a rotated sorted array."""
    Set left to 0
    Set right to length(arr) - 1

    WHILE left <= right DO
      Calculate mid = (left + right) / 2

      IF arr[mid] equals target THEN
        RETURN mid

      // Check which half is sorted
      IF arr[left] <= arr[mid] THEN  // Left half is sorted
        IF target >= arr[left] AND target < arr[mid] THEN
          Set right to mid - 1  // Target in sorted left half
        ELSE
          Set left to mid + 1  // Target in right half
      ELSE  // Right half is sorted
        IF target > arr[mid] AND target <= arr[right] THEN
          Set left to mid + 1  // Target in sorted right half
        ELSE
          Set right to mid - 1  // Target in left half

    RETURN -1  // Element not found
  ```

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
    """Demonstrates common heap operations using Python's heapq module."""
    # Min heap (default in Python)
    min_heap = []
    heapq.heappush(min_heap, 5)
    heapq.heappush(min_heap, 3)
    heapq.heappush(min_heap, 7)

    # Get smallest element without removing
    smallest = min_heap[0]

    # Remove and RETURN smallest element
    smallest = heapq.heappop(min_heap)

    # Max heap (negate values)
    max_heap = []
    heapq.heappush(max_heap, -5)
    heapq.heappush(max_heap, -3)
    heapq.heappush(max_heap, -7)

    # Get largest element without removing
    largest = -max_heap[0]

    # Remove and RETURN largest element
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

  ```python
  ALGORITHM Dijkstra(graph, start)
    """Find the shortest paths from a start node to all other nodes in a weighted graph."""
    Initialize distances array with infinity FOR all nodes except start node
    Initialize priority queue with (start, 0) as (node, distance) pair
    Initialize visited set

    WHILE priority queue is not empty DO
      Extract node with minimum distance from queue

      IF node is already visited THEN
        CONTINUE

      Mark node as visited

      FOR each neighbor of node DO
        Calculate new distance = current distance + edge weight
        IF new distance < stored distance FOR neighbor THEN
          Update distance FOR neighbor
          Add (neighbor, new distance) to priority queue

    RETURN distances array
  ```

- K closest points

  ```python
  ALGORITHM KClosestPoints(points, k, origin)
    """Find the k points closest to the origin using a max heap."""
    Initialize max heap

    FOR each point in points DO
      Calculate distance from point to origin

      IF heap size < k THEN
        Add (distance, point) to heap
      ELSE IF distance < largest distance in heap THEN
        Remove largest element from heap
        Add (distance, point) to heap

    Extract all points from heap into result array
    RETURN result array
  ```

- Merge k sorted lists

  ```python
  ALGORITHM MergeKLists(lists)
    """Merge k sorted linked lists into one sorted list using a min heap."""
    Initialize min heap
    Initialize result list

    // Add the first element from each list to the heap
    FOR each list in lists DO
      IF list is not empty THEN
        Add (list[0], list index) to heap

    WHILE heap is not empty DO
      Extract minimum element (value, list index) from heap
      Add value to result list

      // Advance pointer in the list that provided the min element
      Increment pointer FOR list at list index

      IF list at list index still has elements THEN
        Add (current element, list index) to heap

    RETURN result list
  ```

---

## 8. Matrix as Graph

Treating a 2D grid as a graph with neighboring cells as connected nodes.

**When to use**:

- Pathfinding in grids/mazes
- Island/connected region problems
- Game board traversals

```python
def get_neighbors(row, col, matrix):
    """Helper function to get valid neighbors of a cell in a matrix (grid)."""
    # Four directions: Up, Right, Down, Left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    neighbors = []

    FOR dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        # Check bounds
        IF 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
            neighbors.append((new_row, new_col))

    RETURN neighbors
```

**Example Use Cases**:

- Number of islands

  ```python
  ALGORITHM CountIslands(grid)
    """Count the number of islands (connected groups of 1s) in a binary grid."""
    Initialize count to 0

    FOR each cell in grid DO
      IF cell is land (1) THEN
        Increment count
        Sink connected island using DFS

    FUNCTION SinkIsland(row, col)
      IF row or col out of bounds OR cell is water (0) THEN
        RETURN

      Mark current cell as water (0)

      SinkIsland(row+1, col)  // Down
      SinkIsland(row-1, col)  // Up
      SinkIsland(row, col+1)  // Right
      SinkIsland(row, col-1)  // Left

    RETURN count
  ```

- Flood fill

  ```python
  ALGORITHM FloodFill(image, sr, sc, newColor)
    """Fill a connected region in an image with a new color starting from (sr, sc)."""
    Get starting color = image[sr][sc]

    IF starting color equals newColor THEN
      RETURN image  // No changes needed

    FUNCTION Fill(row, col)
      IF row or col out of bounds OR image[row][col] != starting color THEN
        RETURN

      Set image[row][col] to newColor

      Fill(row+1, col)  // Down
      Fill(row-1, col)  // Up
      Fill(row, col+1)  // Right
      Fill(row, col-1)  // Left

    Fill(sr, sc)
    RETURN image
  ```

- Shortest path in maze

  ```python
  ALGORITHM ShortestPathInMaze(maze, start, destination)
    """Find the shortest path from start to destination in a maze (grid) using BFS."""
    Initialize queue with (start.row, start.col, 0)
    Initialize visited matrix
    Mark start as visited
    Set directions as [(0,1), (1,0), (0,-1), (-1,0)]  // Right, Down, Left, Up

    WHILE queue is not empty DO
      Extract current position (row, col, distance)

      IF current position is destination THEN
        RETURN distance

      FOR each direction (dr, dc) in directions DO
        Calculate new position (newRow, newCol)

        WHILE newRow and newCol are valid AND maze[newRow][newCol] is not wall DO
          Move further in the same direction

        // Move back one step to get valid position
        Adjust newRow, newCol back to last valid position

        IF new position is not visited THEN
          Mark new position as visited
          Add (newRow, newCol, distance+1) to queue

    RETURN -1  // No path found
  ```

---

## 9. Monotonic Stack

A stack that maintains elements in either increasing or decreasing order.

**When to use**:

- Finding the next greater/smaller element
- Problems involving histograms
- Trapping rain water

```python
def monotonic_increasing_stack(arr):
    """Template: Process an array using a monotonic stack (decreasing order shown)."""
    stack = []  # Will maintain decreasing order

    FOR i, val in enumerate(arr):
        # Pop elements greater than current
        WHILE stack and stack[-1] > val:
            popped = stack.pop()
            # Process popped element

        stack.append(val)

    # Process remaining elements in stack IF needed
```

**Time Complexity**: O(n) as each element is pushed and popped at most once
**Space Complexity**: O(n)

**Example Use Cases**:

- Next greater element

  ```python
  ALGORITHM NextGreaterElement(nums)
    """Find the next greater element for each element in an array using a monotonic stack."""
    Initialize result array filled with -1
    Initialize empty stack

    FOR i FROM 0 TO length(nums)-1 DO
      WHILE stack is not empty AND nums[stack.top] < nums[i] DO
        Set result[stack.top] to nums[i]
        Pop from stack

      Push i onto stack

    RETURN result
  ```

- Largest rectangle in histogram

  ```python
  ALGORITHM LargestRectangleArea(heights)
    """Find the largest rectangle area in a histogram using a monotonic stack."""
    Initialize stack
    Initialize maxArea to 0
    Append 0 to heights array  // Sentinel value at end

    FOR i FROM 0 TO length(heights)-1 DO
      WHILE stack is not empty AND heights[stack.top] > heights[i] DO
        Pop height from stack
        Calculate width = i - stack.top - 1 IF stack not empty, ELSE i
        Calculate area = height × width
        Update maxArea IF area is larger

      Push i onto stack

    RETURN maxArea
  ```

- Daily temperatures

  ```python
  ALGORITHM DailyTemperatures(temperatures)
    """Find the number of days until a warmer temperature for each day."""
    Initialize result array with zeros
    Initialize empty stack

    FOR i FROM 0 TO length(temperatures)-1 DO
      WHILE stack is not empty AND temperatures[stack.top] < temperatures[i] DO
        Pop index from stack
        Set result[index] to i - index

      Push i onto stack

    RETURN result
  ```

---

## 10. Topological Sort

Ordering of vertices in a directed acyclic graph where FOR each edge (u,v), u comes before v.

**When to use**:

- Task scheduling with prerequisites
- Course scheduling
- Dependency resolution

```python
from collections import deque

def topological_sort(graph):
    """Perform a topological sort on a directed acyclic graph (DAG)."""
    # Calculate in-degrees
    indegree = {node: 0 FOR node in graph}
    FOR node in graph:
        FOR neighbor in graph[node]:
            indegree[neighbor] += 1

    # Start with nodes that have no dependencies
    queue = deque([node FOR node, count in indegree.items() IF count == 0])
    result = []

    WHILE queue:
        node = queue.popleft()
        result.append(node)

        FOR neighbor in graph[node]:
            indegree[neighbor] -= 1
            IF indegree[neighbor] == 0:
                queue.append(neighbor)

    # Check IF cycle exists
    RETURN result IF len(result) == len(graph) ELSE None
```

**Time Complexity**: O(V + E)
**Space Complexity**: O(V)

**Example Use Cases**:

- Course prerequisites

  ```python
  ALGORITHM CourseScheduling(numCourses, prerequisites)
    """Find a valid order to take courses given prerequisites, or detect a cycle."""
    Create adjacency list representation of graph
    Initialize indegree array of size numCourses

    FOR each prerequisite (course, prereq) DO
      Add course to adjacency list of prereq
      Increment indegree of course

    Initialize queue with all courses having indegree 0
    Initialize courseOrder array

    WHILE queue is not empty DO
      Remove course from queue
      Add course to courseOrder

      FOR each adjacent course of current course DO
        Decrement indegree of adjacent course
        IF indegree becomes 0 THEN
          Add adjacent course to queue

    IF length of courseOrder equals numCourses THEN
      RETURN courseOrder  // Valid schedule
    ELSE
      RETURN empty array  // Cycle detected, impossible to complete
  ```

- Build systems

  ```python
  ALGORITHM BuildDependencyOrder(targets, dependencies)
    """Determine a valid build order for targets with dependencies."""
    Create adjacency list from dependencies
    Initialize indegree map FOR each target

    FOR each dependency (target, dependent) DO
      Add dependent to adjacency list of target
      Increment indegree of dependent

    Initialize queue with all targets having indegree 0
    Initialize buildOrder array

    WHILE queue is not empty DO
      Remove target from queue
      Add target to buildOrder

      FOR each dependent of current target DO
        Decrement indegree of dependent
        IF indegree becomes 0 THEN
          Add dependent to queue

    IF length of buildOrder equals number of targets THEN
      RETURN buildOrder  // Valid build order
    ELSE
      RETURN failure  // Circular dependency detected
  ```

- Parallel job scheduling

  ```python
  ALGORITHM ParallelJobScheduling(jobs, dependencies, numProcessors)
    """Schedule jobs with dependencies on multiple processors to minimize completion time."""
    Create adjacency list from dependencies
    Initialize indegree map FOR each job

    FOR each dependency (job, dependent) DO
      Add dependent to adjacency list of job
      Increment indegree of dependent

    Initialize ready queue with all jobs having indegree 0
    Initialize completion time map FOR each job
    Initialize current time to 0
    Initialize running jobs set

    WHILE ready queue is not empty OR running jobs not empty DO
      // Assign available jobs to processors
      WHILE ready queue not empty AND size of running jobs < numProcessors DO
        Remove job from ready queue
        Add job to running jobs with end time = current time + job duration

      // Fast forward to next job completion
      Set nextCompletionTime to minimum end time in running jobs
      Set current time to nextCompletionTime

      // Process completed jobs
      FOR each job that completes at current time DO
        Remove job from running jobs

        FOR each dependent of job DO
          Decrement indegree of dependent
          Update earliest start time of dependent
          IF indegree becomes 0 THEN
            Add dependent to ready queue

    RETURN maximum completion time across all jobs
  ```

---

## 11. Trie

A tree-like data structure FOR efficient string search operations.

**When to use**:

- Prefix matching
- Autocomplete functionality
- Spell checkers

```python
CLASS TrieNode:
    """Represents a node in a Trie."""
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.count = 0

CLASS Trie:
    """Implements a Trie data structure for efficient string prefix operations."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Inserts a word into the Trie."""
        node = self.root
        FOR char in word:
            IF char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.count += 1
        node.is_end = True

    def search(self, word):
        """Searches for a complete word in the Trie."""
        node = self.root
        FOR char in word:
            IF char not in node.children:
                RETURN False
            node = node.children[char]
        RETURN node.is_end

    def starts_with(self, prefix):
        """Checks if there is any word in the Trie that starts with the given prefix."""
        node = self.root
        FOR char in prefix:
            IF char not in node.children:
                RETURN 0
            node = node.children[char]
        RETURN node.count
```

**Time Complexity**:

- Insert: O(m) where m is word length
- Search: O(m) where m is word length
- Space Complexity: O(n*m) where n is number of words and m is average length

**Example Use Cases**:

- Word dictionary

  ```python
  ALGORITHM ImplementDictionary()
    """Implement a dictionary using a Trie for add, search, and delete operations."""
    Initialize Trie with root node

    FUNCTION AddWord(word)
      Set current to root node

      FOR each character c in word DO
        IF c is not in current.children THEN
          Create new TrieNode FOR c
        Set current to child node FOR c

      Mark current node as end of word

    FUNCTION SearchWord(word)
      Set current to root node

      FOR each character c in word DO
        IF c is not in current.children THEN
          RETURN false
        Set current to child node FOR c

      RETURN true IF current node is marked as end of word, false otherwise

    FUNCTION DeleteWord(word)
      FUNCTION _Delete(node, word, depth)
        IF depth equals length of word THEN
          IF node is not marked as end of word THEN
            RETURN false
          Unmark node as end of word
          RETURN node has no children

        character = word[depth]
        IF character not in node.children THEN
          RETURN false

        shouldDeleteChild = _Delete(node.children[character], word, depth+1)

        IF shouldDeleteChild THEN
          Remove character from node's children
          RETURN node has no children AND is not end of word

        RETURN false

      _Delete(root, word, 0)
  ```

- Autocomplete

  ```python
  ALGORITHM Autocomplete(prefix)
    """Provide autocomplete suggestions based on a given prefix using a Trie."""
    Initialize Trie with preloaded dictionary
    Initialize result list

    FUNCTION FindSuggestions(prefix)
      Set current to root node

      // Navigate to prefix endpoint
      FOR each character c in prefix DO
        IF c is not in current.children THEN
          RETURN empty list  // No words with this prefix
        Set current to child node FOR c

      // Collect all words with this prefix
      CollectWords(current, prefix, result)

      RETURN result

    FUNCTION CollectWords(node, currentPrefix, result)
      IF node is marked as end of word THEN
        Add currentPrefix to result

      FOR each character c in node.children DO
        CollectWords(node.children[c], currentPrefix + c, result)
        IF result size reaches limit THEN
          RETURN

    RETURN FindSuggestions(prefix)
  ```

- IP routing tables

  ```python
  ALGORITHM IPRoutingTable()
    """Implement an IP routing table using a Trie for longest prefix matching."""
    Initialize Trie with root node

    FUNCTION InsertRoute(ipAddress, nextHop)
      Set current to root node
      Convert ipAddress to binary string

      FOR each bit b in binary string DO
        IF b is not in current.children THEN
          Create new TrieNode FOR b
        Set current to child node FOR b

      Store nextHop information in current node

    FUNCTION LongestPrefixMatch(ipAddress)
      Set current to root node
      Convert ipAddress to binary string
      Initialize bestMatch to null

      FOR each bit b in binary string DO
        IF current has nextHop information THEN
          Update bestMatch to current's nextHop

        IF b is not in current.children THEN
          BREAK

        Set current to child node FOR b

      // Check final node
      IF current has nextHop information THEN
        Update bestMatch to current's nextHop

      RETURN bestMatch
  ```

---

## 12. Union Find (Disjoint Set)

Data structure FOR tracking elements partitioned into disjoint sets.

**When to use**:

- Finding connected components
- Cycle detection in undirected graphs
- Kruskal's algorithm FOR minimum spanning trees

### Basic Implementation

```python
CLASS UnionFind:
    """Basic implementation of the Union-Find (Disjoint Set Union) data structure."""
    def __init__(self, n=0):
        self.parent = {}  # Maps element to its parent

    def find(self, x):
        """Finds the representative (root) of the set containing x, with path compression."""
        # IF x not in set yet, add it as its own parent
        IF x not in self.parent:
            self.parent[x] = x

        # Find root of the set containing x
        IF self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        RETURN self.parent[x]

    def union(self, x, y):
        """Merges the sets containing x and y."""
        # Connect x's set to y's set
        self.parent[self.find(x)] = self.find(y)

    def connected(self, x, y):
        """Checks if x and y belong to the same set."""
        RETURN self.find(x) == self.find(y)
```

### Optimized with Rank

```python
CLASS UnionFind:
    """Optimized Union-Find with path compression and union by rank."""
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        """Finds the representative (root) of the set containing x, with path compression."""
        IF x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

        # Path compression
        IF self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        RETURN self.parent[x]

    def union(self, x, y):
        """Merges the sets containing x and y using union by rank."""
        root_x = self.find(x)
        root_y = self.find(y)

        IF root_x == root_y:
            RETURN

        # Union by rank
        IF self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        ELSE:
            self.parent[root_y] = root_x
            IF self.rank[root_x] == self.rank[root_y]:
                self.rank[root_x] += 1
```

**Time Complexity**:

- With path compression and union by rank:
  - Amortized O(α(n)) per operation, where α is the inverse Ackermann FUNCTION (nearly constant)
- Without optimizations:
  - O(n) worst case per operation

**Example Use Cases**:

- Network connectivity

  ```python
  ALGORITHM NetworkConnectivity(nodes, connections)
    """Determine connected components in a network using Union-Find."""
    Initialize UnionFind with all nodes

    FOR each connection (node1, node2) in connections DO
      Union(node1, node2)

    Initialize component count map

    FOR each node in nodes DO
      root = Find(node)
      Increment count FOR this root in component map

    RETURN number of distinct roots and size of each component
  ```

- Image segmentation

  ```python
  ALGORITHM ImageSegmentation(image, similarityThreshold)
    Initialize UnionFind with all pixels

    FOR each pixel p in image DO
      FOR each adjacent pixel q DO
        IF similarity(p, q) > similarityThreshold THEN
          Union(p, q)

    Initialize segment map

    FOR each pixel p in image DO
      root = Find(p)
      Assign p to segment identified by root

    RETURN segmented image
  ```

- Friends circles

  ```python
  ALGORITHM FriendCircles(friendshipMatrix)
    Initialize UnionFind with all people
    n = number of people

    FOR i FROM 0 TO n-1 DO
      FOR j FROM 0 TO n-1 DO
        IF friendshipMatrix[i][j] == 1 THEN
          Union(i, j)

    Initialize circles set

    FOR each person i DO
      Add Find(i) to circles set

    RETURN size of circles set
  ```

---

## 13. Kadane's Algorithm

A dynamic programming approach to find the maximum subarray sum.

**When to use**:

- Finding maximum/minimum sum subarray
- Requiring contiguous elements with optimal value
- When greedy approach with local/global optimal values works

```python
# Kadane's Algorithm (handles all negative arrays)
def kadanes_general(arr):
    """Finds the maximum sum of a contiguous subarray (handles all negative arrays)."""
    IF not arr:
        RETURN 0

    max_so_far = arr[0]
    max_ending_here = arr[0]

    FOR num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    RETURN max_so_far
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

**Example Use Cases**:

- Maximum sum subarray

  ```python
  ALGORITHM MaximumSubarraySum(nums)
    """Find the maximum sum of a contiguous subarray using Kadane's algorithm."""
    IF array is empty THEN
      RETURN 0

    Set maxEndingHere = nums[0]
    Set maxSoFar = nums[0]

    FOR i FROM 1 TO length(nums)-1 DO
      // Either extend previous subarray or start new one
      Set maxEndingHere = MAX(nums[i], maxEndingHere + nums[i])

      // Update global maximum
      Set maxSoFar = MAX(maxSoFar, maxEndingHere)

    RETURN maxSoFar
  ```

- Maximum product subarray

  ```python
  ALGORITHM MaximumProductSubarray(nums)
    """Find the maximum product of a contiguous subarray."""
    IF array is empty THEN
      RETURN 0

    // Track both max and min products (FOR handling negative numbers)
    Set maxProduct = nums[0]
    Set minProduct = nums[0]
    Set result = nums[0]

    FOR i FROM 1 TO length(nums)-1 DO
      // IF current number is negative, SWAP max and min
      IF nums[i] < 0 THEN
        SWAP maxProduct and minProduct

      // Either extend previous subarray or start new one
      Set maxProduct = MAX(nums[i], maxProduct * nums[i])
      Set minProduct = MIN(nums[i], minProduct * nums[i])

      // Update global maximum
      Set result = MAX(result, maxProduct)

    RETURN result
  ```

- Circular array maximum sum

  ```python
  ALGORITHM CircularMaximumSum(nums)
    """Find the maximum subarray sum in a circular array."""
    // Case 1: Maximum subarray is not circular
    Set maxStraightSum = KadaneMaxSum(nums)

    // Case 2: Maximum subarray is circular
    Set totalSum = SUM of all elements in nums
    // Invert signs of all elements
    FOR i FROM 0 TO length(nums)-1 DO
      nums[i] = -nums[i]

    // Find minimum subarray sum (using Kadane on inverted array)
    Set minSubarraySum = KadaneMaxSum(nums)
    // Max circular sum is total sum minus the minimum subarray sum
    Set maxCircularSum = totalSum + minSubarraySum  // Adding because elements are now negative

    // Handle all negative case
    IF totalSum + minSubarraySum equals 0 THEN
      RETURN maxStraightSum

    RETURN MAX(maxStraightSum, maxCircularSum)

    FUNCTION KadaneMaxSum(arr)
      Set maxEndingHere = arr[0]
      Set maxSoFar = arr[0]

      FOR i FROM 1 TO length(arr)-1 DO
        Set maxEndingHere = MAX(arr[i], maxEndingHere + arr[i])
        Set maxSoFar = MAX(maxSoFar, maxEndingHere)

      RETURN maxSoFar
  ```

---

## 14. Prefix Sums

A preprocessing technique FOR efficient range sum queries.

**When to use**:

- Range sum queries
- Cumulative operations on arrays
- Checking FOR specific sum conditions over subarrays

```python
def prefix_sums(arr):
    """Calculates the prefix sum array for a given array."""
    prefix = [0] * (len(arr) + 1)

    FOR i in range(len(arr)):
        prefix[i + 1] = prefix[i] + arr[i]

    RETURN prefix

def range_sum(prefix, left, right):
    """Calculates the sum of elements in a range using the prefix sum array."""
    # Sum of elements from index left to right (inclusive)
    RETURN prefix[right + 1] - prefix[left]

# Example using prefix sums to find subarrays with sum equal to k
def count_subarrays_with_sum(arr, k):
    """Counts the number of subarrays whose sum equals k using prefix sums and a hash map."""
    prefix_sum = 0
    count = 0
    sum_counts = {0: 1}  # Empty subarray has sum 0

    FOR num in arr:
        prefix_sum += num
        # IF (prefix_sum - k) exists, there is a subarray with sum k
        IF prefix_sum - k in sum_counts:
            count += sum_counts[prefix_sum - k]

        # Increment count of current prefix sum
        sum_counts[prefix_sum] = sum_counts.get(prefix_sum, 0) + 1

    RETURN count
```

**Time Complexity**:

- Preprocessing: O(n)
- Range queries: O(1)

**Space Complexity**: O(n) FOR storing prefix sums

**Example Use Cases**:

- Range sum queries

  ```python
  ALGORITHM RangeSum(nums, queries)
    """Efficiently answer multiple range sum queries using prefix sums."""
    // Precompute prefix sums
    Initialize prefixSum array of length len(nums)+1 with prefixSum[0] = 0

    FOR i FROM 0 TO length(nums)-1 DO
      prefixSum[i+1] = prefixSum[i] + nums[i]

    // Process queries
    Initialize results array

    FOR each query (left, right) in queries DO
      // Calculate sum from index left to right (inclusive)
      sum = prefixSum[right+1] - prefixSum[left]
      Add sum to results

    RETURN results
  ```

- Subarray sum equals K

  ```python
  ALGORITHM SubarraySumEqualsK(nums, k)
    """Count the number of contiguous subarrays whose sum equals k."""
    Initialize count = 0
    Initialize prefixSum = 0
    Initialize hashMap with {0: 1}  // Empty subarray has sum 0

    FOR i FROM 0 TO length(nums)-1 DO
      // Update current prefix sum
      prefixSum += nums[i]

      // IF (prefixSum - k) exists in map, we've found subarray(s) with sum k
      IF prefixSum - k exists in hashMap THEN
        count += hashMap[prefixSum - k]

      // Add current prefix sum to hashMap
      IF prefixSum exists in hashMap THEN
        hashMap[prefixSum] += 1
      ELSE
        hashMap[prefixSum] = 1

    RETURN count
  ```

- Count number of subarrays with specific properties

  ```python
  ALGORITHM CountSubarraysWithConstraint(nums, constraint)
    """General template to count subarrays satisfying a constraint using prefix properties."""
    Initialize count = 0
    Initialize prefixProperty = 0
    Initialize hashMap with {0: 1}  // Empty subarray base case

    FOR i FROM 0 TO length(nums)-1 DO
      // Update prefix property (e.g., sum, product, XOR, etc.)
      Update prefixProperty based on nums[i]

      // Calculate the complementary value we need to find
      complementValue = CalculateComplementValue(prefixProperty, constraint)

      // IF complementValue exists, add its count to our result
      IF complementValue exists in hashMap THEN
        count += hashMap[complementValue]

      // Add current prefix property to hashMap
      IF prefixProperty exists in hashMap THEN
        hashMap[prefixProperty] += 1
      ELSE
        hashMap[prefixProperty] = 1

    RETURN count

    // Helper FUNCTION depends on specific property and constraint
    FUNCTION CalculateComplementValue(prefixProp, constraint)
      // Example FOR sum equals K: RETURN prefixProp - K
      // Example FOR sum divisible by K: RETURN prefixProp % K
      // Example FOR XOR equals K: RETURN prefixProp ^ K
      RETURN appropriate value based on constraint
  ```

---

## 15. LinkedList (Fast & Slow Pointers)

A two-pointer technique where one pointer moves faster than the other.

**When to use**:

- Cycle detection problems
- Finding middle element in a linked list
- Finding nth element from the end
- Detecting palindrome linked lists

```python
CLASS ListNode:
    """Represents a node in a singly linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detect_cycle(head):
    """Detects if a cycle exists in a linked list using fast and slow pointers."""
    IF not head or not head.next:
        RETURN False

    slow = head
    fast = head

    # IF there is a cycle, fast will eventually catch up to slow
    WHILE fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        IF slow == fast:  # Cycle detected
            RETURN True

    RETURN False

def find_cycle_start(head):
    """Finds the starting node of a cycle in a linked list."""
    IF not head or not head.next:
        RETURN None

    # Phase 1: Detect cycle
    slow = head
    fast = head

    WHILE fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        IF slow == fast:  # Cycle detected
            BREAK

    # No cycle found
    IF not fast or not fast.next:
        RETURN None

    # Phase 2: Find entrance to cycle
    slow = head
    WHILE slow != fast:
        slow = slow.next
        fast = fast.next

    RETURN slow  # Cycle start node

def find_middle(head):
    """Finds the middle node of a linked list using fast and slow pointers."""
    IF not head:
        RETURN None
    slow = head
    fast = head

    # When fast reaches the end, slow is at the middle
    WHILE fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    RETURN slow  # Middle node
```

**Time Complexity**: O(n)
**Space Complexity**: O(1)

**Example Use Cases**:

- Detect cycle in linked list

  ```python
  ALGORITHM DetectCycle(head)
    """Detects if a cycle exists in a linked list using Floyd's Tortoise and Hare."""
    IF head is null OR head.next is null THEN
      RETURN false

    Set slow = head
    Set fast = head

    WHILE fast is not null AND fast.next is not null DO
      Set slow = slow.next           // Move slow by 1
      Set fast = fast.next.next      // Move fast by 2

      IF slow equals fast THEN
        RETURN true                  // Cycle detected

    RETURN false                     // No cycle
  ```

- Find cycle start point

  ```python
  ALGORITHM FindCycleStart(head)
    """Finds the starting node of a cycle in a linked list (if one exists)."""
    IF head is null OR head.next is null THEN
      RETURN null

    // Phase 1: Detect cycle
    Set slow = head
    Set fast = head
    Set hasCycle = false

    WHILE fast is not null AND fast.next is not null DO
      Set slow = slow.next
      Set fast = fast.next.next

      IF slow equals fast THEN
        Set hasCycle = true
        BREAK

    IF hasCycle is false THEN
      RETURN null                    // No cycle

    // Phase 2: Find entrance to cycle
    Set slow = head

    WHILE slow does not equal fast DO
      Set slow = slow.next
      Set fast = fast.next

    RETURN slow                      // Cycle start node
  ```

- Find middle of linked list

  ```python
  ALGORITHM FindMiddle(head)
    """Finds the middle node of a linked list."""
    IF head is null THEN
      RETURN null

    Set slow = head
    Set fast = head

    WHILE fast is not null AND fast.next is not null DO
      Set slow = slow.next           // Move slow by 1
      Set fast = fast.next.next      // Move fast by 2

    RETURN slow                      // Middle node
  ```

- Palindrome linked list

  ```python
  ALGORITHM IsPalindrome(head)
    """Checks if a linked list is a palindrome."""
    IF head is null OR head.next is null THEN
      RETURN true                    // Empty list or single node is palindrome

    // Find middle of the linked list
    Set slow = head
    Set fast = head

    WHILE fast is not null AND fast.next is not null DO
      Set slow = slow.next
      Set fast = fast.next.next

    // Reverse second half of the list
    Set secondHalf = slow.next
    Set prev = null

    WHILE secondHalf is not null DO
      Set next = secondHalf.next
      Set secondHalf.next = prev
      Set prev = secondHalf
      Set secondHalf = next

    // Compare first half with reversed second half
    Set firstHalf = head
    Set secondHalf = prev

    WHILE secondHalf is not null DO
      IF firstHalf.value does not equal secondHalf.value THEN
        RETURN false

      Set firstHalf = firstHalf.next
      Set secondHalf = secondHalf.next

    RETURN true
  ```

---

## 16. Linked List Reversal

A common pattern FOR manipulating linked list orders.

**When to use**:

- Problems requiring reversal of all or part of a linked list
- Problems involving K-groups or alternative reverse operations

```python
def reverse_linked_list(head):
    """Reverses a singly linked list iteratively."""
    prev = None
    current = head

    WHILE current:
        next_temp = current.next  # Store next node
        current.next = prev       # Reverse pointer
        prev = current            # Move prev forward
        current = next_temp       # Move current forward

    RETURN prev  # New head

def reverse_sublist(head, start, end):
    """Reverses a sublist of a linked list from position start to end."""
    # Create a dummy node FOR easier handling of edge cases
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy

    # Move prev to the node just before the start position
    FOR _ in range(1, start):
        prev = prev.next

    current = prev.next  # Node at start position

    # Reverse nodes from start to end
    FOR _ in range(end - start):
        next_node = current.next
        current.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node

    RETURN dummy.next  # New head

def reverse_k_group(head, k):
    """Reverses nodes of a linked list k at a time."""
    count = 0
    curr = head

    # Count k nodes
    WHILE curr and count < k:
        curr = curr.next
        count += 1

    # IF we have k nodes, reverse them
    IF count == k:
        # Reverse k nodes
        prev = reverse_k_group(curr, k)  # Reverse next k-group and get its head

        # Connect current k-group to the reversed next k-group
        WHILE count > 0:
            next_temp = head.next
            head.next = prev
            prev = head
            head = next_temp
            count -= 1

        RETURN prev  # New head of reversed k-group

    RETURN head  # Less than k nodes left, RETURN as is
```

**Time Complexity**: O(n)
**Space Complexity**: O(1) FOR iterative solutions, O(n) FOR recursive solutions

**Example Use Cases**:

- Reverse linked list

  ```python
  ALGORITHM ReverseLinkedList(head)
    """Reverses a singly linked list iteratively."""
    Set prev = null
    Set current = head

    WHILE current is not null DO
      Set nextTemp = current.next    // Store next node
      Set current.next = prev        // Reverse pointer
      Set prev = current             // Move prev forward
      Set current = nextTemp         // Move current forward

    RETURN prev                      // New head
  ```

- Reverse nodes in K-group

  ```python
  ALGORITHM ReverseKGroup(head, k)
    """Reverses nodes of a linked list k at a time recursively."""
    Set count = 0
    Set current = head

    // Count k nodes
    WHILE current is not null AND count < k DO
      Set current = current.next
      Increment count

    // IF we have k nodes, reverse them
    IF count equals k THEN
      // Recursively reverse next k-group
      Set reversedNext = ReverseKGroup(current, k)

      // Reverse current k-group
      Set prev = reversedNext
      Set current = head

      WHILE count > 0 DO
        Set nextTemp = current.next
        Set current.next = prev
        Set prev = current
        Set current = nextTemp
        Decrement count

      RETURN prev                    // New head of reversed k-group
    ELSE
      RETURN head                    // Less than k nodes, RETURN as is
  ```

- Reverse alternating K elements

  ```python
  ALGORITHM ReverseAlternatingKElements(head, k)
    Set current = head
    Set prev = null
    Set prevTail = null    // Tail of previous group
    Set firstPass = true

    WHILE current is not null DO
      // Count k nodes
      Set groupHead = current
      Set count = 0

      WHILE current is not null AND count < k DO
        Set current = current.next
        Increment count

      IF count equals k AND firstPass OR NOT firstPass THEN
        // Save next group's head
        Set nextGroupHead = current

        // Reverse the current group
        Set subHead = groupHead
        Set subPrev = current    // Points to next group
        Set subCurrent = groupHead
        Set subCount = count

        WHILE subCount > 0 DO
          Set nextTemp = subCurrent.next
          Set subCurrent.next = subPrev
          Set subPrev = subCurrent
          Set subCurrent = nextTemp
          Decrement subCount

        // Connect with previous group
        IF prevTail is not null THEN
          Set prevTail.next = subPrev  // Connect previous tail to new head
        ELSE
          Set head = subPrev           // Update head IF this is first group

        Set prevTail = subHead         // New tail is the original head
        Set current = nextGroupHead    // Move to next group
      ELSE
        // Skip this group (no reversal)
        Set prevTail = groupHead
        WHILE prevTail.next is not null AND prevTail.next does not equal current DO
          Set prevTail = prevTail.next

      // Toggle the flag
      Set firstPass = NOT firstPass

    RETURN head
  ```

---

## 17. Dijkstra's Algorithm

A greedy algorithm FOR finding the shortest path in a weighted graph.

**When to use**:

- Finding shortest path in weighted graph with non-negative weights
- Optimizing distance between nodes
- Pathfinding with cost considerations
- Network routing problems with weights

```python
import heapq

def dijkstra(graph, start):
    """Finds the shortest paths from a start node to all other nodes in a weighted graph."""
    # Initialize distances with infinity FOR all nodes except start
    distances = {node: float('infinity') FOR node in graph}
    distances[start] = 0

    # Priority queue to process nodes by current distance
    priority_queue = [(0, start)]

    # Track visited nodes
    visited = set()

    WHILE priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip IF we've already processed this node
        IF current_node in visited:
            CONTINUE

        # Mark as visited
        visited.add(current_node)

        # Process all neighbors
        FOR neighbor, weight in graph[current_node].items():
            # Skip visited neighbors
            IF neighbor in visited:
                CONTINUE

            # Calculate distance to neighbor through current node
            distance = current_distance + weight

            # IF we found a shorter path, update distance
            IF distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    RETURN distances

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

  ```python
  ALGORITHM NetworkRouting(network, source, destination)
    """Find the shortest path between source and destination in a network using Dijkstra's."""
    // network is a graph of nodes and weighted edges

    Initialize distances map with infinity FOR all nodes
    Set distances[source] = 0
    Initialize priorityQueue with (0, source)
    Initialize previous map to track path

    WHILE priorityQueue is not empty DO
      currentDistance, currentNode = Remove minimum from priorityQueue

      // Skip IF we've processed this node already
      IF currentNode has been visited THEN
        CONTINUE

      // Mark as visited
      Mark currentNode as visited

      // IF we reached destination, we can reconstruct path and RETURN
      IF currentNode equals destination THEN
        RETURN ReconstructPath(previous, source, destination)

      // Check all adjacent nodes
      FOR each neighbor, weight in adjacency list of currentNode DO
        // Skip visited neighbors
        IF neighbor has been visited THEN
          CONTINUE

        // Calculate new distance
        newDistance = currentDistance + weight

        // IF we found a better path, update
        IF newDistance < distances[neighbor] THEN
          distances[neighbor] = newDistance
          previous[neighbor] = currentNode
          Add (newDistance, neighbor) to priorityQueue

    // No path found
    RETURN empty path

    FUNCTION ReconstructPath(previous, source, destination)
      Initialize path as empty list
      Set current = destination

      WHILE current is not null AND current does not equal source DO
        Add current to beginning of path
        Set current = previous[current]

      IF current equals source THEN
        Add source to beginning of path
        RETURN path
      ELSE
        RETURN empty list  // No path exists
  ```

- GPS navigation

  ```python
  ALGORITHM GPSNavigation(map, start, end, trafficData)
    """Find the fastest route in a GPS map considering traffic, using Dijkstra's."""
    // map is a graph of locations and roads with distances
    // trafficData provides current traffic conditions FOR each road segment

    Initialize distances map with infinity FOR all locations
    Set distances[start] = 0
    Initialize priorityQueue with (0, start)
    Initialize previous map to track path

    WHILE priorityQueue is not empty DO
      currentDistance, currentLocation = Remove minimum from priorityQueue

      // Skip IF we've processed this location already
      IF currentLocation has been visited THEN
        CONTINUE

      // Mark as visited
      Mark currentLocation as visited

      // IF we reached destination, we can RETURN
      IF currentLocation equals end THEN
        BREAK

      // Check all adjacent locations
      FOR each neighbor, baseDistance in adjacency list of currentLocation DO
        // Skip visited locations
        IF neighbor has been visited THEN
          CONTINUE

        // Calculate actual distance considering traffic
        actualDistance = baseDistance * trafficData[currentLocation][neighbor]
        newDistance = currentDistance + actualDistance

        // IF we found a better path, update
        IF newDistance < distances[neighbor] THEN
          distances[neighbor] = newDistance
          previous[neighbor] = currentLocation
          Add (newDistance, neighbor) to priorityQueue

    // Reconstruct the best route
    RETURN ReconstructRoute(previous, start, end)
  ```

- Flight scheduling

  ```python
  ALGORITHM FlightScheduling(flights, startAirport, endAirport, startTime)
    """Find the cheapest flight itinerary between two airports using Dijkstra's."""
    // flights is a list of available flights with departure time, arrival time, and cost

    Initialize bestCost map with infinity FOR all airports
    Set bestCost[startAirport] = 0
    Initialize priorityQueue with (0, startAirport, startTime)
    Initialize bestRoute map to track flights taken

    WHILE priorityQueue is not empty DO
      currentCost, currentAirport, currentTime = Remove minimum from priorityQueue

      // IF we reached destination, we can RETURN
      IF currentAirport equals endAirport THEN
        RETURN ReconstructFlightItinerary(bestRoute, startAirport, endAirport)

      // Check all possible flights from current airport
      FOR each flight from currentAirport DO
        // Skip flights that depart before we arrive
        IF flight.departureTime < currentTime + MINIMUM_CONNECTION_TIME THEN
          CONTINUE

        nextAirport = flight.destination
        nextTime = flight.arrivalTime
        nextCost = currentCost + flight.cost

        // IF we found a cheaper route, update
        IF nextCost < bestCost[nextAirport] THEN
          bestCost[nextAirport] = nextCost
          bestRoute[nextAirport] = (currentAirport, flight)
          Add (nextCost, nextAirport, nextTime) to priorityQueue

    // No route found
    RETURN empty itinerary
  ```

- Network Delay Time

  ```python
  ALGORITHM NetworkDelayTime(network, source, n)
    """Find the time it takes for a signal to reach all nodes from a source node."""
    // network is a graph of nodes and weighted edges representing signal delay
    // n is the number of nodes in the network

    Initialize delays map with infinity FOR all nodes
    Set delays[source] = 0
    Initialize priorityQueue with (0, source)
    Initialize visited set

    WHILE priorityQueue is not empty DO
      currentDelay, currentNode = Remove minimum from priorityQueue

      // Skip IF we've processed this node already
      IF currentNode in visited THEN
        CONTINUE

      // Mark as visited
      Add currentNode to visited

      // Check all adjacent nodes
      FOR each neighbor, weight in adjacency list of currentNode DO
        // Calculate new delay
        newDelay = currentDelay + weight

        // IF we found a faster signal path, update
        IF newDelay < delays[neighbor] THEN
          delays[neighbor] = newDelay
          Add (newDelay, neighbor) to priorityQueue

    // Check IF all nodes are reachable
    IF size of visited equals n THEN
      RETURN maximum value in delays  // Time FOR signal to reach all nodes
    ELSE
      RETURN -1  // Some nodes are unreachable
  ```

---

## 18. 0/1 Knapsack Pattern

A dynamic programming approach FOR selecting items with maximum value under a weight constraint.

**When to use**:

- Discrete items with values/weights
- Binary decisions (include/exclude)
- Maximizing/minimizing value with constraints

```python
def knapsack_01(values, weights, capacity):
    """Solves the 0/1 Knapsack problem using dynamic programming (2D DP table)."""
    n = len(values)
    # Initialize DP table
    dp = [[0 FOR _ in range(capacity + 1)] FOR _ in range(n + 1)]

    # Fill DP table
    FOR i in range(1, n + 1):
        FOR w in range(capacity + 1):
            # IF current item weight is more than capacity, skip it
            IF weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            ELSE:
                # Max of including or excluding current item
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w - weights[i-1]],  # Include item
                    dp[i-1][w]  # Exclude item
                )

    RETURN dp[n][capacity]

# Space-optimized version
def knapsack_01_optimized(values, weights, capacity):
    """Solves the 0/1 Knapsack problem using space-optimized dynamic programming (1D DP table)."""
    n = len(values)
    # Use 1D array since we only need previous row
    dp = [0 FOR _ in range(capacity + 1)]

    # Fill DP table
    FOR i in range(n):
        # Process in reverse to avoid overwriting values we still need
        FOR w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    RETURN dp[capacity]
```

**Time Complexity**: O(n *C) where n is items, C is capacity
**Space Complexity**: O(n* C), can be optimized to O(C)

**Example Use Cases**:

- 0/1 Knapsack

  ```python
  ALGORITHM Knapsack01(values, weights, capacity)
    """Maximize the value of items selected without exceeding capacity (0/1 choice)."""
    n = length of values

    // Initialize DP table
    Initialize dp[n+1][capacity+1] with all values as 0

    FOR i FROM 1 TO n DO
      FOR w FROM 0 TO capacity DO
        IF weights[i-1] > w THEN
          // Current item is too heavy FOR this capacity
          dp[i][w] = dp[i-1][w]
        ELSE
          // Max of including or excluding the current item
          dp[i][w] = MAX(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])

    RETURN dp[n][capacity]
  ```

- Subset Sum

  ```python
  ALGORITHM SubsetSum(nums, targetSum)
    """Determine if there exists a subset of nums that sums up to targetSum."""
    n = length of nums

    // Initialize DP table
    Initialize dp[n+1][targetSum+1] with dp[0][0] = true and rest false

    FOR i FROM 1 TO n DO
      FOR s FROM 0 TO targetSum DO
        IF s equals 0 THEN
          // Empty subset always sums to 0
          dp[i][s] = true
        ELSE IF nums[i-1] > s THEN
          // Current number is too large FOR this sum
          dp[i][s] = dp[i-1][s]
        ELSE
          // Either include or exclude current number
          dp[i][s] = dp[i-1][s] OR dp[i-1][s - nums[i-1]]

    RETURN dp[n][targetSum]
  ```

- Equal Subset Sum Partition

  ```python
  ALGORITHM CanPartition(nums)
    """Determine if an array can be partitioned into two subsets with equal sum."""
    totalSum = sum of all elements in nums

    // IF total sum is odd, equal partition is impossible
    IF totalSum is odd THEN
      RETURN false

    targetSum = totalSum / 2
    n = length of nums

    // Initialize DP table
    Initialize dp[n+1][targetSum+1] with dp[0][0] = true and rest false

    FOR i FROM 1 TO n DO
      FOR s FROM 0 TO targetSum DO
        IF s equals 0 THEN
          dp[i][s] = true
        ELSE IF nums[i-1] > s THEN
          dp[i][s] = dp[i-1][s]
        ELSE
          dp[i][s] = dp[i-1][s] OR dp[i-1][s - nums[i-1]]

    RETURN dp[n][targetSum]
  ```

- Minimum Subset Sum Difference

  ```python
  ALGORITHM MinSubsetSumDifference(nums)
    """Find the minimum absolute difference between the sums of two subsets of an array."""
    totalSum = sum of all elements in nums
    n = length of nums

    // Find all possible subset sums up to totalSum/2
    Initialize dp[n+1][totalSum/2 + 1] with dp[0][0] = true and rest false

    FOR i FROM 1 TO n DO
      FOR s FROM 0 TO totalSum/2 DO
        IF s equals 0 THEN
          dp[i][s] = true
        ELSE IF nums[i-1] > s THEN
          dp[i][s] = dp[i-1][s]
        ELSE
          dp[i][s] = dp[i-1][s] OR dp[i-1][s - nums[i-1]]

    // Find the largest subset sum that's possible
    largestPossibleSum = 0
    FOR s FROM totalSum/2 DOWN TO 0 DO
      IF dp[n][s] equals true THEN
        largestPossibleSum = s
        BREAK

    // Minimum difference is total sum minus twice the largest possible sum
    RETURN totalSum - 2 * largestPossibleSum
  ```

---

## 19. Unbounded Knapsack Pattern

A variation of the knapsack problem where items can be used multiple times.

**When to use**:

- Items can be used multiple times
- Selecting repeated elements with constraints
- Max/min value problems with unlimited supply

```python
def unbounded_knapsack(values, weights, capacity):
    """Solves the Unbounded Knapsack problem using dynamic programming."""
    # Initialize DP table
    dp = [0] * (capacity + 1)

    # Fill DP table
    FOR w in range(1, capacity + 1):
        FOR i in range(len(values)):
            IF weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    RETURN dp[capacity]

# Coin change problem (minimizing number of coins)
def coin_change(coins, amount):
    """Finds the minimum number of coins needed to make a given amount."""
    # Initialize with infinity FOR all amounts except 0
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    FOR coin in coins:
        FOR i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    RETURN dp[amount] IF dp[amount] != float('inf') ELSE -1

# Coin change (count number of ways)
def count_ways(coins, amount):
    """Counts the number of ways to make change for a given amount using given coins."""
    dp = [0] * (amount + 1)
    dp[0] = 1  # There is 1 way to make amount 0

    FOR coin in coins:
        FOR i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    RETURN dp[amount]
```

**Time Complexity**: O(n * C) where n is item types, C is capacity
**Space Complexity**: O(C)

**Example Use Cases**:

- Coin Change (min coins)

  ```python
  ALGORITHM MinimumCoins(coins, amount)
    """Find the minimum number of coins required to make a given amount."""
    // Initialize DP array with infinity except FOR 0
    Initialize dp[amount+1] with infinity
    Set dp[0] = 0  // 0 coins needed to make amount 0

    FOR i FROM 1 TO amount DO
      FOR each coin in coins DO
        IF coin <= i THEN
          // Take minimum of current value or 1 + value after using coin
          dp[i] = MIN(dp[i], 1 + dp[i - coin])

    IF dp[amount] equals infinity THEN
      RETURN -1  // Amount cannot be formed
    ELSE
      RETURN dp[amount]
  ```

- Coin Change II (number of ways)

  ```python
  ALGORITHM CountWays(coins, amount)
    """Count the total number of ways to make change for a given amount."""
    // Initialize DP array with zeros except FOR 0
    Initialize dp[amount+1] with 0
    Set dp[0] = 1  // 1 way to make amount 0 (use no coins)

    FOR each coin in coins DO
      FOR i FROM coin TO amount DO
        // Add the number of ways to make amount i - coin
        dp[i] += dp[i - coin]

    RETURN dp[amount]
  ```

- Rod Cutting

  ```python
  ALGORITHM RodCutting(prices, rodLength)
    """Find the maximum obtainable value by cutting up a rod and selling the pieces."""
    // prices[i] is the price of a rod of length i+1

    // Initialize DP array with 0
    Initialize dp[rodLength+1] with 0

    FOR len FROM 1 TO rodLength DO
      maxVal = 0

      FOR cutLen FROM 1 TO len DO
        // Try all possible cuts and pick the best
        maxVal = MAX(maxVal, prices[cutLen-1] + dp[len - cutLen])

      dp[len] = maxVal

    RETURN dp[rodLength]
  ```

- Maximum ribbon cut

  ```python
  ALGORITHM MaximumRibbonCut(ribbonLengths, totalLength)
    """Find the maximum number of pieces a ribbon can be cut into using given lengths."""
    // Initialize DP array with negative infinity except FOR 0
    Initialize dp[totalLength+1] with negative infinity
    Set dp[0] = 0  // 0 cuts needed FOR length 0

    FOR i FROM 1 TO totalLength DO
      FOR each length in ribbonLengths DO
        IF length <= i AND dp[i - length] is not negative infinity THEN
          // Maximum cuts = 1 + cuts after using current length
          dp[i] = MAX(dp[i], 1 + dp[i - length])

    IF dp[totalLength] is negative infinity THEN
      RETURN -1  // Cannot cut the ribbon into given lengths
    ELSE
      RETURN dp[totalLength]
  ```

---

## 20. Longest Common Subsequence (LCS) Pattern

A dynamic programming approach FOR finding common elements between sequences.

**When to use**:

- Problems comparing sequences
- Finding common elements or differences between strings
- Edit distance variations

```python
def longest_common_subsequence(text1, text2):
    """Finds the length of the longest common subsequence between two strings."""
    m, n = len(text1), len(text2)

    # Create DP table
    dp = [[0 FOR _ in range(n + 1)] FOR _ in range(m + 1)]

    # Fill DP table
    FOR i in range(1, m + 1):
        FOR j in range(1, n + 1):
            IF text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            ELSE:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    RETURN dp[m][n]

# Variation: Edit distance
def edit_distance(word1, word2):
    """Calculates the minimum number of operations (insert, delete, replace) to transform word1 to word2."""
    m, n = len(word1), len(word2)

    # Create DP table
    dp = [[0 FOR _ in range(n + 1)] FOR _ in range(m + 1)]

    # Initialize first row and column
    FOR i in range(m + 1):
        dp[i][0] = i
    FOR j in range(n + 1):
        dp[0][j] = j

    # Fill DP table
    FOR i in range(1, m + 1):
        FOR j in range(1, n + 1):
            IF word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            ELSE:
                dp[i][j] = 1 + min(
                    dp[i-1][j],    # Delete
                    dp[i][j-1],    # Insert
                    dp[i-1][j-1]   # Replace
                )

    RETURN dp[m][n]
```

**Time Complexity**: O(m *n) where m, n are string lengths
**Space Complexity**: O(m* n)

**Example Use Cases**:

- Longest Common Subsequence

  ```python
  ALGORITHM LCS(text1, text2)
    """Find the length of the Longest Common Subsequence between two strings."""
    m = length of text1
    n = length of text2

    // Initialize DP table
    Initialize dp[m+1][n+1] with 0

    FOR i FROM 1 TO m DO
      FOR j FROM 1 TO n DO
        IF text1[i-1] equals text2[j-1] THEN
          // IF characters match, add 1 to diagonal value
          dp[i][j] = dp[i-1][j-1] + 1
        ELSE
          // IF characters don't match, take max from left or above
          dp[i][j] = MAX(dp[i-1][j], dp[i][j-1])

    RETURN dp[m][n]
  ```

- Shortest Common Supersequence

  ```python
  ALGORITHM SCS(text1, text2)
    """Find the Shortest Common Supersequence of two strings."""
    m = length of text1
    n = length of text2

    // First find LCS using DP table
    Initialize dp[m+1][n+1] with 0

    FOR i FROM 1 TO m DO
      FOR j FROM 1 TO n DO
        IF text1[i-1] equals text2[j-1] THEN
          dp[i][j] = dp[i-1][j-1] + 1
        ELSE
          dp[i][j] = MAX(dp[i-1][j], dp[i][j-1])

    // Construct SCS by traversing the DP table backwards
    Initialize result as empty string
    i = m, j = n

    WHILE i > 0 AND j > 0 DO
      IF text1[i-1] equals text2[j-1] THEN
        // Add the common character once
        Add text1[i-1] to beginning of result
        Decrement i
        Decrement j
      ELSE IF dp[i-1][j] > dp[i][j-1] THEN
        // Character from text1 not in LCS
        Add text1[i-1] to beginning of result
        Decrement i
      ELSE
        // Character from text2 not in LCS
        Add text2[j-1] to beginning of result
        Decrement j

    // Add remaining characters from text1
    WHILE i > 0 DO
      Add text1[i-1] to beginning of result
      Decrement i

    // Add remaining characters from text2
    WHILE j > 0 DO
      Add text2[j-1] to beginning of result
      Decrement j

    RETURN result
  ```

- Edit Distance

  ```python
  ALGORITHM EditDistance(word1, word2)
    """Calculate the minimum edit distance (Levenshtein distance) between two words."""
    m = length of word1
    n = length of word2

    // Initialize DP table
    Initialize dp[m+1][n+1] with dp[i][0] = i and dp[0][j] = j

    FOR i FROM 1 TO m DO
      FOR j FROM 1 TO n DO
        IF word1[i-1] equals word2[j-1] THEN
          // No operation needed IF characters match
          dp[i][j] = dp[i-1][j-1]
        ELSE
          // Minimum of insert, delete, or replace
          dp[i][j] = 1 + MIN(
            dp[i][j-1],    // Insert
            dp[i-1][j],    // Delete
            dp[i-1][j-1]   // Replace
          )

    RETURN dp[m][n]
  ```

- Longest Palindromic Subsequence

  ```python
  ALGORITHM LPS(text)
    """Find the length of the Longest Palindromic Subsequence within a string."""
    n = length of text

    // Initialize DP table: dp[i][j] = length of LPS in text[i...j]
    Initialize dp[n][n] with 1s on diagonal (i=j)

    // Check subsequences of increasing length
    FOR len FROM 2 TO n DO
      FOR i FROM 0 TO n-len DO
        j = i + len - 1

        IF text[i] equals text[j] THEN
          // IF outer characters match, add 2 to inner palindrome length
          dp[i][j] = dp[i+1][j-1] + 2
        ELSE
          // IF outer characters don't match, take max excluding either end
          dp[i][j] = MAX(dp[i+1][j], dp[i][j-1])

    RETURN dp[0][n-1]
  ```

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
    """Calculates the nth Fibonacci number using recursion with memoization (top-down)."""
    IF n in memo:
        RETURN memo[n]
    IF n <= 1:
        RETURN n

    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    RETURN memo[n]

# Bottom-up approach (tabulation)
def fibonacci_tabulation(n):
    """Calculates the nth Fibonacci number using tabulation (bottom-up DP)."""
    IF n <= 1:
        RETURN n

    dp = [0] * (n + 1)
    dp[1] = 1

    FOR i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    RETURN dp[n]

# Space-optimized version
def fibonacci_optimized(n):
    """Calculates the nth Fibonacci number using space-optimized bottom-up DP."""
    IF n <= 1:
        RETURN n

    a, b = 0, 1
    FOR _ in range(2, n + 1):
        a, b = b, a + b

    RETURN b

# Example: Climbing stairs problem
def climb_stairs(n):
    """Calculates the number of distinct ways to climb n stairs (taking 1 or 2 steps)."""
    IF n <= 2:
        RETURN n

    a, b = 1, 2
    FOR _ in range(3, n + 1):
        a, b = b, a + b

    RETURN b
```

**Time Complexity**: O(n)
**Space Complexity**: O(n) can be optimized to O(1)

**Example Use Cases**:

- Fibonacci Numbers

  ```python
  ALGORITHM Fibonacci(n)
    """Calculate the nth Fibonacci number iteratively (space-optimized)."""
    // Handle base cases
    IF n <= 1 THEN
      RETURN n

    // Initialize first two Fibonacci numbers
    Initialize a = 0, b = 1

    // Calculate nth Fibonacci number iteratively
    FOR i FROM 2 TO n DO
      // Calculate next Fibonacci number
      Set temp = a + b
      Set a = b
      Set b = temp

    RETURN b
  ```

- Climbing Stairs

  ```python
  ALGORITHM ClimbStairs(n)
    """Calculate the number of distinct ways to climb n stairs."""
    // Handle base cases
    IF n <= 2 THEN
      RETURN n

    // Initialize ways to climb 1 and 2 steps
    Initialize oneStep = 1, twoStep = 2

    // Calculate ways to climb n steps
    FOR i FROM 3 TO n DO
      // Calculate ways to reach current step
      Set current = oneStep + twoStep
      Set oneStep = twoStep
      Set twoStep = current

    RETURN twoStep
  ```

- House Thief (non-adjacent elements)

  ```python
  ALGORITHM HouseThief(houses)
    """Find the maximum amount of money a thief can rob from houses without robbing adjacent ones."""
    n = length of houses

    // Handle base cases
    IF n equals 0 THEN
      RETURN 0
    IF n equals 1 THEN
      RETURN houses[0]

    // Initialize DP array: max money at each house
    Initialize dp[n]
    Set dp[0] = houses[0]
    Set dp[1] = MAX(houses[0], houses[1])

    FOR i FROM 2 TO n-1 DO
      // Either rob current house + money from i-2, or skip current house
      dp[i] = MAX(houses[i] + dp[i-2], dp[i-1])

    RETURN dp[n-1]
  ```

---

## 22. Subsets Pattern

A backtracking approach FOR generating combinations of elements.

**When to use**:

- Generating all possible subsets/combinations/permutations
- Need to explore multiple choices at each step
- Building combinations with specific constraints

```python
def generate_subsets(nums):
    """Generates all possible subsets (the power set) of a given set of numbers."""
    result = []

    def backtrack(start, current):
        # Add the current subset to the result
        result.append(current[:])

        # Try including each remaining element
        FOR i in range(start, len(nums)):
            # Include nums[i]
            current.append(nums[i])
            # Recurse with next position
            backtrack(i + 1, current)
            # Backtrack (exclude nums[i])
            current.pop()

    backtrack(0, [])
    RETURN result

def generate_permutations(nums):
    """Generates all possible permutations of a given set of numbers."""
    result = []

    def backtrack(start):
        # IF we've used all numbers, add permutation to result
        IF start == len(nums):
            result.append(nums[:])
            RETURN

        # Try each number at the current position
        FOR i in range(start, len(nums)):
            # SWAP to place nums[i] at position start
            nums[start], nums[i] = nums[i], nums[start]
            # Recurse with next position
            backtrack(start + 1)
            # Backtrack (restore original order)
            nums[start], nums[i] = nums[i], nums[start]

    backtrack(0)
    RETURN result

def combination_sum(candidates, target):
    """Finds all unique combinations in candidates where the numbers sum to target (elements can be reused)."""
    result = []

    def backtrack(start, current, remaining):
        IF remaining == 0:
            result.append(current[:])
            RETURN
        IF remaining < 0:
            RETURN

        FOR i in range(start, len(candidates)):
            current.append(candidates[i])
            backtrack(i, current, remaining - candidates[i])  # Can reuse same element
            current.pop()

    backtrack(0, [], target)
    RETURN result
```

**Time Complexity**: O(2^n) FOR subsets, O(n!) FOR permutations
**Space Complexity**: O(n) FOR recursion stack

**Example Use Cases**:

- Generate Subsets/Powerset

  ```python
  ALGORITHM GenerateSubsets(nums)
    """Generate all possible subsets (powerset) of a given array using backtracking."""
    Initialize result as empty list

    FUNCTION Backtrack(start, current)
      // Add the current subset to the result
      Add a copy of current to result

      // Try including each remaining element
      FOR i FROM start TO length of nums - 1 DO
        // Include nums[i]
        Add nums[i] to current

        // Recurse with next position
        Call Backtrack(i + 1, current)

        // Backtrack (exclude nums[i])
        Remove last element from current

    // Start the recursion
    Call Backtrack(0, empty list)
    RETURN result
  ```

- Permutations

  ```python
  ALGORITHM GeneratePermutations(nums)
    """Generate all possible permutations of an array using backtracking with swaps."""
    Initialize result as empty list

    FUNCTION Backtrack(start)
      // IF we've used all numbers, add permutation to result
      IF start equals length of nums THEN
        Add a copy of nums to result
        RETURN

      // Try each number at the current position
      FOR i FROM start TO length of nums - 1 DO
        // SWAP to place nums[i] at position start
        SWAP nums[start] with nums[i]

        // Recurse with next position
        Call Backtrack(start + 1)

        // Backtrack (restore original order)
        SWAP nums[start] with nums[i] back

    // Start the recursion
    Call Backtrack(0)
    RETURN result
  ```

- Combinations

  ```python
  ALGORITHM GenerateCombinations(n, k)
    """Generate all possible combinations of k numbers chosen from 1 to n."""
    Initialize result as empty list

    FUNCTION Backtrack(start, current)
      // IF we have selected k elements, add to result
      IF length of current equals k THEN
        Add a copy of current to result
        RETURN

      // Try each remaining number
      FOR i FROM start TO n DO
        // Include i
        Add i to current

        // Recurse with next number
        Call Backtrack(i + 1, current)

        // Backtrack (exclude i)
        Remove last element from current

    // Start the recursion
    Call Backtrack(1, empty list)
    RETURN result
  ```

- Letter Combinations of Phone Number

  ```python
  ALGORITHM LetterCombinations(digits)
    """Generate all possible letter combinations that a phone number could represent."""
    // Map digits to letters
    Initialize digitToLetters map:
      '2' -> "abc", '3' -> "def", '4' -> "ghi", '5' -> "jkl",
      '6' -> "mno", '7' -> "pqrs", '8' -> "tuv", '9' -> "wxyz"

    Initialize result as empty list

    // Handle empty input
    IF digits is empty THEN
      RETURN result

    FUNCTION Backtrack(index, current)
      // IF we've processed all digits, add combination to result
      IF index equals length of digits THEN
        Add current string to result
        RETURN

      // Get all letters FOR current digit
      Set currentDigit = digits[index]
      Set letters = digitToLetters[currentDigit]

      // Try each letter
      FOR each letter in letters DO
        // Add letter to current combination
        Append letter to current

        // Recurse with next digit
        Call Backtrack(index + 1, current + letter)

    // Start the recursion
    Call Backtrack(0, empty string)
    RETURN result
  ```

---

## 23. Constraint Satisfaction Pattern

A backtracking approach FOR problems with complex constraints.

**When to use**:

- Problems with complex constraints
- Search space can be pruned early
- Need to find all valid solutions or one valid solution

```python
# Example: Sudoku Solver
def solve_sudoku(board):
    """Solves a Sudoku puzzle using backtracking."""
    # Find an empty cell
    def find_empty():
        FOR r in range(9):
            FOR c in range(9):
                IF board[r][c] == '.':
                    RETURN r, c
        RETURN None

    # Check IF num can be placed at (row, col)
    def is_valid(row, col, num):
        # Check row
        FOR c in range(9):
            IF board[row][c] == num:
                RETURN False

        # Check column
        FOR r in range(9):
            IF board[r][col] == num:
                RETURN False

        # Check 3x3 box
        box_row, box_col = 3 * (row // 3), 3 * (col // 3)
        FOR r in range(box_row, box_row + 3):
            FOR c in range(box_col, box_col + 3):
                IF board[r][c] == num:
                    RETURN False

        RETURN True

    def backtrack():
        # Find an empty cell
        empty = find_empty()
        IF not empty:
            RETURN True  # Solved

        row, col = empty

        # Try each possible number
        FOR num in '123456789':
            IF is_valid(row, col, num):
                # Place number
                board[row][col] = num

                # Recurse
                IF backtrack():
                    RETURN True

                # Backtrack
                board[row][col] = '.'

        RETURN False  # No solution

    backtrack()
    RETURN board

# Example: N-Queens
def solve_n_queens(n):
    """Finds all distinct solutions to the N-Queens puzzle using backtracking."""
    result = []

    # Initialize empty board
    board = [['.' FOR _ in range(n)] FOR _ in range(n)]

    # Check IF a queen can be placed at (row, col)
    def is_safe(row, col):
        # Check column
        FOR i in range(row):
            IF board[i][col] == 'Q':
                RETURN False

        # Check upper-left diagonal
        i, j = row - 1, col - 1
        WHILE i >= 0 and j >= 0:
            IF board[i][j] == 'Q':
                RETURN False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, col + 1
        WHILE i >= 0 and j < n:
            IF board[i][j] == 'Q':
                RETURN False
            i -= 1
            j += 1

        RETURN True

    def backtrack(row):
        IF row == n:
            # Add current board state to result
            result.append([''.join(row) FOR row in board])
            RETURN

        FOR col in range(n):
            IF is_safe(row, col):
                # Place queen
                board[row][col] = 'Q'

                # Recurse to next row
                backtrack(row + 1)

                # Backtrack
                board[row][col] = '.'

    backtrack(0)
    RETURN result
```

**Time Complexity**: Exponential, but pruning reduces actual runtime
**Space Complexity**: O(n) FOR recursion stack

**Example Use Cases**:

- N-Queens

  ```python
  ALGORITHM SolveNQueens(n)
    """Find all distinct solutions to the N-Queens puzzle using backtracking."""
    Initialize result as empty list
    Initialize board as n×n matrix filled with '.'

    FUNCTION IsSafe(row, col)
      // Check column
      FOR i FROM 0 TO row-1 DO
        IF board[i][col] equals 'Q' THEN
          RETURN false

      // Check upper-left diagonal
      Set i = row-1, j = col-1
      WHILE i >= 0 AND j >= 0 DO
        IF board[i][j] equals 'Q' THEN
          RETURN false
        Decrement i
        Decrement j

      // Check upper-right diagonal
      Set i = row-1, j = col+1
      WHILE i >= 0 AND j < n DO
        IF board[i][j] equals 'Q' THEN
          RETURN false
        Decrement i
        Increment j

      RETURN true

    FUNCTION Backtrack(row)
      // IF all queens are placed, add solution
      IF row equals n THEN
        Add current board configuration to result
        RETURN

      // Try placing queen in each column of current row
      FOR col FROM 0 TO n-1 DO
        IF IsSafe(row, col) THEN
          // Place queen
          Set board[row][col] = 'Q'

          // Recurse to next row
          Call Backtrack(row + 1)

          // Backtrack (remove queen)
          Set board[row][col] = '.'

    // Start the recursion
    Call Backtrack(0)
    RETURN result
  ```

- Sudoku Solver

  ```python
  ALGORITHM SolveSudoku(board)
    """Solve a Sudoku puzzle using backtracking."""
    FUNCTION FindEmpty()
      FOR row FROM 0 TO 8 DO
        FOR col FROM 0 TO 8 DO
          IF board[row][col] equals '.' THEN
            RETURN row, col
      RETURN null  // No empty cell found

    FUNCTION IsValid(row, col, num)
      // Check row
      FOR c FROM 0 TO 8 DO
        IF board[row][c] equals num THEN
          RETURN false

      // Check column
      FOR r FROM 0 TO 8 DO
        IF board[r][col] equals num THEN
          RETURN false

      // Check 3×3 box
      Set boxRow = 3 * (row / 3)  // Integer division
      Set boxCol = 3 * (col / 3)  // Integer division

      FOR r FROM boxRow TO boxRow+2 DO
        FOR c FROM boxCol TO boxCol+2 DO
          IF board[r][c] equals num THEN
            RETURN false

      RETURN true

    FUNCTION Backtrack()
      // Find an empty cell
      Set cell = FindEmpty()

      // IF no empty cell, puzzle is solved
      IF cell is null THEN
        RETURN true

      Set row, col = cell

      // Try each possible number
      FOR num FROM '1' TO '9' DO
        IF IsValid(row, col, num) THEN
          // Place the number
          Set board[row][col] = num

          // Recursively solve rest of puzzle
          IF Backtrack() equals true THEN
            RETURN true

          // Backtrack IF solution not found
          Set board[row][col] = '.'

      RETURN false  // Trigger backtracking

    // Start solving
    Call Backtrack()
    RETURN board
  ```

- Word Search

  ```python
  ALGORITHM WordSearch(board, word)
    """Determine if a word exists in a grid by searching adjacent cells."""
    m = number of rows in board
    n = number of columns in board

    FUNCTION DFS(row, col, index)
      // IF we've matched the entire word
      IF index equals length of word THEN
        RETURN true

      // Check bounds and character match
      IF row < 0 OR row >= m OR col < 0 OR col >= n OR
         board[row][col] does not equal word[index] THEN
        RETURN false

      // Mark as visited
      Set temp = board[row][col]
      Set board[row][col] = '#'  // Temporary mark

      // Try all four directions
      Set found = DFS(row+1, col, index+1) OR
                  DFS(row-1, col, index+1) OR
                  DFS(row, col+1, index+1) OR
                  DFS(row, col-1, index+1)

      // Restore the cell
      Set board[row][col] = temp

      RETURN found

    // Try starting from each cell
    FOR row FROM 0 TO m-1 DO
      FOR col FROM 0 TO n-1 DO
        IF DFS(row, col, 0) equals true THEN
          RETURN true

    RETURN false
  ```

- Palindrome Partitioning

  ```python
  ALGORITHM PalindromePartition(s)
    """Partition a string such that every substring of the partition is a palindrome."""
    Initialize result as empty list

    FUNCTION IsPalindrome(start, end)
      WHILE start < end DO
        IF s[start] does not equal s[end] THEN
          RETURN false
        Increment start
        Decrement end
      RETURN true

    FUNCTION Backtrack(start, current)
      // IF we've processed the entire string
      IF start equals length of s THEN
        Add a copy of current to result
        RETURN

      // Try different ending positions FOR current substring
      FOR end FROM start TO length of s - 1 DO
        // IF substring is palindrome, add it and CONTINUE
        IF IsPalindrome(start, end) THEN
          // Add current palindrome substring to partition
          Add s[start:end+1] to current

          // Recursively partition the remaining string
          Call Backtrack(end + 1, current)

          // Backtrack
          Remove last element from current

    // Start the recursion
    Call Backtrack(0, empty list)
    RETURN result
  ```

---

## 24. Top K Elements Pattern

A heap-based pattern FOR finding the most frequent or largest elements.

**When to use**:

- Finding top/smallest K elements
- Stream processing with limited memory
- Maintaining a running set of maximum/minimum elements

```python
import heapq

def find_k_largest(nums, k):
    """Finds the K largest elements in an array using a min-heap."""
    # Use a min heap of size k
    min_heap = []

    FOR num in nums:
        IF len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    RETURN min_heap

def top_k_frequent(nums, k):
    """Finds the K most frequent elements in an array using a frequency map and a min-heap."""
    # Count frequency
    counter = {}
    FOR num in nums:
        counter[num] = counter.get(num, 0) + 1

    # Use min heap to keep track of k most frequent elements
    min_heap = []

    FOR num, count in counter.items():
        IF len(min_heap) < k:
            heapq.heappush(min_heap, (count, num))
        elif count > min_heap[0][0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, (count, num))

    # Extract result
    result = []
    WHILE min_heap:
        result.append(heapq.heappop(min_heap)[1])

    # Reverse to get highest frequency first
    RETURN result[::-1]

def k_closest_points(points, k):
    """Finds the K points closest to the origin using a max-heap."""
    # Use max heap to keep k closest points
    max_heap = []

    FOR x, y in points:
        # Calculate distance (no need FOR square root)
        dist = x*x + y*y

        IF len(max_heap) < k:
            # Negate distance FOR max heap
            heapq.heappush(max_heap, (-dist, [x, y]))
        elif -dist > max_heap[0][0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, (-dist, [x, y]))

    # Extract result
    RETURN [point FOR _, point in max_heap]
```

**Time Complexity**: O(n log k) FOR processing n elements with heap of size k
**Space Complexity**: O(k) FOR the heap

**Example Use Cases**:

- Kth Largest Element

  ```python
  ALGORITHM FindKthLargest(nums, k)
    """Find the Kth largest element in an unsorted array using a min-heap."""
    // Use min heap of size k
    Initialize minHeap as empty heap

    FOR each num in nums DO
      IF size of minHeap < k THEN
        Add num to minHeap
      ELSE IF num > smallest element in minHeap THEN
        Remove smallest element from minHeap
        Add num to minHeap

    // The smallest element in the heap is the kth largest overall
    RETURN smallest element in minHeap
  ```

- K Closest Points to Origin

  ```python
  ALGORITHM KClosestPoints(points, k)
    """Find the K points closest to the origin using a max-heap."""
    // Use max heap to keep k closest points
    Initialize maxHeap as empty heap

    FOR each point (x, y) in points DO
      // Calculate distance (no need FOR square root)
      distance = x² + y²

      IF size of maxHeap < k THEN
        // Store negative distance FOR max heap behavior
        Add (-distance, point) to maxHeap
      ELSE IF -distance > largest negative distance in maxHeap THEN
        Remove element with largest negative distance from maxHeap
        Add (-distance, point) to maxHeap

    // Extract points from the heap
    Initialize result as empty list
    WHILE maxHeap is not empty DO
      Add point from top of maxHeap to result
      Remove top element from maxHeap

    RETURN result
  ```

- Top K Frequent Elements

  ```python
  ALGORITHM TopKFrequent(nums, k)
    """Find the K most frequent elements in an array."""
    // Count frequencies
    Initialize frequency map
    FOR each num in nums DO
      Increment frequency[num]

    // Use min heap to find k most frequent elements
    Initialize minHeap as empty heap

    FOR each (num, count) in frequency map DO
      IF size of minHeap < k THEN
        Add (count, num) to minHeap
      ELSE IF count > smallest count in minHeap THEN
        Remove element with smallest count from minHeap
        Add (count, num) to minHeap

    // Extract elements from heap
    Initialize result as empty list
    WHILE minHeap is not empty DO
      Add number from top of minHeap to result
      Remove top element from minHeap

    // Reverse to get highest frequency first
    RETURN result in reverse order
  ```

- Sort K-sorted Array

  ```python
  ALGORITHM SortKSortedArray(nums, k)
    """Sort an array where each element is at most k positions away from its sorted position."""
    // Each element is at most k positions away from its sorted position
    // Use min heap of size k+1
    Initialize minHeap as empty heap
    Initialize result as empty list

    FOR each num in nums DO
      // Add current element to heap
      Add num to minHeap

      // IF heap size exceeds k+1, remove and add to result
      IF size of minHeap > k+1 THEN
        Add smallest element from minHeap to result
        Remove smallest element from minHeap

    // Add remaining elements from heap to result
    WHILE minHeap is not empty DO
      Add smallest element from minHeap to result
      Remove smallest element from minHeap

    RETURN result
  ```

---

## 25. Two Heaps Pattern

A pattern FOR problems requiring tracking of median elements.

**When to use**:

- Median calculation problems
- Balancing elements on either side of a midpoint
- Processing stream data with statistics

```python
import heapq

CLASS MedianFinder:
    """Data structure to find the median from a data stream using two heaps."""
    def __init__(self):
        """Initializes the MedianFinder with two heaps."""
        self.small = []  # Max-heap FOR smaller half
        self.large = []  # Min-heap FOR larger half

    def addNum(self, num):
        """Adds a number to the data structure and rebalances the heaps."""
        # Add to max_heap
        heapq.heappush(self.small, -num)

        # Balance heaps: ensure max of small <= min of large
        # Move largest element from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Ensure small has at least as many elements as large
        IF len(self.small) < len(self.large):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self):
        """Returns the median of all elements seen so far."""
        IF len(self.small) > len(self.large):
            RETURN -self.small[0]
        ELSE:
            RETURN (-self.small[0] + self.large[0]) / 2.0

CLASS SlidingWindowMedian:
    """Calculates the median of a sliding window using two heaps (less optimal removal)."""
    def __init__(self):
        """Initializes the heaps for sliding window median calculation."""
        self.max_heap = []  # FOR smaller half
        self.min_heap = []  # FOR larger half

    def find_sliding_window_median(self, nums, k):
        """Calculates the median for each sliding window of size k."""
        result = []

        FOR i, num in enumerate(nums):
            # Add new element
            self.add_num(num)

            # Remove element outside window
            IF i >= k:
                self.remove_num(nums[i - k])

            # Calculate median once window is full
            IF i >= k - 1:
                result.append(self.find_median())

        RETURN result

    def add_num(self, num):
        """Adds a number to the heaps and rebalances."""
        # Add to max_heap
        heapq.heappush(self.max_heap, -num)

        # Balance heaps
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        # Ensure max_heap has at least as many elements as min_heap
        IF len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def remove_num(self, num):
        """Removes a number from the heaps and rebalances (O(k) complexity)."""
        # Remove from proper heap
        IF num <= -self.max_heap[0]:
            self.max_heap.remove(-num)
            heapq.heapify(self.max_heap)
        ELSE:
            self.min_heap.remove(num)
            heapq.heapify(self.min_heap)

        # Rebalance IF needed
        IF len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def find_median(self):
        """Finds the median from the current state of the heaps."""
        IF len(self.max_heap) > len(self.min_heap):
            RETURN -self.max_heap[0]
        ELSE:
            RETURN (-self.max_heap[0] + self.min_heap[0]) / 2.0
```

**Time Complexity**: O(log n) per element insertion
**Space Complexity**: O(n) FOR storing all elements

**Example Use Cases**:

- Find Median from Data Stream

  ```python
  CLASS MedianFinder
    """Pseudocode for finding median from a data stream using two heaps."""
    CONSTRUCTOR
      Initialize maxHeap (FOR smaller half) as empty heap
      Initialize minHeap (FOR larger half) as empty heap

    METHOD AddNum(num)
      """Adds a number and rebalances the heaps."""
      // Add to max heap (FOR smaller half)
      // Note: we use negative values since most heap implementations
      // are min heaps by default
      Add -num to maxHeap

      // Balance: ensure max of maxHeap <= min of minHeap
      IF maxHeap is not empty AND minHeap is not empty AND
         -maxHeap.top() > minHeap.top() THEN
        Move -maxHeap.top() to minHeap

      // Balance heap sizes
      IF size of maxHeap > size of minHeap + 1 THEN
        Move -maxHeap.top() to minHeap
      ELSE IF size of minHeap > size of maxHeap THEN
        Move minHeap.top() to maxHeap as negative value

    METHOD FindMedian()
      """Calculates the median from the current heaps."""
      IF size of maxHeap > size of minHeap THEN
        RETURN -maxHeap.top()  // Odd number of elements
      ELSE
        RETURN (-maxHeap.top() + minHeap.top()) / 2  // Even number
  ```

- Sliding Window Median

  ```python
  ALGORITHM SlidingWindowMedian(nums, k)
    """Calculate the median of each sliding window of size k."""
    // Create heaps
    Initialize maxHeap (FOR smaller half) as empty heap
    Initialize minHeap (FOR larger half) as empty heap
    Initialize result as empty list

    FUNCTION AddNum(num)
      // Add to appropriate heap
      IF maxHeap is empty OR num <= -maxHeap.top() THEN
        Add -num to maxHeap
      ELSE
        Add num to minHeap

      // Balance heaps

# Note: The remove_num implementation using list.remove() and heapify()
# has O(k) complexity, leading to an overall O(n*k) time complexity.
# More optimal O(n log k) solutions exist using lazy deletion or balanced BSTs.
      IF size of maxHeap > size of minHeap + 1 THEN
        Remove -maxHeap.top() and add to minHeap
      ELSE IF size of minHeap > size of maxHeap THEN
        Remove minHeap.top() and add to maxHeap as negative

    FUNCTION RemoveNum(num)
      // Remove the element from the appropriate heap
      IF num <= -maxHeap.top() THEN
        Remove -num from maxHeap
      ELSE
        Remove num from minHeap

      // Rebalance IF needed
      IF size of maxHeap > size of minHeap + 1 THEN
        Remove -maxHeap.top() and add to minHeap
      ELSE IF size of minHeap > size of maxHeap THEN
        Remove minHeap.top() and add to maxHeap as negative

    FUNCTION FindMedian()
      IF size of maxHeap > size of minHeap THEN
        RETURN -maxHeap.top()
      ELSE
        RETURN (-maxHeap.top() + minHeap.top()) / 2

    // Process each window
    FOR i FROM 0 TO length of nums - 1 DO
      // Add current element
      AddNum(nums[i])

      // Remove element outside window
      IF i >= k THEN
        RemoveNum(nums[i - k])

      // Calculate median once window is full
      IF i >= k - 1 THEN
        Add FindMedian() to result

    RETURN result
  ```

- IPO (maximize capital)

  ```python
  ALGORITHM FindMaximizedCapital(k, w, profits, capital)
    """Maximize capital by selecting up to k projects within capital constraints."""
    // k: number of projects to select
    // w: initial capital
    // profits: profits FOR each project
    // capital: capital required FOR each project

    // Create pairs of (capital, profit)
    Initialize projects as empty list
    FOR i FROM 0 TO length of profits - 1 DO
      Add (capital[i], profits[i]) to projects

    Sort projects by capital required (ascending)

    Initialize minCapitalHeap (stores projects we can afford) as empty
    Initialize maxProfitHeap (stores available project profits) as empty

    Initialize i = 0 (index into projects)

    // Select k projects
    FOR _ FROM 1 TO k DO
      // Add all projects we can afford to maxProfitHeap
      WHILE i < length of projects AND projects[i].capital <= w DO
        Add projects[i].profit to maxProfitHeap
        Increment i

      // IF no project is available, BREAK
      IF maxProfitHeap is empty THEN
        BREAK

      // Select the most profitable project
      w += maxProfitHeap.top()
      Remove top from maxProfitHeap

    RETURN w  // Final capital
  ```

---

## 26. Bit Manipulation

A set of techniques FOR manipulating individual bits in integers.

**When to use**:

- Problems involving binary representation
- XOR, AND, OR operations
- Problems requiring space optimization
- Numeric problems that can exploit bit properties

```python
# Common bit manipulation operations
def bit_operations():
    """Demonstrates common bitwise operations (AND, OR, XOR, NOT, shifts)."""
# Note: WHILE IPO uses two heaps, it represents a "K-Selection with Constraints"
# pattern rather than the typical median-finding structure of this section.

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

    RETURN bit_and, bit_or, bit_xor, bit_not, left_shift, right_shift

# Counting bits in a number
def count_bits(n):
    """Counts the number of set bits (1s) in the binary representation of n."""
    count = 0
    WHILE n:
        count += n & 1  # Check IF least significant bit is 1
        n >>= 1         # Right shift by 1
    RETURN count

# Power of two check
def is_power_of_two(n):
    """Checks if a number is a power of two using bit manipulation."""
    RETURN n > 0 and (n & (n - 1)) == 0

# XOR to find single number among duplicates
def find_single_number(nums):
    """Finds the single number that appears only once in an array where others appear twice, using XOR."""
    result = 0
    FOR num in nums:
        result ^= num
    RETURN result

# Setting, clearing, and checking bits
def set_bit(num, i):
    """Sets the ith bit of num to 1."""
    RETURN num | (1 << i)

def clear_bit(num, i):
    """Clears the ith bit of num to 0."""
    RETURN num & ~(1 << i)

def toggle_bit(num, i):
    """Toggles the ith bit of num."""
    RETURN num ^ (1 << i)

def check_bit(num, i):
    """Checks if the ith bit of num is set (1)."""
    RETURN (num >> i) & 1
```

**Time Complexity**: O(1) to O(n) depending on problem
**Space Complexity**: Usually O(1)

**Example Use Cases**:

- Counting bits

  ```python
  ALGORITHM CountBits(n)
    """Count the number of set bits (1s) in the binary representation of n."""
    Initialize count = 0

    WHILE n > 0 DO
      // Check IF least significant bit is 1
      IF n & 1 equals 1 THEN
        Increment count

      // Right shift by 1 bit
      n = n >> 1

    RETURN count
  ```

- Finding single number among duplicates

  ```python
  ALGORITHM FindSingleNumber(nums)
    """Find the single element appearing once in an array where others appear twice."""
    // Given array where all elements appear twice except one
    Initialize result = 0

    FOR each num in nums DO
      // XOR operation cancels out duplicate numbers
      result = result XOR num

    RETURN result
  ```

- Power set generation via bits

  ```python
  ALGORITHM GeneratePowerSet(nums)
    """Generate all subsets (powerset) of an array using bit manipulation."""
    Initialize n = length of nums
    Initialize total = 2^n  // Number of subsets
    Initialize result as empty list

    // Each number from 0 to 2^n-1 represents a subset
    FOR i FROM 0 TO total-1 DO
      Initialize current as empty list

      // Check each bit position
      FOR j FROM 0 TO n-1 DO
        // IF jth bit is set in i, include nums[j]
        IF (i & (1 << j)) != 0 THEN
          Add nums[j] to current

      Add current to result

    RETURN result
  ```

- Bit manipulation tricks

  ```python
  // Check IF a number is power of 2
  ALGORITHM IsPowerOfTwo(n)
    """Check if a number is a power of two using bit manipulation."""
    // A power of 2 has exactly one bit set to 1
    // n & (n-1) clears the lowest set bit
    IF n <= 0 THEN
      RETURN false

    RETURN (n & (n-1)) equals 0
  ```

  ```python
  // Get, Set, Clear, Toggle bits
  ALGORITHM SetBit(num, i)
    """Set the ith bit of a number to 1."""
    // Set the ith bit to 1
    RETURN num | (1 << i)

  ALGORITHM ClearBit(num, i)
    """Clear the ith bit of a number to 0."""
    // Clear the ith bit to 0
    RETURN num & ~(1 << i)

  ALGORITHM ToggleBit(num, i)
    """Toggle (flip) the ith bit of a number."""
    // Toggle the ith bit
    RETURN num ^ (1 << i)

  ALGORITHM CheckBit(num, i)
    """Check if the ith bit of a number is set (1)."""
    // Check IF ith bit is 1
    RETURN (num >> i) & 1 equals 1
  ```

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
    """Selects the maximum number of non-overlapping activities using a greedy approach."""
    # Sort activities by finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    selected = [activities[0]]
    last_finish = activities[0][1]

    FOR i in range(1, len(activities)):
        # IF current activity starts after the finish of last selected activity
        IF activities[i][0] >= last_finish:
            selected.append(activities[i])
            last_finish = activities[i][1]

    RETURN selected

# Minimum number of intervals to remove to make rest non-overlapping
def erase_overlap_intervals(intervals):
    """Finds the minimum number of intervals to remove to make the rest non-overlapping."""
    IF not intervals:
        RETURN 0

    # Sort by end time
    intervals.sort(key=lambda x: x[1])

    end = intervals[0][1]
    count = 1  # Count of non-overlapping intervals

    FOR i in range(1, len(intervals)):
        IF intervals[i][0] >= end:
            # Current interval doesn't overlap with previous
            end = intervals[i][1]
            count += 1

    # RETURN number of intervals to remove
    RETURN len(intervals) - count

# Jump Game - determine IF you can reach the end
def can_jump(nums):
    """Determines if the end of an array can be reached by jumping (greedy approach)."""
    max_reach = 0

    FOR i in range(len(nums)):
        # IF current position is beyond max reach, we can't get here
        IF i > max_reach:
            RETURN False

        # Update max reach from current position
        max_reach = max(max_reach, i + nums[i])

        # IF we can reach the end, RETURN early
        IF max_reach >= len(nums) - 1:
            RETURN True

    RETURN max_reach >= len(nums) - 1
```

**Time Complexity**: Usually O(n log n) due to sorting
**Space Complexity**: Usually O(1) or O(n)

**Example Use Cases**:

- Activity Selection

  ```python
  ALGORITHM ActivitySelection(start, finish)
    """Select the maximum number of non-overlapping activities."""
    // Create activities as pairs of (start, finish) times
    Initialize activities as list of pairs from start and finish arrays

    // Sort activities by finish time (ascending)
    Sort activities by finish time

    Initialize selected as [activities[0]]
    Set lastFinish = activities[0].finish

    FOR i FROM 1 TO length of activities - 1 DO
      // IF current activity starts after the finish of last selected
      IF activities[i].start >= lastFinish THEN
        Add activities[i] to selected
        Set lastFinish = activities[i].finish

    RETURN selected
  ```

- Huffman Coding

  ```python
  ALGORITHM HuffmanCoding(chars, frequencies)
    """Build a Huffman Tree and generate codes for character compression."""
    // Create a priority queue (min heap) of nodes
    Initialize minHeap

    // Create a leaf node FOR each character and add to heap
    FOR i FROM 0 TO length of chars - 1 DO
      Create node with chars[i] and frequencies[i]
      Add node to minHeap

    // Build Huffman Tree
    WHILE size of minHeap > 1 DO
      // Extract two nodes with lowest frequency
      left = Extract min from minHeap
      right = Extract min from minHeap

      // Create a new internal node with these two as children
      // and frequency equal to the sum of their frequencies
      internalFreq = left.frequency + right.frequency
      Create internal node with frequency internalFreq, left child left, right child right

      // Add this node to the min heap
      Add internal node to minHeap

    // The remaining node is the root of the Huffman tree
    root = Extract min from minHeap

    // Generate codes by traversing the tree
    Initialize codes as empty map
    GenerateHuffmanCodes(root, "", codes)

    RETURN codes
  ```

- Fractional Knapsack

  ```python
  ALGORITHM FractionalKnapsack(weights, values, capacity)
    """Solve the Fractional Knapsack problem using a greedy approach based on value/weight ratio."""
    // Create items as (value, weight, value/weight ratio)
    Initialize items as empty list
    FOR i FROM 0 TO length of weights - 1 DO
      ratio = values[i] / weights[i]
      Add (values[i], weights[i], ratio) to items

    // Sort items by value-to-weight ratio (descending)
    Sort items by ratio in descending order

    Initialize totalValue = 0
    Initialize currentWeight = 0

    FOR each item in items DO
      IF currentWeight + item.weight <= capacity THEN
        // Take the whole item
        Add item.weight to currentWeight
        Add item.value to totalValue
      ELSE
        // Take a fraction of the item
        remainingCapacity = capacity - currentWeight
        fraction = remainingCapacity / item.weight
        Add remainingCapacity to currentWeight
        Add fraction * item.value to totalValue
        BREAK  // Knapsack is full

    RETURN totalValue
  ```

- Interval Scheduling (Minimum Intervals to Remove)

  ```python
  ALGORITHM MinRemovalIntervals(intervals)
    """Find the minimum number of intervals to remove to make the rest non-overlapping."""
    IF intervals is empty THEN
      RETURN 0

    // Sort by end time
    Sort intervals by end time

    Initialize end = intervals[0].end
    Initialize count = 1  // Count of non-overlapping intervals

    FOR i FROM 1 TO length of intervals - 1 DO
      IF intervals[i].start >= end THEN
        // Current interval doesn't overlap with previous
        Set end = intervals[i].end
        Increment count

    // RETURN number of intervals to remove
    RETURN length of intervals - count
  ```

- Jump Game (can reach end)

  ```python
  ALGORITHM CanJump(nums)
    """Determine if the end of an array can be reached by jumping."""
    n = length of nums

    // Initialize the farthest position we can reach
    Initialize maxReach = 0

    FOR i FROM 0 TO n-1 DO
      // IF we can't reach the current position, RETURN false
      IF i > maxReach THEN
        RETURN false

      // Update the farthest position we can reach
      maxReach = MAX(maxReach, i + nums[i])

      // IF we can already reach the end, RETURN true
      IF maxReach >= n-1 THEN
        RETURN true

    RETURN false // Only reachable IF loop completes AND maxReach >= n-1
  ```

- Best Time to Buy and Sell Stock (Max Profit)

  ```python
  ALGORITHM MaxProfit(prices)
    """Find the maximum profit from buying and selling a stock once."""
    IF prices is empty THEN
      RETURN 0

    Set minPrice = prices[0]
    Set maxProfit = 0

    FOR i FROM 1 TO length(prices)-1 DO
      IF prices[i] < minPrice THEN
        Update minPrice = prices[i]
      ELSE
        Calculate currentProfit = prices[i] - minPrice
        Update maxProfit = MAX(maxProfit, currentProfit)

    RETURN maxProfit
  ```

