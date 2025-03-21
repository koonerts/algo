# Algorithm Patterns Speedrun Quiz

This speedrun quiz tests your ability to quickly identify algorithm patterns and apply the correct techniques to solve problems. For each question, select the correct option and check your answers below.

## 1. Two Pointers (Opposite Direction)

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

## 2. Two Pointers (Same Direction)

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

## 3. Sliding Window (Fixed Size)

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

## 4. Sliding Window (Variable Size)

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

## 5. Fast & Slow Pointers

**Determine if a linked list has a cycle.**

- [ ] A. Use a hash set to track visited nodes
- [ ] B. Use two pointers moving at different speeds
- [ ] C. Count the number of nodes and check against a threshold
- [ ] D. Use recursion to mark visited nodes

<details>
<summary>View Answer</summary>

**B. Use two pointers moving at different speeds**

Floyd's Cycle-Finding Algorithm (tortoise and hare) uses two pointers moving at different speeds. The slow pointer moves one step at a time, while the fast pointer moves two steps. If there's a cycle, the fast pointer will eventually catch up to the slow pointer.
</details>

---

## 6. Fast & Slow Pointers (Advanced)

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

## 7. Linked List Reversal

**Reverse a linked list in-place.**

- [ ] A. Use a stack to temporarily store all nodes
- [ ] B. Create a new linked list in reverse order
- [ ] C. Use three pointers (prev, current, next) and reverse links one by one
- [ ] D. Use recursion to reverse sublists and connect them

<details>
<summary>View Answer</summary>

**C. Use three pointers (prev, current, next) and reverse links one by one**

The iterative in-place approach uses three pointers: prev (initially null), current (head), and next. For each node, we save the next node, reverse the current node's pointer to point to prev, move prev to current, and current to next.
</details>

---

## 8. Linked List Reversal (Advanced)

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

## 9. Breadth-First Search (Trees)

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

## 10. Breadth-First Search (Graphs)

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

## 11. Depth-First Search (Trees)

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

## 12. Depth-First Search (Graphs)

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

## 13. Cycle Detection (Directed Graphs)

**Detect if a directed graph contains a cycle.**

- [ ] A. Use Union-Find data structure
- [ ] B. Use a single DFS with three node states: unvisited, in-progress, and finished
- [ ] C. Apply Kahn's topological sort algorithm
- [ ] D. Use two separate BFS traversals

<details>
<summary>View Answer</summary>

**B. Use a single DFS with three node states: unvisited, in-progress, and finished**

For directed graphs, we use DFS with three node states: unvisited, in-progress (currently in our DFS path), and finished. If during DFS we encounter a node that is in-progress, we've found a cycle because we're revisiting a node in our current path.
</details>

---

## 14. Backtracking (Basic)

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

## 15. Backtracking (Permutations)

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

## 16. Backtracking (Constraint Satisfaction)

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

## 17. Binary Search (Basic)

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

## 18. Binary Search (Boundary)

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

## 19. Binary Search (Rotated Array)

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

## 20. Binary Search (On Answer)

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

## 21. Binary Search Trees

**Find the kth smallest element in a Binary Search Tree.**

- [ ] A. Convert the BST to a sorted array and return the kth element
- [ ] B. Use inorder traversal with a counter to find the kth element
- [ ] C. Modify the BST nodes to store subtree size and use that for selection
- [ ] D. Use level-order traversal with priority queue

<details>
<summary>View Answer</summary>

**B. Use inorder traversal with a counter to find the kth element**

Inorder traversal of a BST visits nodes in ascending order. We perform an inorder traversal with a counter. When the counter reaches k, we've found our kth smallest element.
</details>

---

## 22. Heap (Top K Elements)

**Find the k largest elements in an unsorted array.**

- [ ] A. Sort the array and return the last k elements
- [ ] B. Use quickselect algorithm to find the kth largest element
- [ ] C. Use a min-heap of size k to track largest elements
- [ ] D. Use a max-heap containing all elements and extract k times

<details>
<summary>View Answer</summary>

**C. Use a min-heap of size k to track largest elements**

We maintain a min-heap of size k. For each element, we add it to the heap and remove the smallest element if the heap size exceeds k. After processing all elements, the heap contains the k largest elements. Time complexity: O(n log k).
</details>

---

## 23. Heap (Two Heaps)

**Design a data structure that can efficiently find the median of a stream of numbers.**

- [ ] A. Keep the stream sorted in an array
- [ ] B. Use a balanced binary search tree
- [ ] C. Use two heaps: max-heap for smaller half, min-heap for larger half
- [ ] D. Use a single heap with custom comparison logic

<details>
<summary>View Answer</summary>

**C. Use two heaps: max-heap for smaller half, min-heap for larger half**

We use two heaps: a max-heap for the smaller half of the numbers and a min-heap for the larger half. We keep them balanced (size difference ≤ 1). The median is either the top of the max-heap (if it has more elements) or the average of both tops (if equal size).
</details>

---

## 24. Matrix as Graph

**Count the number of islands in a binary grid (connected 1's surrounded by 0's or the boundary).**

- [ ] A. Use Union-Find to connect all land cells
- [ ] B. Use DFS/BFS from each unvisited land cell, marking visited cells
- [ ] C. Use dynamic programming to identify isolated regions
- [ ] D. Convert to a graph adjacency matrix and count components

<details>
<summary>View Answer</summary>

**B. Use DFS/BFS from each unvisited land cell, marking visited cells**

We treat the grid as a graph where adjacent land cells (1's) are connected. For each unvisited land cell, we perform DFS/BFS to visit all connected land cells and mark them as visited. Each such traversal corresponds to one island.
</details>

---

## 25. Monotonic Stack

**Find the next greater element for each element in an array.**

- [ ] A. Use nested loops to find the next greater element for each position
- [ ] B. Sort the array with indices and process in order
- [ ] C. Use a monotonic decreasing stack to track potential next greater elements
- [ ] D. Use a priority queue to find greater elements efficiently

<details>
<summary>View Answer</summary>

**C. Use a monotonic decreasing stack to track potential next greater elements**

We use a stack to keep track of indices of elements waiting for their next greater element. When we find a greater element, we pop indices from the stack and update their next greater element. This approach processes each element at most twice (push & pop).
</details>

---

## 26. Topological Sort

**Given a list of courses with prerequisites, find a valid order to take all courses.**

- [ ] A. Use depth-first search with a cycle check
- [ ] B. Apply Kahn's algorithm using indegree counts and a queue
- [ ] C. Sort courses by their number of prerequisites
- [ ] D. Use Union-Find to identify course groups

<details>
<summary>View Answer</summary>

**B. Apply Kahn's algorithm using indegree counts and a queue**

We use Kahn's algorithm: calculate indegree (number of prerequisites) for each course, start with courses having no prerequisites (indegree 0), and as we take each course, decrement the indegree of courses that depend on it. When a course's indegree becomes 0, add it to the queue.
</details>

---

## 27. Trie (Prefix Tree)

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

## 28. Union Find

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

## 29. Kadane's Algorithm

**Find the contiguous subarray with the largest sum in an array that may contain negative numbers.**

- [ ] A. Use a sliding window approach
- [ ] B. Implement Kadane's algorithm tracking local and global maxima
- [ ] C. Sort the array and select the largest elements
- [ ] D. Create a prefix sum array and find maximum difference

<details>
<summary>View Answer</summary>

**B. Implement Kadane's algorithm tracking local and global maxima**

Kadane's algorithm uses dynamic programming to find the maximum subarray sum. We track two values: the maximum sum ending at the current position (local_max) and the overall maximum seen so far (global_max). For each element, we decide whether to extend the current subarray or start a new one.
</details>

---

## 30. Prefix Sums

**Given an array, find the number of subarrays whose sum equals a target value.**

- [ ] A. Use nested loops to check all possible subarrays
- [ ] B. Use sliding window to find valid subarrays
- [ ] C. Calculate prefix sums and count pairs with a difference of the target
- [ ] D. Sort the array and use binary search to find pairs

<details>
<summary>View Answer</summary>

**C. Calculate prefix sums and count pairs with a difference of the target**

We calculate the prefix sum array where prefix[i] = sum of elements from 0 to i. A subarray from i to j has sum = prefix[j] - prefix[i-1]. We use a hash map to count prefix sums. For each prefix sum, we check how many previous prefix sums equal (current prefix sum - target).
</details>

---

## 31. Dynamic Programming (0/1 Knapsack)

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

## 32. Dynamic Programming (Unbounded Knapsack)

**Given unlimited quantities of coins with different values, find the minimum number of coins to make a specific amount.**

- [ ] A. Use a greedy approach always selecting the largest coin possible
- [ ] B. Use BFS to find the shortest path to the target amount
- [ ] C. Use dynamic programming with a 1D array tracking minimum coins
- [ ] D. Use a recursive approach with memoization

<details>
<summary>View Answer</summary>

**C. Use dynamic programming with a 1D array tracking minimum coins**

In the Coin Change problem, we use a 1D DP array where dp[i] = minimum coins needed to make amount i. For each coin value, we update dp[i] = min(dp[i], dp[i-coin] + 1) for all valid i. This accounts for using each coin value multiple times.
</details>

---

## 33. Dynamic Programming (Longest Common Subsequence)

**Find the length of the longest common subsequence between two strings.**

- [ ] A. Use a greedy approach matching characters from left to right
- [ ] B. Apply the longest common substring algorithm
- [ ] C. Use dynamic programming with a 2D table comparing all prefixes
- [ ] D. Convert to character frequency arrays and calculate intersection

<details>
<summary>View Answer</summary>

**C. Use dynamic programming with a 2D table comparing all prefixes**

For the LCS problem, we create a 2D DP table where dp[i][j] = length of LCS for first i characters of string1 and first j characters of string2. If the current characters match, dp[i][j] = dp[i-1][j-1] + 1. Otherwise, dp[i][j] = max(dp[i-1][j], dp[i][j-1]).
</details>

---

## 34. Dynamic Programming (Fibonacci Pattern)

**Find the number of distinct ways to climb n stairs if you can take 1 or 2 steps at a time.**

- [ ] A. Use a recursive approach with memoization
- [ ] B. Use dynamic programming with a 1D array tracking ways
- [ ] C. Apply a mathematical formula based on the Fibonacci sequence
- [ ] D. Use a combinatorial approach with binomial coefficients

<details>
<summary>View Answer</summary>

**B. Use dynamic programming with a 1D array tracking ways**

This is the classic climbing stairs problem. Let dp[i] = number of ways to reach step i. We have dp[i] = dp[i-1] + dp[i-2] (we can reach step i by taking 1 step from i-1 or 2 steps from i-2). This follows the Fibonacci pattern with dp[1] = 1 and dp[2] = 2.
</details>

---

## 35. Bit Manipulation

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

## 36. Greedy Algorithms

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

## 37. Graph Algorithms (Dijkstra)

**Find the shortest path from a source node to all other nodes in a weighted graph with non-negative edges.**

- [ ] A. Use BFS to find shortest paths in terms of edge count
- [ ] B. Apply Dijkstra's algorithm with a priority queue
- [ ] C. Use the Bellman-Ford algorithm for all pairs shortest paths
- [ ] D. Apply Floyd-Warshall algorithm to find all shortest paths

<details>
<summary>View Answer</summary>

**B. Apply Dijkstra's algorithm with a priority queue**

Dijkstra's algorithm finds shortest paths in weighted graphs with non-negative edges. We use a priority queue to always process the node with the smallest current distance. For each node, we update the distances to its neighbors if going through this node provides a shorter path.
</details>

---

## 38. Graph Algorithms (Minimum Spanning Tree)

**Find the minimum weight spanning tree in a connected, undirected graph.**

- [ ] A. Use Dijkstra's algorithm starting from any vertex
- [ ] B. Apply Kruskal's algorithm sorting edges by weight
- [ ] C. Use BFS and include all edges traversed
- [ ] D. Apply topological sort and select edges in order

<details>
<summary>View Answer</summary>

**B. Apply Kruskal's algorithm sorting edges by weight**

Kruskal's algorithm finds a minimum spanning tree by sorting all edges by weight and adding them to the tree if they don't create a cycle (checked using Union-Find). This greedy approach guarantees a minimum weight spanning tree by always selecting the lightest valid edge.
</details>

---

## 39. String Algorithms (KMP)

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

## 40. Combinatorial Search

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

## 41. Design Problems (LRU Cache)

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

## 42. System Design Patterns (Rate Limiter)

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

## 43. Memory Management (Garbage Collection)

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

## 44. Concurrency Patterns (Reader-Writer Lock)

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

## 45. Network Flow (Max Flow)

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

## 46. Computational Geometry

**Find the convex hull of a set of points in a plane (smallest convex polygon containing all points).**

- [ ] A. Use brute force checking all possible polygons
- [ ] B. Apply Graham's scan algorithm
- [ ] C. Implement a divide-and-conquer approach
- [ ] D. Use a dynamic programming solution

<details>
<summary>View Answer</summary>

**B. Apply Graham's scan algorithm**

Graham's scan finds the convex hull in O(n log n) time. It starts with the lowest point, sorts all other points by polar angle, and then processes them in order, maintaining a stack of hull points. For each point, it removes points that would create a non-convex angle before adding the new point.
</details>

---

## 47. String Matching (Approximate)

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

## 48. Randomized Algorithms

**Implement a reservoir sampling algorithm to select k items uniformly at random from a stream of unknown size.**

- [ ] A. Store all elements and randomly select k at the end
- [ ] B. Use a frequency counting approach
- [ ] C. Apply reservoir sampling with decreasing probability of replacement
- [ ] D. Use a min-heap to maintain the k largest random values

<details>
<summary>View Answer</summary>

**C. Apply reservoir sampling with decreasing probability of replacement**

Reservoir sampling selects k elements uniformly from a stream of unknown size. We keep the first k elements, then for each subsequent element i, we select it with probability k/i and randomly replace one of our k elements. This guarantees each element has equal probability of being selected.
</details>

---

## 49. Advanced Data Structures (Segment Tree)

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

## 50. Specialized Trees (B-Tree)

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