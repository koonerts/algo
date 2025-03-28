# Algorithm Patterns Speedrun Quiz - Answers

This document contains all the answers to the Algorithm Patterns Speedrun Quiz.

## Table of Contents

- [High ROI Patterns](#high-roi-patterns)
- [Medium ROI Patterns](#medium-roi-patterns)
- [Low ROI Patterns](#low-roi-patterns)
- [Additional Patterns](#additional-patterns)

---

# High ROI Patterns

## Two Pointers

### 1. Two Pointers (Opposite Direction) {#q1}

**C. Use two pointers starting from both ends of the array**

Since the array is sorted, we can use two pointers - one at the beginning and one at the end. If their sum is too large, we move the right pointer left; if too small, we move the left pointer right. This gives us O(n) time complexity.

---

### 2. Two Pointers (Same Direction) {#q2}

**B. Use a sliding window with two pointers tracking a valid segment**

This is a classic sliding window problem with two pointers moving in the same direction. We maintain a window where we've flipped at most k zeros, expanding the right pointer and contracting the left pointer when necessary to maintain our constraint.

---

## Sliding Window

### 3. Sliding Window (Fixed Size) {#q3}

**C. Maintain a fixed-size sliding window, subtracting old values and adding new ones**

With a fixed-size sliding window, we start by calculating the sum of the first k elements. Then, as we slide the window, we subtract the element leaving the window and add the element entering the window, keeping track of the maximum sum seen.

---

### 4. Sliding Window (Variable Size) {#q4}

**D. Use a sliding window that expands and contracts based on the current sum**

We use a variable-size sliding window. We expand the window by moving the right pointer until the sum is at least k, then contract it by moving the left pointer while maintaining the sum ≥ k. At each valid window, we update the minimum length.

---

### 5. Sliding Window (Variable Size - Alternative) {#q5}

**A. Use two pointers to define a window, expand until invalid, then contract**

This is a classic variable-size sliding window problem. We maintain a window using two pointers and a running sum. We expand the window by moving the right pointer until the sum exceeds our target, then contract by moving the left pointer until valid again, tracking the maximum valid window size.

---

## Breadth-First Search

### 6. Breadth-First Search (Trees) {#q6}

**B. Use a level-order traversal with a queue, tracking level sums**

BFS is perfect for level-order traversal. We use a queue to process nodes level by level, calculating the sum at each level and tracking the maximum sum level.

---

### 7. Breadth-First Search (Trees - Width) {#q7}

**B. Use level-order traversal (BFS) with node counting per level**

BFS is naturally level-by-level. We use a queue to process nodes level by level, keeping track of the number of nodes at each level. The maximum of these counts is the tree's width.

---

### 8. Breadth-First Search (Graphs) {#q8}

**C. Use breadth-first search with a queue and visited set**

For unweighted graphs, BFS naturally finds the shortest path by processing nodes in order of their distance from the start node. We use a queue and a visited set to avoid cycles.

---

### 9. Breadth-First Search (Grid Graphs) {#q9}

**B. Use BFS to explore cells level by level until reaching the end**

For unweighted graphs (where each step has the same cost), BFS naturally finds the shortest path by exploring nodes in order of their distance from the start. We use a queue and a visited set to avoid revisiting cells.

---

# Medium ROI Patterns

## Depth-First Search

### 10. Depth-First Search (Trees) {#q10}

**A. Do an inorder traversal and verify if the result is sorted**

This is one approach. Alternatively, we can use DFS with min/max constraints, where each node's value must be within a range determined by its ancestors. For a BST, inorder traversal produces elements in sorted order.

---

### 11. Depth-First Search (Trees - Balance) {#q11}

**C. Use bottom-up DFS to calculate heights and check balance**

Use post-order traversal (a type of DFS) to compute heights bottom-up. For each node, calculate the height of left and right subtrees. If their difference exceeds 1, the tree is unbalanced. This way, we can check balance in a single pass.

---

### 12. Depth-First Search (Graphs) {#q12}

**B. Use DFS with recursion or a stack from the source node**

DFS can be used to check if there's a path from source to destination. We recursively explore all paths from the source, marking nodes as visited, until we either find the destination or exhaust all possibilities.

---

### 13. Depth-First Search (Cycle Detection) {#q13}

**C. Use DFS with three node states: unvisited, in-progress, and visited**

To detect cycles in a directed graph using DFS, we maintain three states for nodes: unvisited, in-progress (in the current DFS path), and visited (finished processing). If we encounter an in-progress node during DFS, we've found a cycle.

---

## Backtracking

### 14. Backtracking (Basic) {#q14}

**C. Use recursion with backtracking, adding and removing elements**

Backtracking is perfect for generating all combinations. We recursively build combinations by adding one element at a time, exploring all possibilities, and backtracking by removing the last element before trying the next option.

---

### 15. Backtracking (Subsets) {#q15}

**C. Use recursion with backtracking, including/excluding each element**

Classic backtracking approach: for each element, we have two choices - include it in the current subset or exclude it. We recursively explore both options for each element, building subsets incrementally.

---

### 16. Backtracking (Permutations) {#q16}

**B. Use recursion with swapping characters at each position**

For each position, we try all possible characters that can be placed there (by swapping with the current character). Then we recursively generate all permutations for the remaining positions. After the recursive call, we backtrack by swapping back.

---

### 17. Backtracking (Constraint Satisfaction) {#q17}

**B. Apply backtracking with constraint checking for each cell**

For each empty cell, we try all valid digits (1-9) that don't violate Sudoku constraints (row, column, and 3x3 box). After placing a digit, we recursively try to solve the rest of the puzzle. If we reach a dead end, we backtrack and try a different digit.

---

### 18. Backtracking (N-Queens) {#q18}

**C. Use backtracking with constraint checking and counting valid arrangements**

The N-Queens problem is a classic backtracking problem. We place queens one row at a time, checking if each position is valid (not threatened by previously placed queens). We backtrack when necessary and count all valid arrangements.

---

## Binary Search

### 19. Binary Search (Basic) {#q19}

**B. Use binary search, repeatedly dividing the search space in half**

Binary search compares the target value to the middle element of the array. If they are unequal, the half in which the target cannot lie is eliminated, and the search continues on the remaining half until the target is found or the subarray size becomes zero.

---

### 20. Binary Search (Boundary) {#q20}

**C. Use binary search but continue leftward even after finding a match**

Standard binary search finds any occurrence. To find the first occurrence, when we find a match, we don't stop but instead continue searching in the left half (by setting right = mid - 1). We also remember this position as a potential answer.

---

### 21. Binary Search (Rotated Array) {#q21}

**B. Modified binary search that handles the rotation internally**

We use a modified binary search. At each step, we determine which half of the array is sorted. If the target is in the range of the sorted half, we search there; otherwise, we search the other half. This preserves the O(log n) time complexity.

---

### 22. Binary Search (On Answer) {#q22}

**C. Binary search on the potential capacity values**

Instead of searching for a value in an array, we binary search on the potential answer space (possible capacity values). For each capacity, we check if it's feasible (can ship all packages within the day limit). The minimum feasible capacity is our answer.

---

### 23. Binary Search (First Bad Version) {#q23}

**B. Use binary search to find the first bad version**

This is a classic binary search problem for finding the boundary between good and bad versions. We search for the first occurrence where isBadVersion(version) returns true.

---

## Heap

### 24. Heap (Top K Elements) {#q24}

**C. Maintain a min-heap of size k while processing the array**

To find the k largest elements, we can maintain a min-heap of size k. For each element, we add it to the heap and remove the smallest element if the heap size exceeds k. This gives us O(n log k) time complexity.

---

### 25. Heap (Two Heaps) {#q25}

**C. Use two heaps: a max-heap for the smaller half and a min-heap for the larger half**

We maintain two heaps: a max-heap for the smaller half of the numbers and a min-heap for the larger half. We balance the heaps so their sizes differ by at most 1, allowing us to find the median in O(1) time after insertion.

---

## Binary Search Tree

### 26. Binary Search Tree (Traversal) {#q26}

**A. Do an inorder traversal and return the kth element**

Since inorder traversal of a BST visits nodes in ascending order, we can simply perform an inorder traversal and return the kth element visited.

---

## Fast & Slow Pointers

### 27. Fast & Slow Pointers (Cycle Detection) {#q27}

**B. Use fast and slow pointers to detect a cycle**

The Floyd's Cycle-Finding Algorithm (tortoise and hare) uses two pointers moving at different speeds. If there's a cycle, the fast pointer will eventually catch up to the slow pointer.

---

### 28. Fast & Slow Pointers (Middle Finding) {#q28}

**C. Use a slow pointer and a fast pointer that moves twice as fast**

When the fast pointer reaches the end of the list, the slow pointer will be at the middle. The fast pointer moves two steps for every one step of the slow pointer. When the fast pointer reaches the end (or null), the slow pointer will be at the middle.

---

## Dynamic Programming

### 29. Dynamic Programming (Kadane's Algorithm) {#q29}

**B. Use dynamic programming to track maximum subarray ending at each position**

Kadane's algorithm is a dynamic programming approach that maintains two variables: the maximum subarray sum ending at the current position, and the global maximum subarray sum. We iterate through the array once, updating these values.

---

### 30. Dynamic Programming (0/1 Knapsack) {#q30}

**C. Use dynamic programming with a 2D table to track optimal values**

The 0/1 Knapsack problem is solved using dynamic programming. We create a 2D table where dp[i][w] represents the maximum value achievable with the first i items and weight limit w.

---

### 31. Dynamic Programming (Unbounded Knapsack) {#q31}

**D. Use dynamic programming with a 1D array to track minimum coins**

The Coin Change problem is an unbounded knapsack problem. We use a 1D DP array where dp[i] represents the minimum number of coins needed to make amount i. For each coin, we update dp[i] = min(dp[i], dp[i - coin] + 1).

---

### 32. Dynamic Programming (Longest Common Subsequence) {#q32}

**C. Use dynamic programming with a 2D table to build the LCS**

The Longest Common Subsequence problem uses a 2D DP table where dp[i][j] represents the length of the LCS of the first i characters of string 1 and the first j characters of string 2.

---

### 33. Dynamic Programming (Fibonacci Pattern) {#q33}

**C. Use dynamic programming with Fibonacci pattern**

This is the classic climbing stairs problem, which follows the Fibonacci pattern. The number of ways to reach the nth stair is the sum of the ways to reach the (n-1)th and (n-2)th stairs.

---

# Low ROI Patterns

## Divide and Conquer

### 34. Divide and Conquer {#q34}

**B. Divide the array in half recursively and find the maximum subarray crossing the midpoint**

The divide and conquer approach splits the array in half and recursively finds the maximum subarray in the left half, right half, and crossing the middle. The maximum of these three is the answer. This is different from Kadane's algorithm which uses dynamic programming.

---

## Trie

### 35. Trie (Prefix Tree) {#q35}

**C. Build a trie data structure for efficient prefix matching**

A trie is designed for prefix operations. We can navigate to the node corresponding to the prefix and then traverse all paths from that node to get all words with that prefix.

---

### 36. Trie (Advanced Usage) {#q36}

**B. Implement a trie (prefix tree) with character nodes**

A trie is optimized for prefix operations. Each node represents a character and has links to child nodes for subsequent characters. To check if a prefix exists, we navigate the trie character by character. If we can follow the entire prefix, it exists in our dictionary.

---

## Union Find

### 37. Union Find (Basics) {#q37}

**C. Use Union-Find to merge connected components and detect cycles**

Union-Find is perfect for this problem. We process each edge, unioning the sets of the connected nodes. If we attempt to union nodes already in the same set, we've found a cycle. A valid tree has n-1 edges and no cycles.

---

### 38. Union Find (Component Counting) {#q38}

**C. Use Union-Find to merge connected nodes and count sets**

Union-Find efficiently tracks disjoint sets. For each edge (u,v), we union the sets containing u and v. After processing all edges, the number of disjoint sets equals the number of connected components.

---

## Greedy Algorithms

### 39. Greedy Algorithms (Activity Selection) {#q39}

**C. Sort activities by end time and select non-overlapping ones**

This is the Activity Selection problem. The greedy approach is to sort activities by their end times and select activities that don't overlap with the previously selected activity.

---

### 40. Greedy Algorithms (Interval Scheduling) {#q40}

**C. Sort by end time and greedily select compatible intervals**

We sort intervals by end time and greedily select intervals that don't overlap with the previously selected interval. The number of intervals we can't select is the minimum number to remove. This works because selecting the interval that ends earliest maximizes flexibility for future selections.

---

# Additional Patterns

## Matrix as Graph

### 41. Matrix as Graph (Island Counting) {#q41}

**B. Apply DFS or BFS from each unvisited '1' cell, marking visited cells**

We can treat the matrix as a graph where adjacent cells are connected. For each unvisited '1' cell, we perform DFS or BFS to explore and mark the entire island as visited, incrementing our count for each new island we discover.

---

## Monotonic Stack

### 42. Monotonic Stack {#q42}

**C. Use a stack to keep track of elements waiting for their next greater element**

A monotonic stack is perfect for this problem. We maintain a stack of elements waiting for their next greater element. When we encounter a greater element, we pop from the stack and update their results.

---

## Topological Sort

### 43. Topological Sort {#q43}

**C. Apply BFS with indegree tracking to build the topological order**

Topological sorting can be implemented using BFS with indegree tracking. We start with nodes that have no dependencies (indegree=0), remove them, update the indegrees of their neighbors, and continue until all nodes are processed or we detect a cycle.

---

## Linked List Techniques

### 44. Linked List Reversal {#q44}

**B. Maintain three pointers (prev, current, next) and reverse links**

The iterative approach to reversing a linked list involves maintaining three pointers: prev, current, and next. We traverse the list once, reversing the next pointer of each node to point to the previous node.

---

### 45. Linked List Reversal (Advanced) {#q45}

**A. Use recursion to reverse each group and connect them**

We recursively reverse the first k nodes using the same technique as reversing a whole linked list. Then, we connect the reversed part with the recursively processed rest of the list (which will have its own k-groups reversed).

---

## Prefix Sums

### 46. Prefix Sums (Subarray Sum) {#q46}

**C. Use a hash map to store prefix sums and their frequencies**

We calculate the prefix sum while iterating through the array. For each position, we check if (prefix_sum - target) exists in our hash map, which would indicate a subarray with the target sum ending at the current position.

---

## Bit Manipulation

### 47. Bit Manipulation (XOR Technique) {#q47}

**C. Apply XOR to all elements in the array**

This is a classic bit manipulation problem. XORing a number with itself results in 0, and XORing with 0 leaves the number unchanged. By XORing all elements, the duplicates cancel out, leaving only the single number.

---

### 48. Bit Manipulation (Advanced) {#q48}

**C. Use bit manipulation to count bits modulo 3**

We count the number of 1s at each bit position for all numbers. Since each bit of a number that appears three times contributes either 0 or 3 to the count, the bits from the unique number will make the count not divisible by 3. We construct our answer from these bits.

---

## Advanced Graph Algorithms

### 49. Graph Algorithms (Dijkstra) {#q49}

**C. Use Dijkstra's algorithm with a priority queue**

Dijkstra's algorithm is designed for this exact problem. It uses a priority queue to always process the node with the smallest current distance, guaranteeing the shortest path to each node.

---

### 50. Graph Coloring {#q50}

**B. Apply BFS/DFS to color vertices and check for conflicts**

This is a bipartite graph check. We use BFS or DFS to color the graph with 2 colors, alternating colors for adjacent vertices. If at any point we can't assign a different color to an adjacent vertex, the graph is not bipartite.

---

## Advanced Data Structures

### 51. Design Problems (LRU Cache) {#q51}

**C. Use a hash map combined with a doubly linked list**

An efficient LRU cache combines a hash map for O(1) lookups with a doubly linked list to maintain order of use. When an item is accessed, it's moved to the front of the list (most recently used). When capacity is reached, we remove the item at the end of the list (least recently used).

---

### 52. Advanced Data Structures (Segment Tree) {#q52}

**C. Segment tree**

A segment tree is specialized for range queries and updates. It's a binary tree where each node represents a range of the array. Leaf nodes represent individual elements, and internal nodes represent the combined result (sum, min, max, etc.) of their children. This allows for O(log n) range queries and updates.

---

## String Algorithms

### 53. String Algorithms (KMP) {#q53}

**B. Apply the Knuth-Morris-Pratt (KMP) algorithm using partial matches**

KMP avoids unnecessary comparisons by using information from previous matches. It preprocesses the pattern to create a "partial match" table, which indicates how much of the pattern can be skipped when a mismatch occurs. This reduces the time complexity to O(n+m) where n and m are the lengths of text and pattern.

---

### 54. String Matching (Approximate) {#q54}

**D. Implement a bit-parallel algorithm like Bitap**

The Bitap algorithm (also known as Shift-OR or Baeza-Yates-Gonnet algorithm) uses bit manipulation for approximate string matching. It can be modified to handle up to k errors by maintaining k+1 bit arrays. This approach is particularly efficient for patterns shorter than the word size.

---

## Specialized Patterns

### 55. Combinatorial Search {#q55}

**B. Apply backtracking ensuring valid balance of parentheses**

We use backtracking with two rules: we can add an opening parenthesis if we haven't used all n, and we can add a closing parenthesis if there are unclosed opening parentheses. This ensures all generated combinations are valid.

---

### 56. System Design Patterns (Rate Limiter) {#q56}

**C. Use a sliding window with timestamps for each request**

A sliding window approach keeps track of timestamps of requests in the last minute. For each new request, we clean out timestamps older than 1 minute and check if the remaining count is less than the limit. This ensures exactly n requests per minute regardless of distribution within the minute.

---

### 57. Memory Management (Garbage Collection) {#q57}

**B. Mark and sweep**

Mark and Sweep is a garbage collection algorithm that works in two phases: 1) Mark: start from root objects and recursively mark all reachable objects as "in use" 2) Sweep: scan the entire memory and free any objects not marked as "in use". This identifies and collects all unreachable objects.

---

### 58. Concurrency Patterns (Reader-Writer Lock) {#q58}

**C. Use a reader-writer lock with reader count and writer flag**

A reader-writer lock allows multiple readers to access the resource simultaneously, but grants exclusive access to writers. It typically uses a mutex to protect a reader count and a writer flag. Readers increment/decrement the count, while writers check for zero readers and set the writer flag.

---

### 59. Network Flow (Max Flow) {#q59}

**B. Apply the Ford-Fulkerson algorithm with augmenting paths**

The Ford-Fulkerson algorithm finds maximum flow by repeatedly finding augmenting paths (paths with available capacity) from source to sink and sending flow through them. We continue until no augmenting path exists. The Edmonds-Karp variant uses BFS to find the shortest augmenting path each time.

---

### 60. Specialized Trees (B-Tree) {#q60}

**D. B-tree or B+ tree**

B-trees and B+ trees are optimized for systems that read and write large blocks of data, like databases and file systems. They have a high branching factor, keeping the tree height small which minimizes disk accesses. B+ trees additionally link the leaves, making range queries more efficient.

---
