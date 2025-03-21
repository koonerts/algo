# Algorithm Patterns Speedrun Quiz (Prioritized)

This speedrun quiz tests your ability to quickly identify algorithm patterns and apply the correct techniques to solve problems. Questions are organized by return on investment (ROI) - starting with patterns that are easiest to learn and offer the highest return.

## Table of Contents

- [High ROI Patterns](#high-roi-patterns)
  - [Two Pointers](#two-pointers)
  - [Sliding Window](#sliding-window)
  - [Breadth-First Search](#breadth-first-search)
- [Medium ROI Patterns](#medium-roi-patterns)
  - [Depth-First Search](#depth-first-search)
  - [Backtracking](#backtracking)
  - [Binary Search](#binary-search)
  - [Heap](#heap)
  - [Binary Search Tree](#binary-search-tree)
  - [Fast & Slow Pointers](#fast--slow-pointers)
  - [Dynamic Programming](#dynamic-programming)
- [Low ROI Patterns](#low-roi-patterns)
  - [Divide and Conquer](#divide-and-conquer)
  - [Trie](#trie)
  - [Union Find](#union-find)
  - [Greedy Algorithms](#greedy-algorithms)
- [Additional Patterns](#additional-patterns)
  - [Matrix as Graph](#matrix-as-graph)
  - [Monotonic Stack](#monotonic-stack)
  - [Topological Sort](#topological-sort)
  - [Linked List Techniques](#linked-list-techniques)
  - [Prefix Sums](#prefix-sums)
  - [Bit Manipulation](#bit-manipulation)
  - [Advanced Graph Algorithms](#advanced-graph-algorithms)
  - [Advanced Data Structures](#advanced-data-structures)
  - [String Algorithms](#string-algorithms)
  - [Specialized Patterns](#specialized-patterns)

---

# High ROI Patterns

## Two Pointers

### 1. Two Pointers (Opposite Direction)

**You need to find if there's a pair of elements in a sorted array that sum to a target value.**

- [ ] A. Use a hash map to track seen values
- [ ] B. Use a sliding window with variable size
- [ ] C. Use two pointers starting from both ends of the array
- [ ] D. Use binary search on each element

<details>
<summary>View Answer</summary>

**C. Use two pointers starting from both ends of the array**

Since the array is sorted, we can use two pointers - one at the beginning and one at the end. If their sum is too large, we move the right pointer left; if too small, we move the left pointer right. This gives us O(n) time complexity.
</details>

---

### 2. Two Pointers (Same Direction)

**Find the longest subarray containing only 1's after flipping at most k 0's to 1's.**

- [ ] A. Use a dynamic programming approach with a 2D array
- [ ] B. Use a sliding window with two pointers tracking a valid segment
- [ ] C. Use binary search to find the optimal subarray length
- [ ] D. Use a greedy approach flipping the first k zeros

<details>
<summary>View Answer</summary>

**B. Use a sliding window with two pointers tracking a valid segment**

This is a classic sliding window problem with two pointers moving in the same direction. We maintain a window where we've flipped at most k zeros, expanding the right pointer and contracting the left pointer when necessary to maintain our constraint.
</details>

---

## Sliding Window

### 3. Sliding Window (Fixed Size)

**Find the maximum sum of any contiguous subarray of fixed size k in an array.**

- [ ] A. Sort the array and take the last k elements
- [ ] B. Use a queue to track elements in the current window
- [ ] C. Maintain a fixed-size sliding window, subtracting old values and adding new ones
- [ ] D. Create a prefix sum array and calculate differences

<details>
<summary>View Answer</summary>

**C. Maintain a fixed-size sliding window, subtracting old values and adding new ones**

With a fixed-size sliding window, we start by calculating the sum of the first k elements. Then, as we slide the window, we subtract the element leaving the window and add the element entering the window, keeping track of the maximum sum seen.
</details>

---

### 4. Sliding Window (Variable Size)

**Find the shortest subarray with a sum at least k.**

- [ ] A. Use binary search to find the minimum length
- [ ] B. Sort the array and use two pointers
- [ ] C. Use dynamic programming with an array of minimum lengths
- [ ] D. Use a sliding window that expands and contracts based on the current sum

<details>
<summary>View Answer</summary>

**D. Use a sliding window that expands and contracts based on the current sum**

We use a variable-size sliding window. We expand the window by moving the right pointer until the sum is at least k, then contract it by moving the left pointer while maintaining the sum ≥ k. At each valid window, we update the minimum length.
</details>

---

### 5. Sliding Window (Variable Size - Alternative)

**Find the length of the longest subarray with a sum less than or equal to a given value.**

- [ ] A. Use two pointers to define a window, expand until invalid, then contract
- [ ] B. Build a trie to store all possible subarrays
- [ ] C. Sort the array and use binary search
- [ ] D. Use Dijkstra's algorithm to find the shortest path

<details>
<summary>View Answer</summary>

**A. Use two pointers to define a window, expand until invalid, then contract**

This is a classic variable-size sliding window problem. We maintain a window using two pointers and a running sum. We expand the window by moving the right pointer until the sum exceeds our target, then contract by moving the left pointer until valid again, tracking the maximum valid window size.
</details>

---

## Breadth-First Search

### 6. Breadth-First Search (Trees)

**Find the level with the largest sum in a binary tree.**

- [ ] A. Use a recursive depth-first approach with a global maximum
- [ ] B. Use a level-order traversal with a queue, tracking level sums
- [ ] C. Convert the tree to a graph and use Dijkstra's algorithm
- [ ] D. Apply a dynamic programming approach with memoization

<details>
<summary>View Answer</summary>

**B. Use a level-order traversal with a queue, tracking level sums**

BFS is perfect for level-order traversal. We use a queue to process nodes level by level, calculating the sum at each level and tracking the maximum sum level.
</details>

---

### 7. Breadth-First Search (Trees - Width)

**Find the maximum width of a binary tree (maximum number of nodes at any level).**

- [ ] A. Use preorder traversal with level tracking
- [ ] B. Use level-order traversal (BFS) with node counting per level
- [ ] C. Calculate width recursively using the height
- [ ] D. Convert the tree to an array representation

<details>
<summary>View Answer</summary>

**B. Use level-order traversal (BFS) with node counting per level**

BFS is naturally level-by-level. We use a queue to process nodes level by level, keeping track of the number of nodes at each level. The maximum of these counts is the tree's width.
</details>

---

### 8. Breadth-First Search (Graphs)

**Find the shortest path between two nodes in an unweighted graph.**

- [ ] A. Use depth-first search with backtracking
- [ ] B. Apply Dijkstra's algorithm with priority queue
- [ ] C. Use breadth-first search with a queue and visited set
- [ ] D. Use Union-Find to determine connectivity

<details>
<summary>View Answer</summary>

**C. Use breadth-first search with a queue and visited set**

For unweighted graphs, BFS naturally finds the shortest path by processing nodes in order of their distance from the start node. We use a queue and a visited set to avoid cycles.
</details>

---

### 9. Breadth-First Search (Grid Graphs)

**Find the shortest path from start to end in a grid where some cells are blocked.**

- [ ] A. Use DFS with a visited set to find all possible paths
- [ ] B. Use BFS to explore cells level by level until reaching the end
- [ ] C. Use Dijkstra's algorithm with a modified heuristic
- [ ] D. Use A* search with Manhattan distance

<details>
<summary>View Answer</summary>

**B. Use BFS to explore cells level by level until reaching the end**

For unweighted graphs (where each step has the same cost), BFS naturally finds the shortest path by exploring nodes in order of their distance from the start. We use a queue and a visited set to avoid revisiting cells.
</details>

---

# Medium ROI Patterns

## Depth-First Search

### 10. Depth-First Search (Trees)

**Check if a binary tree is a valid binary search tree.**

- [ ] A. Do an inorder traversal and verify if the result is sorted
- [ ] B. Calculate the sum of all node values
- [ ] C. Use level-order traversal with constraints checking
- [ ] D. Apply the Union-Find algorithm to detect cycles

<details>
<summary>View Answer</summary>

**A. Do an inorder traversal and verify if the result is sorted**

This is one approach. Alternatively, we can use DFS with min/max constraints, where each node's value must be within a range determined by its ancestors. For a BST, inorder traversal produces elements in sorted order.
</details>

---

### 11. Depth-First Search (Trees - Balance)

**Check if a binary tree is balanced (the depth of any two leaf nodes differs by at most 1).**

- [ ] A. Compare the depths of every pair of leaf nodes
- [ ] B. Use BFS to check if the tree is complete
- [ ] C. Use bottom-up DFS to calculate heights and check balance
- [ ] D. Count nodes at each level and verify even distribution

<details>
<summary>View Answer</summary>

**C. Use bottom-up DFS to calculate heights and check balance**

Use post-order traversal (a type of DFS) to compute heights bottom-up. For each node, calculate the height of left and right subtrees. If their difference exceeds 1, the tree is unbalanced. This way, we can check balance in a single pass.
</details>

---

### 12. Depth-First Search (Graphs)

**Determine if there's a path between two nodes in a directed graph.**

- [ ] A. Use BFS with a queue starting from the source node
- [ ] B. Use DFS with recursion or a stack from the source node
- [ ] C. Use Union-Find to check if nodes are connected
- [ ] D. Calculate the transitive closure of the graph

<details>
<summary>View Answer</summary>

**B. Use DFS with recursion or a stack from the source node**

DFS can be used to check if there's a path from source to destination. We recursively explore all paths from the source, marking nodes as visited, until we either find the destination or exhaust all possibilities.
</details>

---

### 13. Depth-First Search (Cycle Detection)

**Detect if a directed graph has a cycle.**

- [ ] A. Use a union-find data structure
- [ ] B. Apply BFS and count nodes at each level
- [ ] C. Use DFS with three node states: unvisited, in-progress, and visited
- [ ] D. Sort the adjacency list and check for repeated edges

<details>
<summary>View Answer</summary>

**C. Use DFS with three node states: unvisited, in-progress, and visited**

To detect cycles in a directed graph using DFS, we maintain three states for nodes: unvisited, in-progress (in the current DFS path), and visited (finished processing). If we encounter an in-progress node during DFS, we've found a cycle.
</details>

---

## Backtracking

### 14. Backtracking (Basic)

**Generate all possible combinations of k numbers from 1 to n.**

- [ ] A. Use dynamic programming with a 2D table
- [ ] B. Apply BFS with branching at each level
- [ ] C. Use recursion with backtracking, adding and removing elements
- [ ] D. Build a mathematical formula to calculate all combinations

<details>
<summary>View Answer</summary>

**C. Use recursion with backtracking, adding and removing elements**

Backtracking is perfect for generating all combinations. We recursively build combinations by adding one element at a time, exploring all possibilities, and backtracking by removing the last element before trying the next option.
</details>

---

### 15. Backtracking (Subsets)

**Generate all possible subsets of a set of distinct integers.**

- [ ] A. Use bit manipulation to represent all subsets
- [ ] B. Use a mathematical formula for combinations
- [ ] C. Use recursion with backtracking, including/excluding each element
- [ ] D. Implement a breadth-first approach generating subsets level by level

<details>
<summary>View Answer</summary>

**C. Use recursion with backtracking, including/excluding each element**

Classic backtracking approach: for each element, we have two choices - include it in the current subset or exclude it. We recursively explore both options for each element, building subsets incrementally.
</details>

---

### 16. Backtracking (Permutations)

**Generate all permutations of a string with distinct characters.**

- [ ] A. Use mathematical formulas to generate permutations directly
- [ ] B. Use recursion with swapping characters at each position
- [ ] C. Generate all subsets first, then arrange each subset
- [ ] D. Use a queue to iteratively build permutations level by level

<details>
<summary>View Answer</summary>

**B. Use recursion with swapping characters at each position**

For each position, we try all possible characters that can be placed there (by swapping with the current character). Then we recursively generate all permutations for the remaining positions. After the recursive call, we backtrack by swapping back.
</details>

---

### 17. Backtracking (Constraint Satisfaction)

**Solve a Sudoku puzzle.**

- [ ] A. Use a greedy algorithm to fill in obvious cells first
- [ ] B. Apply backtracking with constraint checking for each cell
- [ ] C. Convert to a graph coloring problem and use BFS
- [ ] D. Use dynamic programming with a state table

<details>
<summary>View Answer</summary>

**B. Apply backtracking with constraint checking for each cell**

For each empty cell, we try all valid digits (1-9) that don't violate Sudoku constraints (row, column, and 3x3 box). After placing a digit, we recursively try to solve the rest of the puzzle. If we reach a dead end, we backtrack and try a different digit.
</details>

---

### 18. Backtracking (N-Queens)

**Count the number of ways to arrange n queens on an n×n chessboard so that no two queens threaten each other.**

- [ ] A. Use a greedy algorithm to place queens optimally
- [ ] B. Apply dynamic programming with state tables
- [ ] C. Use backtracking with constraint checking and counting valid arrangements
- [ ] D. Calculate mathematically using combinatorics

<details>
<summary>View Answer</summary>

**C. Use backtracking with constraint checking and counting valid arrangements**

The N-Queens problem is a classic backtracking problem. We place queens one row at a time, checking if each position is valid (not threatened by previously placed queens). We backtrack when necessary and count all valid arrangements.
</details>

---

## Binary Search

### 19. Binary Search (Basic)

**Find a specific value in a sorted array.**

- [ ] A. Use sequential search from the beginning
- [ ] B. Use binary search, repeatedly dividing the search space in half
- [ ] C. Use interpolation search based on values distribution
- [ ] D. Use exponential search followed by binary search

<details>
<summary>View Answer</summary>

**B. Use binary search, repeatedly dividing the search space in half**

Binary search compares the target value to the middle element of the array. If they are unequal, the half in which the target cannot lie is eliminated, and the search continues on the remaining half until the target is found or the subarray size becomes zero.
</details>

---

### 20. Binary Search (Boundary)

**Find the index of the first occurrence of a value in a sorted array with duplicates.**

- [ ] A. Use linear search from the beginning until finding the value
- [ ] B. Use binary search to find any occurrence, then scan left
- [ ] C. Use binary search but continue leftward even after finding a match
- [ ] D. Sort the array indices by value and find the smallest index

<details>
<summary>View Answer</summary>

**C. Use binary search but continue leftward even after finding a match**

Standard binary search finds any occurrence. To find the first occurrence, when we find a match, we don't stop but instead continue searching in the left half (by setting right = mid - 1). We also remember this position as a potential answer.
</details>

---

### 21. Binary Search (Rotated Array)

**Find a value in a sorted array that was rotated at an unknown pivot point.**

- [ ] A. First find the pivot, then perform binary search on the appropriate half
- [ ] B. Modified binary search that handles the rotation internally
- [ ] C. Search both halves of the array using regular binary search
- [ ] D. Convert to a normal sorted array first, then use standard binary search

<details>
<summary>View Answer</summary>

**B. Modified binary search that handles the rotation internally**

We use a modified binary search. At each step, we determine which half of the array is sorted. If the target is in the range of the sorted half, we search there; otherwise, we search the other half. This preserves the O(log n) time complexity.
</details>

---

### 22. Binary Search (On Answer)

**Find the minimum capacity of ships needed to transport packages within a given number of days.**

- [ ] A. Use dynamic programming to find optimal distribution
- [ ] B. Use a greedy approach assigning packages sequentially
- [ ] C. Binary search on the potential capacity values
- [ ] D. Sort packages and assign to ships using two pointers

<details>
<summary>View Answer</summary>

**C. Binary search on the potential capacity values**

Instead of searching for a value in an array, we binary search on the potential answer space (possible capacity values). For each capacity, we check if it's feasible (can ship all packages within the day limit). The minimum feasible capacity is our answer.
</details>

---

### 23. Binary Search (First Bad Version)

**Find the first bad version in a series of versions where all versions after a bad one are also bad.**

- [ ] A. Check versions sequentially from the beginning
- [ ] B. Use binary search to find the first bad version
- [ ] C. Apply two-pointer technique from both ends
- [ ] D. Use a breadth-first search starting from the middle version

<details>
<summary>View Answer</summary>

**B. Use binary search to find the first bad version**

This is a classic binary search problem for finding the boundary between good and bad versions. We search for the first occurrence where isBadVersion(version) returns true.
</details>

---

## Heap

### 24. Heap (Top K Elements)

**Find the k largest elements in an array.**

- [ ] A. Sort the array and return the last k elements
- [ ] B. Use quickselect algorithm to find the kth largest element
- [ ] C. Maintain a min-heap of size k while processing the array
- [ ] D. Use two pointers to partition the array around k

<details>
<summary>View Answer</summary>

**C. Maintain a min-heap of size k while processing the array**

To find the k largest elements, we can maintain a min-heap of size k. For each element, we add it to the heap and remove the smallest element if the heap size exceeds k. This gives us O(n log k) time complexity.
</details>

---

### 25. Heap (Two Heaps)

**Find the median of a data stream.**

- [ ] A. Sort the stream after each addition
- [ ] B. Maintain a balanced binary search tree
- [ ] C. Use two heaps: a max-heap for the smaller half and a min-heap for the larger half
- [ ] D. Track the sum and count to calculate average

<details>
<summary>View Answer</summary>

**C. Use two heaps: a max-heap for the smaller half and a min-heap for the larger half**

We maintain two heaps: a max-heap for the smaller half of the numbers and a min-heap for the larger half. We balance the heaps so their sizes differ by at most 1, allowing us to find the median in O(1) time after insertion.
</details>

---

## Binary Search Tree

### 26. Binary Search Tree (Traversal)

**Find the kth smallest element in a binary search tree.**

- [ ] A. Do an inorder traversal and return the kth element
- [ ] B. Use a min-heap to track the k smallest elements
- [ ] C. Apply Morris traversal for constant space
- [ ] D. Convert the BST to a sorted array and return the kth element

<details>
<summary>View Answer</summary>

**A. Do an inorder traversal and return the kth element**

Since inorder traversal of a BST visits nodes in ascending order, we can simply perform an inorder traversal and return the kth element visited.
</details>

---

## Fast & Slow Pointers

### 27. Fast & Slow Pointers (Cycle Detection)

**Detect if a linked list has a cycle.**

- [ ] A. Use a hash set to track visited nodes
- [ ] B. Use fast and slow pointers to detect a cycle
- [ ] C. Count the number of nodes and check if it exceeds the expected length
- [ ] D. Use a stack to track the traversal path

<details>
<summary>View Answer</summary>

**B. Use fast and slow pointers to detect a cycle**

The Floyd's Cycle-Finding Algorithm (tortoise and hare) uses two pointers moving at different speeds. If there's a cycle, the fast pointer will eventually catch up to the slow pointer.
</details>

---

### 28. Fast & Slow Pointers (Middle Finding)

**Find the middle node of a linked list in a single pass.**

- [ ] A. First count the nodes, then traverse to the middle
- [ ] B. Use recursion to find the depth and middle node simultaneously 
- [ ] C. Use a slow pointer and a fast pointer that moves twice as fast
- [ ] D. Use a stack to store nodes and find the middle

<details>
<summary>View Answer</summary>

**C. Use a slow pointer and a fast pointer that moves twice as fast**

When the fast pointer reaches the end of the list, the slow pointer will be at the middle. The fast pointer moves two steps for every one step of the slow pointer. When the fast pointer reaches the end (or null), the slow pointer will be at the middle.
</details>

---

## Dynamic Programming

### 29. Dynamic Programming (Kadane's Algorithm)

**Find the maximum sum of a contiguous subarray in an array of integers.**

- [ ] A. Sort the array and take the largest elements
- [ ] B. Use dynamic programming to track maximum subarray ending at each position
- [ ] C. Apply two pointers to track the subarray boundaries
- [ ] D. Calculate the prefix sum and find the maximum difference

<details>
<summary>View Answer</summary>

**B. Use dynamic programming to track maximum subarray ending at each position**

Kadane's algorithm is a dynamic programming approach that maintains two variables: the maximum subarray sum ending at the current position, and the global maximum subarray sum. We iterate through the array once, updating these values.
</details>

---

### 30. Dynamic Programming (0/1 Knapsack)

**Given weights and values of n items, put them in a knapsack of capacity W to get the maximum value.**

- [ ] A. Use a greedy approach by selecting items with the highest value/weight ratio
- [ ] B. Apply BFS to explore all possible combinations
- [ ] C. Use dynamic programming with a 2D table to track optimal values
- [ ] D. Sort items by value and add them until capacity is reached

<details>
<summary>View Answer</summary>

**C. Use dynamic programming with a 2D table to track optimal values**

The 0/1 Knapsack problem is solved using dynamic programming. We create a 2D table where dp[i][w] represents the maximum value achievable with the first i items and weight limit w.
</details>

---

### 31. Dynamic Programming (Unbounded Knapsack)

**Given coins of different denominations and a total amount, find the minimum number of coins needed to make up that amount.**

- [ ] A. Sort the coins and use a greedy approach
- [ ] B. Use BFS to find the shortest path to the target amount
- [ ] C. Apply DFS with memoization to explore all combinations
- [ ] D. Use dynamic programming with a 1D array to track minimum coins

<details>
<summary>View Answer</summary>

**D. Use dynamic programming with a 1D array to track minimum coins**

The Coin Change problem is an unbounded knapsack problem. We use a 1D DP array where dp[i] represents the minimum number of coins needed to make amount i. For each coin, we update dp[i] = min(dp[i], dp[i - coin] + 1).
</details>

---

### 32. Dynamic Programming (Longest Common Subsequence)

**Find the length of the longest common subsequence between two strings.**

- [ ] A. Use a sliding window to compare substrings
- [ ] B. Apply a hash map to count common characters
- [ ] C. Use dynamic programming with a 2D table to build the LCS
- [ ] D. Convert both strings to character frequency arrays and compare

<details>
<summary>View Answer</summary>

**C. Use dynamic programming with a 2D table to build the LCS**

The Longest Common Subsequence problem uses a 2D DP table where dp[i][j] represents the length of the LCS of the first i characters of string 1 and the first j characters of string 2.
</details>

---

### 33. Dynamic Programming (Fibonacci Pattern)

**Count the number of ways to reach the nth stair when you can climb 1 or 2 stairs at a time.**

- [ ] A. Use recursion to try all combinations
- [ ] B. Apply BFS to find all possible paths
- [ ] C. Use dynamic programming with Fibonacci pattern
- [ ] D. Apply combinatorial formula directly

<details>
<summary>View Answer</summary>

**C. Use dynamic programming with Fibonacci pattern**

This is the classic climbing stairs problem, which follows the Fibonacci pattern. The number of ways to reach the nth stair is the sum of the ways to reach the (n-1)th and (n-2)th stairs.
</details>

---

# Low ROI Patterns

## Divide and Conquer

### 34. Divide and Conquer

**Given n items with values and weights, determine the maximum value you can put in a knapsack of capacity W.**

- [ ] A. Use a greedy approach taking items with highest value/weight ratio
- [ ] B. Try all possible combinations using backtracking
- [ ] C. Use dynamic programming with a 2D table of items vs. capacity
- [ ] D. Sort items by value and take until capacity is reached

<details>
<summary>View Answer</summary>

**C. Use dynamic programming with a 2D table of items vs. capacity**

The 0/1 Knapsack problem is solved with a 2D DP table where dp[i][w] = maximum value achievable with first i items and weight limit w. For each item, we have two choices: include it if there's capacity, or exclude it. We take the maximum of these two options.
</details>

---

## Trie

### 35. Trie (Prefix Tree)

**Implement an autocomplete system that suggests words based on a prefix.**

- [ ] A. Use a hash map to store all possible prefixes
- [ ] B. Apply binary search on a sorted list of words
- [ ] C. Build a trie data structure for efficient prefix matching
- [ ] D. Use a bloom filter to check if prefixes exist

<details>
<summary>View Answer</summary>

**C. Build a trie data structure for efficient prefix matching**

A trie is designed for prefix operations. We can navigate to the node corresponding to the prefix and then traverse all paths from that node to get all words with that prefix.
</details>

---

### 36. Trie (Advanced Usage)

**Design a data structure for efficiently searching words by prefix.**

- [ ] A. Use a hash map with all possible prefixes as keys
- [ ] B. Implement a trie (prefix tree) with character nodes
- [ ] C. Use a sorted array of strings with binary search
- [ ] D. Implement a balanced binary search tree of strings

<details>
<summary>View Answer</summary>

**B. Implement a trie (prefix tree) with character nodes**

A trie is optimized for prefix operations. Each node represents a character and has links to child nodes for subsequent characters. To check if a prefix exists, we navigate the trie character by character. If we can follow the entire prefix, it exists in our dictionary.
</details>

---

## Union Find

### 37. Union Find (Basics)

**Given a list of edges, determine if they form a valid tree (connected graph without cycles).**

- [ ] A. Use DFS to detect cycles in the graph
- [ ] B. Apply BFS to check connectivity
- [ ] C. Use Union-Find to merge connected components and detect cycles
- [ ] D. Sort the edges by weight and use a greedy algorithm

<details>
<summary>View Answer</summary>

**C. Use Union-Find to merge connected components and detect cycles**

Union-Find is perfect for this problem. We process each edge, unioning the sets of the connected nodes. If we attempt to union nodes already in the same set, we've found a cycle. A valid tree has n-1 edges and no cycles.
</details>

---

### 38. Union Find (Component Counting)

**Determine the number of connected components in an undirected graph.**

- [ ] A. Use depth-first search to count connected components
- [ ] B. Use breadth-first search from each unvisited node
- [ ] C. Use Union-Find to merge connected nodes and count sets
- [ ] D. Convert to an adjacency matrix and analyze connectivity

<details>
<summary>View Answer</summary>

**C. Use Union-Find to merge connected nodes and count sets**

Union-Find efficiently tracks disjoint sets. For each edge (u,v), we union the sets containing u and v. After processing all edges, the number of disjoint sets equals the number of connected components.
</details>

---

## Greedy Algorithms

### 39. Greedy Algorithms (Activity Selection)

**Given a set of activities with start and end times, find the maximum number of activities that can be performed by a single person.**

- [ ] A. Sort activities by their duration and select the shortest ones
- [ ] B. Sort activities by start time and select non-overlapping ones
- [ ] C. Sort activities by end time and select non-overlapping ones
- [ ] D. Use dynamic programming to explore all possible combinations

<details>
<summary>View Answer</summary>

**C. Sort activities by end time and select non-overlapping ones**

This is the Activity Selection problem. The greedy approach is to sort activities by their end times and select activities that don't overlap with the previously selected activity.
</details>

---

### 40. Greedy Algorithms (Interval Scheduling)

**Determine the minimum number of intervals to remove to make all remaining intervals non-overlapping.**

- [ ] A. Remove intervals with the longest duration first
- [ ] B. Sort by start time and use dynamic programming
- [ ] C. Sort by end time and greedily select compatible intervals
- [ ] D. Use Union-Find to merge overlapping intervals

<details>
<summary>View Answer</summary>

**C. Sort by end time and greedily select compatible intervals**

We sort intervals by end time and greedily select intervals that don't overlap with the previously selected interval. The number of intervals we can't select is the minimum number to remove. This works because selecting the interval that ends earliest maximizes flexibility for future selections.
</details>

---

# Additional Patterns

## Matrix as Graph

### 41. Matrix as Graph (Island Counting)

**Find the number of distinct islands in a 2D grid, where an island is a group of connected 1's.**

- [ ] A. Use dynamic programming to count islands
- [ ] B. Apply DFS or BFS from each unvisited '1' cell, marking visited cells
- [ ] C. Use a union-find data structure to merge connected components
- [ ] D. Apply Dijkstra's algorithm to find shortest paths between islands

<details>
<summary>View Answer</summary>

**B. Apply DFS or BFS from each unvisited '1' cell, marking visited cells**

We can treat the matrix as a graph where adjacent cells are connected. For each unvisited '1' cell, we perform DFS or BFS to explore and mark the entire island as visited, incrementing our count for each new island we discover.
</details>

---

## Monotonic Stack

### 42. Monotonic Stack

**Find the next greater element for each element in an array.**

- [ ] A. Use a doubly linked list to store elements
- [ ] B. Sort the array and binary search for each element
- [ ] C. Use a stack to keep track of elements waiting for their next greater element
- [ ] D. Apply a heap to track maximum elements

<details>
<summary>View Answer</summary>

**C. Use a stack to keep track of elements waiting for their next greater element**

A monotonic stack is perfect for this problem. We maintain a stack of elements waiting for their next greater element. When we encounter a greater element, we pop from the stack and update their results.
</details>

---

## Topological Sort

### 43. Topological Sort

**Given a list of tasks with dependencies, find a valid order to complete all tasks.**

- [ ] A. Sort the tasks by their number of dependencies
- [ ] B. Use DFS to explore the dependency graph and detect cycles
- [ ] C. Apply BFS with indegree tracking to build the topological order
- [ ] D. Use a union-find data structure to merge related tasks

<details>
<summary>View Answer</summary>

**C. Apply BFS with indegree tracking to build the topological order**

Topological sorting can be implemented using BFS with indegree tracking. We start with nodes that have no dependencies (indegree=0), remove them, update the indegrees of their neighbors, and continue until all nodes are processed or we detect a cycle.
</details>

---

## Linked List Techniques

### 44. Linked List Reversal

**Reverse a linked list.**

- [ ] A. Use a stack to store nodes and rebuild in reverse order
- [ ] B. Maintain three pointers (prev, current, next) and reverse links
- [ ] C. Use a queue to reorder nodes
- [ ] D. Create a new list in reverse order

<details>
<summary>View Answer</summary>

**B. Maintain three pointers (prev, current, next) and reverse links**

The iterative approach to reversing a linked list involves maintaining three pointers: prev, current, and next. We traverse the list once, reversing the next pointer of each node to point to the previous node.
</details>

---

### 45. Linked List Reversal (Advanced)

**Reverse nodes in a linked list in groups of k.**

- [ ] A. Use recursion to reverse each group and connect them
- [ ] B. Create k separate lists and then merge them
- [ ] C. Use a stack to reverse every k elements
- [ ] D. Count nodes first, then reverse only complete groups

<details>
<summary>View Answer</summary>

**A. Use recursion to reverse each group and connect them**

We recursively reverse the first k nodes using the same technique as reversing a whole linked list. Then, we connect the reversed part with the recursively processed rest of the list (which will have its own k-groups reversed).
</details>

---

## Prefix Sums

### 46. Prefix Sums (Subarray Sum)

**Find the number of subarrays with a sum equal to a given target.**

- [ ] A. Use a sliding window with variable size
- [ ] B. Apply two pointers to track subarray boundaries
- [ ] C. Use a hash map to store prefix sums and their frequencies
- [ ] D. Sort the array and use binary search

<details>
<summary>View Answer</summary>

**C. Use a hash map to store prefix sums and their frequencies**

We calculate the prefix sum while iterating through the array. For each position, we check if (prefix_sum - target) exists in our hash map, which would indicate a subarray with the target sum ending at the current position.
</details>

---

## Bit Manipulation

### 47. Bit Manipulation (XOR Technique)

**Find the single number in an array where every other number appears twice.**

- [ ] A. Sort the array and check adjacent elements
- [ ] B. Use a hash map to count occurrences
- [ ] C. Apply XOR to all elements in the array
- [ ] D. Use a binary search tree to track unique elements

<details>
<summary>View Answer</summary>

**C. Apply XOR to all elements in the array**

This is a classic bit manipulation problem. XORing a number with itself results in 0, and XORing with 0 leaves the number unchanged. By XORing all elements, the duplicates cancel out, leaving only the single number.
</details>

---

### 48. Bit Manipulation (Advanced)

**Find the only element that appears once in an array where all other elements appear exactly three times.**

- [ ] A. Sort the array and check adjacent elements
- [ ] B. Use a hash map to count occurrences
- [ ] C. Use bit manipulation to count bits modulo 3
- [ ] D. Use a mathematical formula with sums

<details>
<summary>View Answer</summary>

**C. Use bit manipulation to count bits modulo 3**

We count the number of 1s at each bit position for all numbers. Since each bit of a number that appears three times contributes either 0 or 3 to the count, the bits from the unique number will make the count not divisible by 3. We construct our answer from these bits.
</details>

---

## Advanced Graph Algorithms

### 49. Graph Algorithms (Dijkstra)

**Find the shortest path from a source node to all other nodes in a weighted graph with non-negative edges.**

- [ ] A. Use BFS to explore nodes level by level
- [ ] B. Apply DFS with a visited set
- [ ] C. Use Dijkstra's algorithm with a priority queue
- [ ] D. Apply the Bellman-Ford algorithm for shortest paths

<details>
<summary>View Answer</summary>

**C. Use Dijkstra's algorithm with a priority queue**

Dijkstra's algorithm is designed for this exact problem. It uses a priority queue to always process the node with the smallest current distance, guaranteeing the shortest path to each node.
</details>

---

### 50. Graph Coloring

**Determine if a graph can be colored with at most 2 colors such that no adjacent vertices have the same color.**

- [ ] A. Use a greedy algorithm to assign colors
- [ ] B. Apply BFS/DFS to color vertices and check for conflicts
- [ ] C. Use Union-Find to detect odd-length cycles
- [ ] D. Sort vertices by degree and color in order

<details>
<summary>View Answer</summary>

**B. Apply BFS/DFS to color vertices and check for conflicts**

This is a bipartite graph check. We use BFS or DFS to color the graph with 2 colors, alternating colors for adjacent vertices. If at any point we can't assign a different color to an adjacent vertex, the graph is not bipartite.
</details>

---

## Advanced Data Structures

### 51. Design Problems (LRU Cache)

**Implement a data structure for an LRU (Least Recently Used) cache.**

- [ ] A. Use a simple array with linear search for access
- [ ] B. Implement with a balanced binary search tree
- [ ] C. Use a hash map combined with a doubly linked list
- [ ] D. Use a priority queue based on access timestamps

<details>
<summary>View Answer</summary>

**C. Use a hash map combined with a doubly linked list**

An efficient LRU cache combines a hash map for O(1) lookups with a doubly linked list to maintain order of use. When an item is accessed, it's moved to the front of the list (most recently used). When capacity is reached, we remove the item at the end of the list (least recently used).
</details>

---

### 52. Advanced Data Structures (Segment Tree)

**Which data structure would be most efficient for range queries and updates on an array?**

- [ ] A. Binary search tree
- [ ] B. Hash table
- [ ] C. Segment tree
- [ ] D. Linked list

<details>
<summary>View Answer</summary>

**C. Segment tree**

A segment tree is specialized for range queries and updates. It's a binary tree where each node represents a range of the array. Leaf nodes represent individual elements, and internal nodes represent the combined result (sum, min, max, etc.) of their children. This allows for O(log n) range queries and updates.
</details>

---

## String Algorithms

### 53. String Algorithms (KMP)

**Find all occurrences of a pattern string in a text string efficiently.**

- [ ] A. Use naive approach checking all possible positions
- [ ] B. Apply the Knuth-Morris-Pratt (KMP) algorithm using partial matches
- [ ] C. Use the Boyer-Moore algorithm with bad character and good suffix rules
- [ ] D. Apply a rolling hash (Rabin-Karp) algorithm

<details>
<summary>View Answer</summary>

**B. Apply the Knuth-Morris-Pratt (KMP) algorithm using partial matches**

KMP avoids unnecessary comparisons by using information from previous matches. It preprocesses the pattern to create a "partial match" table, which indicates how much of the pattern can be skipped when a mismatch occurs. This reduces the time complexity to O(n+m) where n and m are the lengths of text and pattern.
</details>

---

### 54. String Matching (Approximate)

**Find strings that approximately match a pattern allowing for k errors (edit distance).**

- [ ] A. Use dynamic programming to calculate edit distance for all substrings
- [ ] B. Apply the Rabin-Karp algorithm with hash comparisons
- [ ] C. Use a modified KMP algorithm with allowed errors
- [ ] D. Implement a bit-parallel algorithm like Bitap

<details>
<summary>View Answer</summary>

**D. Implement a bit-parallel algorithm like Bitap**

The Bitap algorithm (also known as Shift-OR or Baeza-Yates-Gonnet algorithm) uses bit manipulation for approximate string matching. It can be modified to handle up to k errors by maintaining k+1 bit arrays. This approach is particularly efficient for patterns shorter than the word size.
</details>

---

## Specialized Patterns

### 55. Combinatorial Search

**Generate all possible valid combinations of n pairs of parentheses.**

- [ ] A. Use dynamic programming to build up valid strings
- [ ] B. Apply backtracking ensuring valid balance of parentheses
- [ ] C. Use BFS to build strings level by level
- [ ] D. Create a mathematical formula for Catalan numbers and generate directly

<details>
<summary>View Answer</summary>

**B. Apply backtracking ensuring valid balance of parentheses**

We use backtracking with two rules: we can add an opening parenthesis if we haven't used all n, and we can add a closing parenthesis if there are unclosed opening parentheses. This ensures all generated combinations are valid.
</details>

---

### 56. System Design Patterns (Rate Limiter)

**Implement a rate limiter that allows n requests per minute per user.**

- [ ] A. Use a simple counter reset every minute
- [ ] B. Implement a token bucket algorithm
- [ ] C. Use a sliding window with timestamps for each request
- [ ] D. Apply a leaky bucket algorithm that processes requests at a fixed rate

<details>
<summary>View Answer</summary>

**C. Use a sliding window with timestamps for each request**

A sliding window approach keeps track of timestamps of requests in the last minute. For each new request, we clean out timestamps older than 1 minute and check if the remaining count is less than the limit. This ensures exactly n requests per minute regardless of distribution within the minute.
</details>

---

### 57. Memory Management (Garbage Collection)

**Which algorithm marks objects for garbage collection by starting from root objects and marking everything reachable?**

- [ ] A. Reference counting
- [ ] B. Mark and sweep
- [ ] C. Generational garbage collection
- [ ] D. Compaction

<details>
<summary>View Answer</summary>

**B. Mark and sweep**

Mark and Sweep is a garbage collection algorithm that works in two phases: 1) Mark: start from root objects and recursively mark all reachable objects as "in use" 2) Sweep: scan the entire memory and free any objects not marked as "in use". This identifies and collects all unreachable objects.
</details>

---

### 58. Concurrency Patterns (Reader-Writer Lock)

**Implement a mechanism that allows multiple readers but only one writer to access a resource simultaneously.**

- [ ] A. Use a simple mutex that locks for both readers and writers
- [ ] B. Implement a semaphore with initial value of maximum readers
- [ ] C. Use a reader-writer lock with reader count and writer flag
- [ ] D. Apply the actor model with message passing

<details>
<summary>View Answer</summary>

**C. Use a reader-writer lock with reader count and writer flag**

A reader-writer lock allows multiple readers to access the resource simultaneously, but grants exclusive access to writers. It typically uses a mutex to protect a reader count and a writer flag. Readers increment/decrement the count, while writers check for zero readers and set the writer flag.
</details>

---

### 59. Network Flow (Max Flow)

**Find the maximum flow in a flow network from source to sink.**

- [ ] A. Use Dijkstra's algorithm to find the path with maximum capacity
- [ ] B. Apply the Ford-Fulkerson algorithm with augmenting paths
- [ ] C. Use a greedy approach selecting highest capacity edges
- [ ] D. Implement Kruskal's algorithm on flow capacities

<details>
<summary>View Answer</summary>

**B. Apply the Ford-Fulkerson algorithm with augmenting paths**

The Ford-Fulkerson algorithm finds maximum flow by repeatedly finding augmenting paths (paths with available capacity) from source to sink and sending flow through them. We continue until no augmenting path exists. The Edmonds-Karp variant uses BFS to find the shortest augmenting path each time.
</details>

---

### 60. Specialized Trees (B-Tree)

**Which tree structure is commonly used in databases and file systems for efficient disk access?**

- [ ] A. Binary search tree
- [ ] B. Red-black tree
- [ ] C. AVL tree
- [ ] D. B-tree or B+ tree

<details>
<summary>View Answer</summary>

**D. B-tree or B+ tree**

B-trees and B+ trees are optimized for systems that read and write large blocks of data, like databases and file systems. They have a high branching factor, keeping the tree height small which minimizes disk accesses. B+ trees additionally link the leaves, making range queries more efficient.
</details>