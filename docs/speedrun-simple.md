# Algorithm Patterns Speedrun Quiz (Prioritized)

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

[View Answer](speedrun-answers.md#q1)

---

### 2. Two Pointers (Same Direction)

**Find the longest subarray containing only 1's after flipping at most k 0's to 1's.**

- [ ] A. Use a dynamic programming approach with a 2D array
- [ ] B. Use a sliding window with two pointers tracking a valid segment
- [ ] C. Use binary search to find the optimal subarray length
- [ ] D. Use a greedy approach flipping the first k zeros

[View Answer](speedrun-answers.md#q2)

---

## Sliding Window

### 3. Sliding Window (Fixed Size)

**Find the maximum sum of any contiguous subarray of fixed size k in an array.**

- [ ] A. Sort the array and take the last k elements
- [ ] B. Use a queue to track elements in the current window
- [ ] C. Maintain a fixed-size sliding window, subtracting old values and adding new ones
- [ ] D. Create a prefix sum array and calculate differences

[View Answer](speedrun-answers.md#q3)

---

### 4. Sliding Window (Variable Size)

**Find the shortest subarray with a sum at least k.**

- [ ] A. Use binary search to find the minimum length
- [ ] B. Sort the array and use two pointers
- [ ] C. Use dynamic programming with an array of minimum lengths
- [ ] D. Use a sliding window that expands and contracts based on the current sum

[View Answer](speedrun-answers.md#q4)

---

### 5. Sliding Window (Variable Size - Alternative)

**Find the length of the longest subarray with a sum less than or equal to a given value.**

- [ ] A. Use two pointers to define a window, expand until invalid, then contract
- [ ] B. Build a trie to store all possible subarrays
- [ ] C. Sort the array and use binary search
- [ ] D. Use Dijkstra's algorithm to find the shortest path

[View Answer](speedrun-answers.md#q5)

---

## Breadth-First Search

### 6. Breadth-First Search (Trees)

**Find the level with the largest sum in a binary tree.**

- [ ] A. Use a recursive depth-first approach with a global maximum
- [ ] B. Use a level-order traversal with a queue, tracking level sums
- [ ] C. Convert the tree to a graph and use Dijkstra's algorithm
- [ ] D. Apply a dynamic programming approach with memoization

[View Answer](speedrun-answers.md#q6)

---

### 7. Breadth-First Search (Trees - Width)

**Find the maximum width of a binary tree (maximum number of nodes at any level).**

- [ ] A. Use preorder traversal with level tracking
- [ ] B. Use level-order traversal (BFS) with node counting per level
- [ ] C. Calculate width recursively using the height
- [ ] D. Convert the tree to an array representation

[View Answer](speedrun-answers.md#q7)

---

### 8. Breadth-First Search (Graphs)

**Find the shortest path between two nodes in an unweighted graph.**

- [ ] A. Use depth-first search with backtracking
- [ ] B. Apply Dijkstra's algorithm with priority queue
- [ ] C. Use breadth-first search with a queue and visited set
- [ ] D. Use Union-Find to determine connectivity

[View Answer](speedrun-answers.md#q8)

---

### 9. Breadth-First Search (Grid Graphs)

**Find the shortest path from start to end in a grid where some cells are blocked.**

- [ ] A. Use DFS with a visited set to find all possible paths
- [ ] B. Use BFS to explore cells level by level until reaching the end
- [ ] C. Use Dijkstra's algorithm with a modified heuristic
- [ ] D. Use A* search with Manhattan distance

[View Answer](speedrun-answers.md#q9)

---

# Medium ROI Patterns

## Depth-First Search

### 10. Depth-First Search (Trees)

**Check if a binary tree is a valid binary search tree.**

- [ ] A. Do an inorder traversal and verify if the result is sorted
- [ ] B. Calculate the sum of all node values
- [ ] C. Use level-order traversal with constraints checking
- [ ] D. Apply the Union-Find algorithm to detect cycles

[View Answer](speedrun-answers.md#q10)

---

### 11. Depth-First Search (Trees - Balance)

**Check if a binary tree is balanced (the depth of any two leaf nodes differs by at most 1).**

- [ ] A. Compare the depths of every pair of leaf nodes
- [ ] B. Use BFS to check if the tree is complete
- [ ] C. Use bottom-up DFS to calculate heights and check balance
- [ ] D. Count nodes at each level and verify even distribution

[View Answer](speedrun-answers.md#q11)

---

### 12. Depth-First Search (Graphs)

**Determine if there's a path between two nodes in a directed graph.**

- [ ] A. Use BFS with a queue starting from the source node
- [ ] B. Use DFS with recursion or a stack from the source node
- [ ] C. Use Union-Find to check if nodes are connected
- [ ] D. Calculate the transitive closure of the graph

[View Answer](speedrun-answers.md#q12)

---

### 13. Depth-First Search (Cycle Detection)

**Detect if a directed graph has a cycle.**

- [ ] A. Use a union-find data structure
- [ ] B. Apply BFS and count nodes at each level
- [ ] C. Use DFS with three node states: unvisited, in-progress, and visited
- [ ] D. Sort the adjacency list and check for repeated edges

[View Answer](speedrun-answers.md#q13)

---

## Backtracking

### 14. Backtracking (Basic)

**Generate all possible combinations of k numbers from 1 to n.**

- [ ] A. Use dynamic programming with a 2D table
- [ ] B. Apply BFS with branching at each level
- [ ] C. Use recursion with backtracking, adding and removing elements
- [ ] D. Build a mathematical formula to calculate all combinations

[View Answer](speedrun-answers.md#q14)

---

### 15. Backtracking (Subsets)

**Generate all possible subsets of a set of distinct integers.**

- [ ] A. Use bit manipulation to represent all subsets
- [ ] B. Use a mathematical formula for combinations
- [ ] C. Use recursion with backtracking, including/excluding each element
- [ ] D. Implement a breadth-first approach generating subsets level by level

[View Answer](speedrun-answers.md#q15)

---

### 16. Backtracking (Permutations)

**Generate all permutations of a string with distinct characters.**

- [ ] A. Use mathematical formulas to generate permutations directly
- [ ] B. Use recursion with swapping characters at each position
- [ ] C. Generate all subsets first, then arrange each subset
- [ ] D. Use a queue to iteratively build permutations level by level

[View Answer](speedrun-answers.md#q16)

---

### 17. Backtracking (Constraint Satisfaction)

**Solve a Sudoku puzzle.**

- [ ] A. Use a greedy algorithm to fill in obvious cells first
- [ ] B. Apply backtracking with constraint checking for each cell
- [ ] C. Convert to a graph coloring problem and use BFS
- [ ] D. Use dynamic programming with a state table

[View Answer](speedrun-answers.md#q17)

---

### 18. Backtracking (N-Queens)

**Count the number of ways to arrange n queens on an n×n chessboard so that no two queens threaten each other.**

- [ ] A. Use a greedy algorithm to place queens optimally
- [ ] B. Apply dynamic programming with state tables
- [ ] C. Use backtracking with constraint checking and counting valid arrangements
- [ ] D. Calculate mathematically using combinatorics

[View Answer](speedrun-answers.md#q18)

---

## Binary Search

### 19. Binary Search (Basic)

**Find a specific value in a sorted array.**

- [ ] A. Use sequential search from the beginning
- [ ] B. Use binary search, repeatedly dividing the search space in half
- [ ] C. Use interpolation search based on values distribution
- [ ] D. Use exponential search followed by binary search

[View Answer](speedrun-answers.md#q19)

---

### 20. Binary Search (Boundary)

**Find the index of the first occurrence of a value in a sorted array with duplicates.**

- [ ] A. Use linear search from the beginning until finding the value
- [ ] B. Use binary search to find any occurrence, then scan left
- [ ] C. Use binary search but continue leftward even after finding a match
- [ ] D. Sort the array indices by value and find the smallest index

[View Answer](speedrun-answers.md#q20)

---

### 21. Binary Search (Rotated Array)

**Find a value in a sorted array that was rotated at an unknown pivot point.**

- [ ] A. First find the pivot, then perform binary search on the appropriate half
- [ ] B. Modified binary search that handles the rotation internally
- [ ] C. Search both halves of the array using regular binary search
- [ ] D. Convert to a normal sorted array first, then use standard binary search

[View Answer](speedrun-answers.md#q21)

---

### 22. Binary Search (On Answer)

**Find the minimum capacity of ships needed to transport packages within a given number of days.**

- [ ] A. Use dynamic programming to find optimal distribution
- [ ] B. Use a greedy approach assigning packages sequentially
- [ ] C. Binary search on the potential capacity values
- [ ] D. Sort packages and assign to ships using two pointers

[View Answer](speedrun-answers.md#q22)

---

### 23. Binary Search (First Bad Version)

**Find the first bad version in a series of versions where all versions after a bad one are also bad.**

- [ ] A. Check versions sequentially from the beginning
- [ ] B. Use binary search to find the first bad version
- [ ] C. Apply two-pointer technique from both ends
- [ ] D. Use a breadth-first search starting from the middle version

[View Answer](speedrun-answers.md#q23)

---

## Heap

### 24. Heap (Top K Elements)

**Find the k largest elements in an array.**

- [ ] A. Sort the array and return the last k elements
- [ ] B. Use quickselect algorithm to find the kth largest element
- [ ] C. Maintain a min-heap of size k while processing the array
- [ ] D. Use two pointers to partition the array around k

[View Answer](speedrun-answers.md#q24)

---

### 25. Heap (Two Heaps)

**Find the median of a data stream.**

- [ ] A. Sort the stream after each addition
- [ ] B. Maintain a balanced binary search tree
- [ ] C. Use two heaps: a max-heap for the smaller half and a min-heap for the larger half
- [ ] D. Track the sum and count to calculate average

[View Answer](speedrun-answers.md#q25)

---

## Binary Search Tree

### 26. Binary Search Tree (Traversal)

**Find the kth smallest element in a binary search tree.**

- [ ] A. Do an inorder traversal and return the kth element
- [ ] B. Use a min-heap to track the k smallest elements
- [ ] C. Apply Morris traversal for constant space
- [ ] D. Convert the BST to a sorted array and return the kth element

[View Answer](speedrun-answers.md#q26)

---

## Fast & Slow Pointers

### 27. Fast & Slow Pointers (Cycle Detection)

**Detect if a linked list has a cycle.**

- [ ] A. Use a hash set to track visited nodes
- [ ] B. Use fast and slow pointers to detect a cycle
- [ ] C. Count the number of nodes and check if it exceeds the expected length
- [ ] D. Use a stack to track the traversal path

[View Answer](speedrun-answers.md#q27)

---

### 28. Fast & Slow Pointers (Middle Finding)

**Find the middle node of a linked list in a single pass.**

- [ ] A. First count the nodes, then traverse to the middle
- [ ] B. Use recursion to find the depth and middle node simultaneously
- [ ] C. Use a slow pointer and a fast pointer that moves twice as fast
- [ ] D. Use a stack to store nodes and find the middle

[View Answer](speedrun-answers.md#q28)

---

## Dynamic Programming

### 29. Dynamic Programming (Kadane's Algorithm)

**Find the maximum sum of a contiguous subarray in an array of integers.**

- [ ] A. Sort the array and take the largest elements
- [ ] B. Use dynamic programming to track maximum subarray ending at each position
- [ ] C. Apply two pointers to track the subarray boundaries
- [ ] D. Calculate the prefix sum and find the maximum difference

[View Answer](speedrun-answers.md#q29)

---

### 30. Dynamic Programming (0/1 Knapsack)

**Given weights and values of n items, put them in a knapsack of capacity W to get the maximum value.**

- [ ] A. Use a greedy approach by selecting items with the highest value/weight ratio
- [ ] B. Apply BFS to explore all possible combinations
- [ ] C. Use dynamic programming with a 2D table to track optimal values
- [ ] D. Sort items by value and add them until capacity is reached

[View Answer](speedrun-answers.md#q30)

---

### 31. Dynamic Programming (Unbounded Knapsack)

**Given coins of different denominations and a total amount, find the minimum number of coins needed to make up that amount.**

- [ ] A. Sort the coins and use a greedy approach
- [ ] B. Use BFS to find the shortest path to the target amount
- [ ] C. Apply DFS with memoization to explore all combinations
- [ ] D. Use dynamic programming with a 1D array to track minimum coins

[View Answer](speedrun-answers.md#q31)

---

### 32. Dynamic Programming (Longest Common Subsequence)

**Find the length of the longest common subsequence between two strings.**

- [ ] A. Use a sliding window to compare substrings
- [ ] B. Apply a hash map to count common characters
- [ ] C. Use dynamic programming with a 2D table to build the LCS
- [ ] D. Convert both strings to character frequency arrays and compare

[View Answer](speedrun-answers.md#q32)

---

### 33. Dynamic Programming (Fibonacci Pattern)

**Count the number of ways to reach the nth stair when you can climb 1 or 2 stairs at a time.**

- [ ] A. Use recursion to try all combinations
- [ ] B. Apply BFS to find all possible paths
- [ ] C. Use dynamic programming with Fibonacci pattern
- [ ] D. Apply combinatorial formula directly

[View Answer](speedrun-answers.md#q33)

---

# Low ROI Patterns

## Divide and Conquer

### 34. Divide and Conquer

**Implement a function to find the maximum subarray sum using divide and conquer.**

- [ ] A. Use Kadane's algorithm to track maximum sum ending at each position
- [ ] B. Divide the array in half recursively and find the maximum subarray crossing the midpoint
- [ ] C. Sort the array and take the largest elements
- [ ] D. Use dynamic programming with a 2D table

[View Answer](speedrun-answers.md#q34)

---

## Trie

### 35. Trie (Prefix Tree)

**Implement an autocomplete system that suggests words based on a prefix.**

- [ ] A. Use a hash map to store all possible prefixes
- [ ] B. Apply binary search on a sorted list of words
- [ ] C. Build a trie data structure for efficient prefix matching
- [ ] D. Use a bloom filter to check if prefixes exist

[View Answer](speedrun-answers.md#q35)

---

### 36. Trie (Advanced Usage)

**Design a data structure for efficiently searching words by prefix.**

- [ ] A. Use a hash map with all possible prefixes as keys
- [ ] B. Implement a trie (prefix tree) with character nodes
- [ ] C. Use a sorted array of strings with binary search
- [ ] D. Implement a balanced binary search tree of strings

[View Answer](speedrun-answers.md#q36)

---

## Union Find

### 37. Union Find (Basics)

**Given a list of edges, determine if they form a valid tree (connected graph without cycles).**

- [ ] A. Use DFS to detect cycles in the graph
- [ ] B. Apply BFS to check connectivity
- [ ] C. Use Union-Find to merge connected components and detect cycles
- [ ] D. Sort the edges by weight and use a greedy algorithm

[View Answer](speedrun-answers.md#q37)

---

### 38. Union Find (Component Counting)

**Determine the number of connected components in an undirected graph.**

- [ ] A. Use depth-first search to count connected components
- [ ] B. Use breadth-first search from each unvisited node
- [ ] C. Use Union-Find to merge connected nodes and count sets
- [ ] D. Convert to an adjacency matrix and analyze connectivity

[View Answer](speedrun-answers.md#q38)

---

## Greedy Algorithms

### 39. Greedy Algorithms (Activity Selection)

**Given a set of activities with start and end times, find the maximum number of activities that can be performed by a single person.**

- [ ] A. Sort activities by their duration and select the shortest ones
- [ ] B. Sort activities by start time and select non-overlapping ones
- [ ] C. Sort activities by end time and select non-overlapping ones
- [ ] D. Use dynamic programming to explore all possible combinations

[View Answer](speedrun-answers.md#q39)

---

### 40. Greedy Algorithms (Interval Scheduling)

**Determine the minimum number of intervals to remove to make all remaining intervals non-overlapping.**

- [ ] A. Remove intervals with the longest duration first
- [ ] B. Sort by start time and use dynamic programming
- [ ] C. Sort by end time and greedily select compatible intervals
- [ ] D. Use Union-Find to merge overlapping intervals

[View Answer](speedrun-answers.md#q40)

---

# Additional Patterns

## Matrix as Graph

### 41. Matrix as Graph (Island Counting)

**Find the number of distinct islands in a 2D grid, where an island is a group of connected 1's.**

- [ ] A. Use dynamic programming to count islands
- [ ] B. Apply DFS or BFS from each unvisited '1' cell, marking visited cells
- [ ] C. Use a union-find data structure to merge connected components
- [ ] D. Apply Dijkstra's algorithm to find shortest paths between islands

[View Answer](speedrun-answers.md#q41)

---

## Monotonic Stack

### 42. Monotonic Stack

**Find the next greater element for each element in an array.**

- [ ] A. Use a doubly linked list to store elements
- [ ] B. Sort the array and binary search for each element
- [ ] C. Use a stack to keep track of elements waiting for their next greater element
- [ ] D. Apply a heap to track maximum elements

[View Answer](speedrun-answers.md#q42)

---

## Topological Sort

### 43. Topological Sort

**Given a list of tasks with dependencies, find a valid order to complete all tasks.**

- [ ] A. Sort the tasks by their number of dependencies
- [ ] B. Use DFS to explore the dependency graph and detect cycles
- [ ] C. Apply BFS with indegree tracking to build the topological order
- [ ] D. Use a union-find data structure to merge related tasks

[View Answer](speedrun-answers.md#q43)

---

## Linked List Techniques

### 44. Linked List Reversal

**Reverse a linked list.**

- [ ] A. Use a stack to store nodes and rebuild in reverse order
- [ ] B. Maintain three pointers (prev, current, next) and reverse links
- [ ] C. Use a queue to reorder nodes
- [ ] D. Create a new list in reverse order

[View Answer](speedrun-answers.md#q44)

---

### 45. Linked List Reversal (Advanced)

**Reverse nodes in a linked list in groups of k.**

- [ ] A. Use recursion to reverse each group and connect them
- [ ] B. Create k separate lists and then merge them
- [ ] C. Use a stack to reverse every k elements
- [ ] D. Count nodes first, then reverse only complete groups

[View Answer](speedrun-answers.md#q45)

---

## Prefix Sums

### 46. Prefix Sums (Subarray Sum)

**Find the number of subarrays with a sum equal to a given target.**

- [ ] A. Use a sliding window with variable size
- [ ] B. Apply two pointers to track subarray boundaries
- [ ] C. Use a hash map to store prefix sums and their frequencies
- [ ] D. Sort the array and use binary search

[View Answer](speedrun-answers.md#q46)

---

## Bit Manipulation

### 47. Bit Manipulation (XOR Technique)

**Find the single number in an array where every other number appears twice.**

- [ ] A. Sort the array and check adjacent elements
- [ ] B. Use a hash map to count occurrences
- [ ] C. Apply XOR to all elements in the array
- [ ] D. Use a binary search tree to track unique elements

[View Answer](speedrun-answers.md#q47)

---

### 48. Bit Manipulation (Advanced)

**Find the only element that appears once in an array where all other elements appear exactly three times.**

- [ ] A. Sort the array and check adjacent elements
- [ ] B. Use a hash map to count occurrences
- [ ] C. Use bit manipulation to count bits modulo 3
- [ ] D. Use a mathematical formula with sums

[View Answer](speedrun-answers.md#q48)

---

## Advanced Graph Algorithms

### 49. Graph Algorithms (Dijkstra)

**Find the shortest path from a source node to all other nodes in a weighted graph with non-negative edges.**

- [ ] A. Use BFS to explore nodes level by level
- [ ] B. Apply DFS with a visited set
- [ ] C. Use Dijkstra's algorithm with a priority queue
- [ ] D. Apply the Bellman-Ford algorithm for shortest paths

[View Answer](speedrun-answers.md#q49)

---

### 50. Graph Coloring

**Determine if a graph can be colored with at most 2 colors such that no adjacent vertices have the same color.**

- [ ] A. Use a greedy algorithm to assign colors
- [ ] B. Apply BFS/DFS to color vertices and check for conflicts
- [ ] C. Use Union-Find to detect odd-length cycles
- [ ] D. Sort vertices by degree and color in order

[View Answer](speedrun-answers.md#q50)

---

## Advanced Data Structures

### 51. Design Problems (LRU Cache)

**Implement a data structure for an LRU (Least Recently Used) cache.**

- [ ] A. Use a simple array with linear search for access
- [ ] B. Implement with a balanced binary search tree
- [ ] C. Use a hash map combined with a doubly linked list
- [ ] D. Use a priority queue based on access timestamps

[View Answer](speedrun-answers.md#q51)

---

### 52. Advanced Data Structures (Segment Tree)

**Which data structure would be most efficient for range queries and updates on an array?**

- [ ] A. Binary search tree
- [ ] B. Hash table
- [ ] C. Segment tree
- [ ] D. Linked list

[View Answer](speedrun-answers.md#q52)

---

## String Algorithms

### 53. String Algorithms (KMP)

**Find all occurrences of a pattern string in a text string efficiently.**

- [ ] A. Use naive approach checking all possible positions
- [ ] B. Apply the Knuth-Morris-Pratt (KMP) algorithm using partial matches
- [ ] C. Use the Boyer-Moore algorithm with bad character and good suffix rules
- [ ] D. Apply a rolling hash (Rabin-Karp) algorithm

[View Answer](speedrun-answers.md#q53)

---

### 54. String Matching (Approximate)

**Find strings that approximately match a pattern allowing for k errors (edit distance).**

- [ ] A. Use dynamic programming to calculate edit distance for all substrings
- [ ] B. Apply the Rabin-Karp algorithm with hash comparisons
- [ ] C. Use a modified KMP algorithm with allowed errors
- [ ] D. Implement a bit-parallel algorithm like Bitap

[View Answer](speedrun-answers.md#q54)

---

## Specialized Patterns

### 55. Combinatorial Search

**Generate all possible valid combinations of n pairs of parentheses.**

- [ ] A. Use dynamic programming to build up valid strings
- [ ] B. Apply backtracking ensuring valid balance of parentheses
- [ ] C. Use BFS to build strings level by level
- [ ] D. Create a mathematical formula for Catalan numbers and generate directly

[View Answer](speedrun-answers.md#q55)

---

### 56. System Design Patterns (Rate Limiter)

**Implement a rate limiter that allows n requests per minute per user.**

- [ ] A. Use a simple counter reset every minute
- [ ] B. Implement a token bucket algorithm
- [ ] C. Use a sliding window with timestamps for each request
- [ ] D. Apply a leaky bucket algorithm that processes requests at a fixed rate

[View Answer](speedrun-answers.md#q56)

---

### 57. Memory Management (Garbage Collection)

**Which algorithm marks objects for garbage collection by starting from root objects and marking everything reachable?**

- [ ] A. Reference counting
- [ ] B. Mark and sweep
- [ ] C. Generational garbage collection
- [ ] D. Compaction

[View Answer](speedrun-answers.md#q57)

---

### 58. Concurrency Patterns (Reader-Writer Lock)

**Implement a mechanism that allows multiple readers but only one writer to access a resource simultaneously.**

- [ ] A. Use a simple mutex that locks for both readers and writers
- [ ] B. Implement a semaphore with initial value of maximum readers
- [ ] C. Use a reader-writer lock with reader count and writer flag
- [ ] D. Apply the actor model with message passing

[View Answer](speedrun-answers.md#q58)

---

### 59. Network Flow (Max Flow)

**Find the maximum flow in a flow network from source to sink.**

- [ ] A. Use Dijkstra's algorithm to find the path with maximum capacity
- [ ] B. Apply the Ford-Fulkerson algorithm with augmenting paths
- [ ] C. Use a greedy approach selecting highest capacity edges
- [ ] D. Implement Kruskal's algorithm on flow capacities

[View Answer](speedrun-answers.md#q59)

---

### 60. Specialized Trees (B-Tree)

**Which tree structure is commonly used in databases and file systems for efficient disk access?**

- [ ] A. Binary search tree
- [ ] B. Red-black tree
- [ ] C. AVL tree
- [ ] D. B-tree or B+ tree

[View Answer](speedrun-answers.md#q60)

---
