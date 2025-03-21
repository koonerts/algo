# Algorithm Pattern Identification Guide

This guide helps you identify which algorithm pattern to use based on problem characteristics. For each pattern, we provide:

1. **How to Identify:** Key signs that suggest using this pattern
2. **Example Problem Types:** Typical problems that use this pattern
3. **Time & Space Complexity:** General complexity characteristics

---

# Array Patterns

## Sliding Window

**How to Identify:**

- Problems involving contiguous subarrays or substrings
- Finding max/min/sum over a contiguous sequence of fixed or variable size
- Problems asking for longest/shortest subarray with a given property

**Example Problem Types:**

- Maximum sum subarray of size K
- Longest substring with K distinct characters
- Minimum size subarray with a given sum
- String permutations or anagrams

**Time & Space Complexity:**

- Time: O(n) where n is array length (each element processed at most twice)
- Space: O(1) for fixed window, O(k) where k is window size for variable window

### Two Pointers

**How to Identify:**

- Problems involving sorted arrays or linked lists
- Need to find pairs or triplets satisfying certain conditions
- Problems asking for in-place array modification
- Finding intersections or palindromes

**Example Problem Types:**

- Two Sum, Three Sum
- Container with Most Water
- Remove duplicates from sorted array
- Palindrome verification

**Time & Space Complexity:**

- Time: O(n) for most implementations or O(n²) for nested two pointers
- Space: O(1) as typically implemented in-place

### Kadane's Algorithm

**How to Identify:**

- Finding maximum/minimum sum subarray
- Requiring contiguous elements with optimal value
- When greedy approach with local/global optimal values works

**Example Problem Types:**

- Maximum sum subarray
- Maximum product subarray
- Circular array maximum sum

**Time & Space Complexity:**

- Time: O(n)
- Space: O(1)

### Prefix Sums

**How to Identify:**

- Range sum queries
- Cumulative operations on arrays
- Checking for specific sum conditions over subarrays

**Example Problem Types:**

- Range sum queries
- Subarray sum equals K
- Count number of subarrays with specific properties

**Time & Space Complexity:**

- Time: O(n) for preprocessing, O(1) for queries
- Space: O(n) for storing prefix sums

---

## Linked List Patterns

### Fast & Slow Pointers

**How to Identify:**

- Cycle detection problems
- Finding middle element
- Finding nth element from the end
- Identifying if linked list has a cycle

**Example Problem Types:**

- Detect cycle in linked list
- Find cycle start point
- Find middle of linked list
- Palindrome linked list

**Time & Space Complexity:**

- Time: O(n)
- Space: O(1)

### Linked List Reversal

**How to Identify:**

- Problems requiring reversal of all or part of a linked list
- Problems involving K-groups or alternative reverse operations

**Example Problem Types:**

- Reverse linked list
- Reverse nodes in K-group
- Reverse alternating K elements

**Time & Space Complexity:**

- Time: O(n)
- Space: O(1) for iterative solutions, O(n) for recursive solutions

---

## Tree Patterns

### Tree Traversal

**How to Identify:**

- Problems requiring visiting all nodes in a tree
- Node relationship problems
- Searching or collecting data from all nodes

**Example Problem Types:**

- Preorder, inorder, postorder traversal
- Level order traversal
- Path sum problems
- Tree serialization/deserialization

**Time & Space Complexity:**

- Time: O(n) where n is number of nodes
- Space: O(h) where h is tree height for recursion, O(n) worst case

### Depth-First Search (DFS)

**How to Identify:**

- Problems requiring exhaustive tree/graph exploration
- Path finding problems
- Problems requiring backtracking
- Problems that need to go as deep as possible before backtracking

**Example Problem Types:**

- Path existence between nodes
- Connected components
- Topological sorting
- Cycle detection

**Time & Space Complexity:**

- Time: O(V + E) where V is vertices and E is edges
- Space: O(h) for recursion stack where h is maximum depth

# Breadth-First Search (BFS)

**How to Identify:**

- Finding shortest path in unweighted graph/tree
- Level-order traversal
- Problems requiring exploration in layers
- Finding nodes at k distance

**Example Problem Types:**

- Shortest path in unweighted graph
- Level order traversal
- Word ladder problems
- Connected components

**Time & Space Complexity:**

- Time: O(V + E) where V is vertices and E is edges
- Space: O(w) where w is maximum width of tree/graph

## Binary Search Tree

**How to Identify:**

- Ordered operations on trees
- Search, insertion, deletion with ordering requirements
- Validation of BST properties

**Example Problem Types:**

- Validate BST
- Insert/delete in BST
- Kth smallest element in BST
- Floor/ceiling values in BST

**Time & Space Complexity:**

- Time: O(h) where h is tree height
- Space: O(h) for recursion stack

### Trie (Prefix Tree)

**How to Identify:**

- Dictionary operations on strings
- Prefix matching problems
- Problems involving character-by-character processing
- Autocomplete or spell-checker functionalities

**Example Problem Types:**

- Implement prefix tree
- Word search in a dictionary
- Autocomplete feature
- Longest common prefix

**Time & Space Complexity:**

- Time: O(m) for insertions and searches, where m is key length
- Space: O(n * m) where n is number of keys, m is average key length

## Graph Patterns

### Dijkstra's Algorithm

**How to Identify:**

- Finding shortest path in weighted graph with non-negative weights
- Optimizing distance between nodes
- Pathfinding with cost considerations
- Network routing problems with weights

**Example Problem Types:**

- Network routing
- GPS navigation
- Flight scheduling
- Network Delay Time (LC#743)

**Time & Space Complexity:**

- Time: O((V + E) log V) with binary heap implementation
- Space: O(V)

### Union-Find (Disjoint Set)

**How to Identify:**

- Problems involving connected components
- Need to check if elements are in same set
- Dynamic connectivity problems
- Cycle detection in undirected graphs

**Example Problem Types:**

- Kruskal's algorithm for MST
- Find connected components
- Redundant connection detection

**Time & Space Complexity:**

- Time: O(α(n)) amortized per operation where α is inverse Ackermann function
- Space: O(n)

## Dynamic Programming Patterns

### 0/1 Knapsack Pattern

**How to Identify:**

- Discrete items with values/weights
- Binary decisions (include/exclude)
- Maximizing/minimizing value with constraints

**Example Problem Types:**

- 0/1 Knapsack
- Subset Sum
- Equal Subset Sum Partition
- Minimum Subset Sum Difference

**Time & Space Complexity:**

- Time: O(n * C) where n is items, C is capacity
- Space: O(n * C), can be optimized to O(C)

### Unbounded Knapsack Pattern

**How to Identify:**

- Items can be used multiple times
- Selecting repeated elements with constraints
- Max/min value problems with unlimited supply

**Example Problem Types:**

- Coin Change (min coins)
- Coin Change II (number of ways)
- Rod Cutting
- Maximum ribbon cut

**Time & Space Complexity:**

- Time: O(n * C) where n is item types, C is capacity
- Space: O(C)

### Longest Common Subsequence (LCS) Pattern

**How to Identify:**

- Problems comparing sequences
- Finding common elements or differences between strings
- Edit distance variations

**Example Problem Types:**

- Longest Common Subsequence
- Shortest Common Supersequence
- Edit Distance
- Longest Palindromic Subsequence

**Time & Space Complexity:**

- Time: O(m * n) where m, n are string lengths
- Space: O(m * n)

### Fibonacci Sequence Pattern

**How to Identify:**

- Problems with recursive relation f(n) = f(n-1) + f(n-2)
- Current state depends on 1-2 previous states
- Counting distinct ways to reach a target

**Example Problem Types:**

- Fibonacci Numbers
- Staircase
- House Thief (similar to non-adjacent elements)
- Jump Game variations

**Time & Space Complexity:**

- Time: O(n)
- Space: O(n) can be optimized to O(1)

## Backtracking Patterns

### Subsets Pattern

**How to Identify:**

- Generating all possible subsets/combinations/permutations
- Need to explore multiple choices at each step
- Building combinations with specific constraints

**Example Problem Types:**

- Generate Subsets/Powerset
- Permutations
- Combinations
- Letter Combinations of Phone Number

**Time & Space Complexity:**

- Time: O(2^n) for subsets, O(n!) for permutations
- Space: O(n) for recursion stack

### Constraint Satisfaction Pattern

**How to Identify:**

- Problems with complex constraints
- Search space can be pruned early
- Need to find all valid solutions or one valid solution

**Example Problem Types:**

- N-Queens
- Sudoku Solver
- Word Search
- Palindrome Partitioning

**Time & Space Complexity:**

- Time: Exponential, but pruning reduces actual runtime
- Space: O(n) for recursion stack

## Heap Patterns

### Top K Elements Pattern

**How to Identify:**

- Finding top/smallest K elements
- Stream processing with limited memory
- Maintaining a running set of maximum/minimum elements

**Example Problem Types:**

- Kth Largest Element
- K Closest Points to Origin
- Top K Frequent Elements
- Sort K-sorted Array

**Time & Space Complexity:**

- Time: O(n log k) for processing n elements with heap of size k
- Space: O(k) for the heap

### Two Heaps Pattern

**How to Identify:**

- Median calculation problems
- Balancing elements on either side of a midpoint
- Processing stream data with statistics

**Example Problem Types:**

- Find Median from Data Stream
- Sliding Window Median
- IPO (maximize capital)

**Time & Space Complexity:**

- Time: O(log n) per element insertion
- Space: O(n) for storing all elements

## Additional Patterns

### Binary Search Variations

**How to Identify:**

- Sorted arrays or matrix
- Problems where search space can be halved each time
- Finding exact match or closest element
- Monotonically increasing/decreasing properties

**Example Problem Types:**

- Standard binary search
- Search in rotated sorted array
- Search for a range
- Find minimum in rotated sorted array

**Time & Space Complexity:**

- Time: O(log n)
- Space: O(1) iterative, O(log n) recursive

### Greedy Algorithms

**How to Identify:**

- Local optimal choice leads to global optimum
- Problems where you can make choices without reconsidering
- Optimization problems with "obvious" next steps

**Example Problem Types:**

- Activity selection
- Huffman coding
- Fractional knapsack
- Interval scheduling

**Time & Space Complexity:**

- Time: Usually O(n log n) due to sorting
- Space: Usually O(1) or O(n)

### Bit Manipulation

**How to Identify:**

- Problems involving binary representation
- XOR, AND, OR operations
- Problems requiring space optimization
- Numeric problems that can exploit bit properties

**Example Problem Types:**

- Counting bits
- Finding single number among duplicates
- Power set generation via bits
- Bit manipulation tricks

**Time & Space Complexity:**

- Time: O(1) to O(n) depending on problem
- Space: Usually O(1)

## Amazon LeetCode Problems by Pattern

This section categorizes common Amazon interview problems from LeetCode by their algorithmic patterns.

### Array Patterns

#### Sliding Window

- 3: Longest Substring Without Repeating Characters
- 76: Minimum Window Substring
- 438: Find All Anagrams in a String
- 567: Permutation in String
- 1358: Number of Substrings Containing All Three Characters

#### Two Pointers

- 1: Two Sum
- 11: Container With Most Water
- 15: 3Sum
- 18: 4Sum
- 26: Remove Duplicates from Sorted Array
- 42: Trapping Rain Water
- 88: Merge Sorted Array
- 121: Best Time to Buy and Sell Stock
- 680: Valid Palindrome II

#### Kadane's Algorithm

- 53: Maximum Subarray
- 152: Maximum Product Subarray
- 1749: Maximum Absolute Sum of Any Subarray

#### Prefix Sums

- 560: Subarray Sum Equals K
- 525: Contiguous Array
- 907: Sum of Subarray Minimums

### Linked List Patterns

#### Fast & Slow Pointers

- 141: Linked List Cycle
- 142: Linked List Cycle II
- 143: Reorder List
- 234: Palindrome Linked List

#### Linked List Reversal

- 92: Reverse Linked List II
- 206: Reverse Linked List
- 25: Reverse Nodes in k-Group

#### Other Linked List Patterns

- 2: Add Two Numbers
- 23: Merge k Sorted Lists
- 138: Copy List with Random Pointer
- 160: Intersection of Two Linked Lists

### Tree Patterns

#### Tree Traversal

- 102: Binary Tree Level Order Traversal
- 103: Binary Tree Zigzag Level Order Traversal
- 199: Binary Tree Right Side View
- 543: Diameter of Binary Tree
- 863: All Nodes Distance K in Binary Tree

#### DFS Pattern

- 124: Binary Tree Maximum Path Sum
- 236: Lowest Common Ancestor of a Binary Tree
- 437: Path Sum III
- 112: Path Sum

#### Binary Search Tree

- 98: Validate Binary Search Tree
- 108: Convert Sorted Array to Binary Search Tree
- 230: Kth Smallest Element in a BST
- 235: Lowest Common Ancestor of a Binary Search Tree

### Graph Patterns

#### BFS Pattern

- 127: Word Ladder
- 200: Number of Islands
- 994: Rotting Oranges
- 1293: Shortest Path in a Grid with Obstacles Elimination
- 909: Snakes and Ladders

#### DFS & Backtracking

- 79: Word Search
- 212: Word Search II
- 547: Number of Provinces
- 695: Max Area of Island
- 841: Keys and Rooms

#### Topological Sort

- 207: Course Schedule
- 210: Course Schedule II
- 332: Reconstruct Itinerary

#### Union-Find

- 399: Evaluate Division

### Dynamic Programming Patterns

#### Knapsack Patterns

- 322: Coin Change
- 403: Frog Jump

#### LCS Patterns

- 5: Longest Palindromic Substring
- 72: Edit Distance
- 516: Longest Palindromic Subsequence

#### Fibonacci Patterns

- 70: Climbing Stairs
- 55: Jump Game
- 45: Jump Game II
- 198: House Robber

#### 2D Dynamic Programming

- 62: Unique Paths
- 64: Minimum Path Sum

#### LIS Pattern

- 300: Longest Increasing Subsequence

### Backtracking Patterns

#### Subsets Pattern

- 17: Letter Combinations of a Phone Number
- 22: Generate Parentheses
- 39: Combination Sum
- 46: Permutations
- 78: Subsets
- 131: Palindrome Partitioning

#### Constraint Satisfaction

- 36: Valid Sudoku
- 51: N-Queens
- 773: Sliding Puzzle

### Heap Patterns

#### Top K Elements

- 215: Kth Largest Element in an Array
- 347: Top K Frequent Elements
- 658: Find K Closest Elements
- 692: Top K Frequent Words
- 703: Kth Largest Element in a Stream
- 973: K Closest Points to Origin

#### Two Heaps Pattern

- 295: Find Median from Data Stream

#### Other Heap Applications

- 632: Smallest Range Covering Elements from K Lists
- 1642: Furthest Building You Can Reach

### Searching Problems

#### Binary Search

- 4: Median of Two Sorted Arrays
- 33: Search in Rotated Sorted Array
- 34: Find First and Last Position of Element in Sorted Array
- 153: Find Minimum in Rotated Sorted Array
- 162: Find Peak Element
- 540: Single Element in a Sorted Array
- 875: Koko Eating Bananas

### Stack & Queue Problems

#### Stack Applications

- 20: Valid Parentheses
- 71: Simplify Path
- 150: Evaluate Reverse Polish Notation
- 155: Min Stack
- 224: Basic Calculator
- 227: Basic Calculator II
- 739: Daily Temperatures
- 901: Online Stock Span
- 1047: Remove All Adjacent Duplicates In String

#### Queue Applications

- 1172: Dinner Plate Stacks
- 1472: Design Browser History

#### Monotonic Queue

- 239: Sliding Window Maximum

### Design Problems

- 146: LRU Cache
- 380: Insert Delete GetRandom O(1)
- 460: LFU Cache
- 706: Design HashMap
- 1472: Design Browser History

### Greedy Problems

- 55: Jump Game
- 134: Gas Station
- 435: Non-overlapping Intervals
- 621: Task Scheduler
- 763: Partition Labels
- 767: Reorganize String
- 881: Boats to Save People

### String Manipulation

- 8: String to Integer (atoi)
- 13: Roman to Integer
- 14: Longest Common Prefix
- 28: Find the Index of the First Occurrence in a String
- 49: Group Anagrams
- 67: Add Binary
- 151: Reverse Words in a String
- 242: Valid Anagram
- 387: First Unique Character in a String
- 443: String Compression

### Matrix Problems

- 36: Valid Sudoku
- 54: Spiral Matrix
- 73: Set Matrix Zeroes
- 130: Surrounded Regions
- 419: Battleships in a Board
- 733: Flood Fill

### Math & Bit Manipulation

- 7: Reverse Integer
- 9: Palindrome Number
- 12: Integer to Roman
- 13: Roman to Integer
- 169: Majority Element
- 202: Happy Number
- 273: Integer to English Words

## Problem-to-Pattern Matching Table

### Array & String Problems

| If you see this...                            | Consider this pattern... | Example problems                                                                                                                    | Key characteristics                                             |
| --------------------------------------------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Contiguous subarrays/substrings               | Sliding Window           | Max sum subarray of size K, Longest substring with K distinct chars, LC#3, LC#76, LC#438, LC#2251 (Number of Flowers in Full Bloom) | Fixed or variable size window that "slides" through array       |
| Need max/min/sum over window of elements      | Sliding Window           | Minimum size subarray with given sum, Fruit into baskets, LC#1358                                                                   | Often involves expanding/contracting window based on conditions |
| String pattern matching within another string | Sliding Window           | Find all anagrams in a string (LC#438), Permutation in string, Minimum window substring (LC#76)                                     | Track character frequencies within current window               |
| Repeated characters in window                 | Sliding Window           | Longest substring without repeating characters (LC#3), Longest repeating character replacement                                      | Use hash map/set to track seen characters                       |
| Paired elements in sorted array               | Two Pointers             | Two Sum (LC#1), Container with most water (LC#11), Trapping rain water (LC#42)                                                      | Start pointers at opposite ends, move based on comparison       |
| Remove duplicates                             | Two Pointers             | Remove duplicates from sorted array (LC#26), Remove element                                                                         | Fast/slow pointers tracking write position                      |
| Palindrome verification                       | Two Pointers             | Valid palindrome, Valid palindrome with removal allowance (LC#680)                                                                  | Pointers start at opposite ends, move inward                    |
| Triplets/quadruplets with constraints         | Two Pointers             | 3Sum (LC#15), 4Sum (LC#18), 3Sum closest, 3Sum smaller                                                                              | Sort array first, then use two pointers inside loop             |
| Merging sorted arrays                         | Two Pointers             | Merge sorted array (LC#88), Intersection of arrays                                                                                  | Maintain position in each array with separate pointers          |
| Max/min subarray sum                          | Kadane's Algorithm       | Maximum subarray (LC#53), Maximum product subarray (LC#152)                                                                         | Track current sum and max sum seen so far                       |
| Circular array max/min                        | Kadane's Algorithm       | Maximum circular subarray sum, Maximum absolute sum of any subarray (LC#1749)                                                       | Compare regular max sum vs total - min sum                      |
| Local vs global maxima                        | Kadane's Algorithm       | Best time to buy/sell stock (LC#121)                                                                                                | Reset when subarray becomes negative                            |
| Range queries                                 | Prefix Sums              | Range sum queries, Subarray sum equals K (LC#560), Continuous subarray sum                                                          | Precompute cumulative sums to make queries O(1)                 |
| Count subarrays with property                 | Prefix Sums              | Subarrays with sum divisible by K, Count nice subarrays, Contiguous array (LC#525)                                                  | Use (prefix_sum % k) frequency dictionary                       |
| Product of array except self                  | Prefix Products          | Product of array except self, Maximum product subarray (LC#152)                                                                     | Calculate prefix and suffix products, combine results           |
| Equilibrium index                             | Prefix Sums              | Find equilibrium index where left sum equals right sum, Find pivot index                                                            | Compare prefix sum with total sum                               |
| Minimum/maximum subsequence                   | Greedy + Array           | Increasing triplet subsequence, Longest increasing subsequence (LC#300)                                                             | Maintain minimum values seen so far                             |
| Array rotation problems                       | Array Manipulation       | Rotate array (LC#189), Search in rotated sorted array (LC#33)                                                                       | Identify pattern after rotation                                 |
| Majority element                              | Boyer-Moore Voting       | Majority element (LC#169), Majority element II                                                                                      | Cancel out non-majority elements                                |
| Cyclic sort                                   | In-place Sorting         | Missing number, Find all disappeared numbers (LC#448), LC#41 (First Missing Positive)                                               | Place each number in its correct position                       |

### Linked List Problems

| If you see this...                   | Consider this pattern...           | Example problems                                                                    | Key characteristics                              |
| ------------------------------------ | ---------------------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------ |
| Cycle detection                      | Fast & Slow Pointers               | Detect cycle in linked list (LC#141), Find cycle start (LC#142)                     | Fast pointer moves 2x speed of slow pointer      |
| Finding middle element               | Fast & Slow Pointers               | Middle of linked list, Reorder list (LC#143)                                        | Fast pointer moves 2x speed until it reaches end |
| Nth element from end                 | Fast & Slow Pointers               | Remove Nth node from end, Find Nth from end                                         | Maintain gap of N between pointers               |
| Linked list palindrome               | Fast & Slow Pointers               | Palindrome linked list (LC#234)                                                     | Find middle, reverse second half, compare        |
| Reverse linked list                  | Linked List Reversal               | Reverse linked list (LC#206), Reverse in K groups (LC#25)                           | Track prev, current, and next pointers           |
| Alternate K nodes                    | Linked List Reversal               | Reverse alternating K elements, Swap nodes in pairs, Reverse linked list II (LC#92) | Reverse specific segments conditionally          |
| Reorder linked list                  | Linked List Reversal + Fast & Slow | Reorder list (first half with second half reversed) (LC#143)                        | Split list, reverse second half, merge           |
| Intersection of linked lists         | Two Pointers                       | Intersection of two linked lists (LC#160)                                           | Align pointers by switching lists                |
| Linked list operations               | Dummy Head Node                    | Remove duplicates, Partition list                                                   | Use dummy head to simplify edge cases            |
| Copy linked list with random pointer | Hash Map                           | Copy list with random pointer (LC#138)                                              | Map original nodes to copied nodes               |

### Tree Problems

| If you see this...                 | Consider this pattern... | Example problems                                                                     | Key characteristics                                 |
| ---------------------------------- | ------------------------ | ------------------------------------------------------------------------------------ | --------------------------------------------------- |
| Tree node relationships            | Tree Traversal           | Common ancestor (LC#236, LC#235), Path sum (LC#112), Node distance                   | Choose traversal based on problem requirements      |
| Collect values from tree nodes     | Tree Traversal           | Level order traversal (LC#102), Zigzag traversal (LC#103), Right side view (LC#199)  | Process nodes based on specific order (pre/in/post) |
| Tree serialization/deserialization | Tree Traversal           | Serialize/deserialize binary tree (LC#297), Construct from preorder/inorder (LC#105) | Carefully encode tree structure in string format    |
| Binary tree path problems          | DFS + Backtracking       | Binary tree paths, Path sum II, Path sum III (LC#437)                                | Use recursion with path tracking                    |
| Tree transformation                | Tree Traversal           | Flatten binary tree to linked list, Convert sorted array to BST (LC#108)             | Choose traversal order that matches desired result  |
| Diameter/height problems           | Post-order Traversal     | Diameter of binary tree (LC#543), Maximum path sum (LC#124), Balanced binary tree    | Process child results before parent                 |
| Tree construction                  | Recursive Construction   | Construct binary tree from traversal (LC#105), Build tree from preorder/inorder      | Identify root, recursively build subtrees           |
| Symmetric tree verification        | Tree Traversal           | Symmetric tree, Same tree                                                            | Compare corresponding subtrees                      |
| Node distance problems             | LCA + Distance           | Distance between nodes, All nodes at distance K (LC#863)                             | First find LCA, then calculate distances            |
| Tree pruning                       | Post-order Traversal     | Trim BST, Binary tree pruning                                                        | Process child results before deciding parent action |

### Binary Search Tree Problems

| If you see this...    | Consider this pattern... | Example problems                                                  | Key characteristics                          |
| --------------------- | ------------------------ | ----------------------------------------------------------------- | -------------------------------------------- |
| Validate BST          | Binary Search Tree       | Validate binary search tree (LC#98), Convert sorted list to BST   | Use inorder traversal or min/max constraints |
| K-th smallest/largest | Binary Search Tree       | Kth smallest element in BST (LC#230), K closest values            | Inorder traversal gives sorted order         |
| Floor/ceiling values  | Binary Search Tree       | Closest value in BST, Successor/predecessor                       | Binary search with tracking closest          |
| BST construction      | Binary Search Tree       | Convert sorted array to BST (LC#108), Construct BST from preorder | Use binary search approach for balanced tree |
| BST modification      | Binary Search Tree       | Delete node in BST, Insert into BST                               | Preserve BST property during operations      |
| Range queries         | Binary Search Tree       | Range sum of BST, Count nodes in range                            | Use BST property to prune search paths       |
| BST iterator          | Controlled Traversal     | BST iterator, Flatten BST to sorted list                          | Implement inorder traversal iteratively      |

### Graph Problems

| If you see this...                  | Consider this pattern...    | Example problems                                                                            | Key characteristics                                      |
| ----------------------------------- | --------------------------- | ------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Tree/graph path finding             | DFS                         | Path sum, All paths from source to target (LC#797), Word search (LC#79)                     | Recursive exploration with backtracking                  |
| Exhaustive exploration              | DFS                         | Word search (LC#79), Islands count (LC#200), Max area of island (LC#695)                    | Mark visited nodes, explore all directions               |
| Topological sorting                 | DFS                         | Course schedule (LC#207), Course schedule II (LC#210), Task scheduling                      | Track visited nodes and process in post-order            |
| Shortest path (unweighted)          | BFS                         | Word ladder (LC#127), Shortest path in binary matrix, Rotting oranges (LC#994)              | Use queue to process nodes level by level                |
| Level-wise tree traversal           | BFS                         | Level order traversal (LC#102), Average of levels, Right side view (LC#199)                 | Process nodes level by level, track depth                |
| Minimum distance queries            | BFS                         | Distance from all buildings, Rot oranges (LC#994), 01 Matrix                                | Start BFS from multiple source points                    |
| Shortest path (weighted)            | Dijkstra's                  | Network delay time, Cheapest flights within K stops (LC#787), Path with maximum probability | Use priority queue to process nodes by distance          |
| Minimum spanning tree               | Prim's/Kruskal's            | Connecting cities with minimum cost, Min cost to connect all points                         | Build connected graph with minimum edge weight sum       |
| Connected components                | Union-Find                  | Number of islands II, Redundant connection, Accounts merge                                  | Track sets of connected components                       |
| Cycle detection in undirected graph | Union-Find                  | Graph valid tree, Detect cycle, Redundant connection                                        | Check if new edge connects already connected components  |
| Strongly connected components       | Kosaraju's/Tarjan's         | Critical connections, Find all critical edges                                               | Find components that remain connected after edge removal |
| Bipartite graph checking            | Graph Coloring              | Is graph bipartite, Possible bipartition                                                    | Color nodes with alternating colors                      |
| Graph representation                | Adjacency List/Matrix       | Clone graph, Find the town judge, Course schedule (LC#207)                                  | Choose representation based on graph density             |
| All pairs shortest path             | Floyd-Warshall              | Find city with smallest number of neighbors, Network delay time                             | Consider paths through intermediate vertices             |
| Maximum flow                        | Ford-Fulkerson/Edmonds-Karp | Maximum flow problems, Maximum bipartite matching                                           | Find augmenting paths to increase flow                   |
| Eulerian path                       | Eulerian Path Algorithm     | Reconstruct itinerary (LC#332), Valid arrangement of pairs                                  | Find path that uses each edge exactly once               |

### Dynamic Programming Problems

| If you see this...                | Consider this pattern...   | Example problems                                                                                       | Key characteristics                            |
| --------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------ | ---------------------------------------------- |
| Choice of items under constraints | 0/1 Knapsack               | Subset sum, Partition equal subset sum, Target sum                                                     | Can either include or exclude each item        |
| Target sum combinations           | 0/1 Knapsack               | Target sum, Coin change (limited supply), Partition to K equal sum subsets                             | Binary decision for each item                  |
| Unlimited supply of items         | Unbounded Knapsack         | Coin change (LC#322), Rod cutting, Integer break                                                       | Can reuse items multiple times                 |
| Ways to make change               | Unbounded Knapsack         | Coin change II (total ways), Combination sum IV                                                        | Count ways to reach target with reuse          |
| String comparison                 | Longest Common Subsequence | Edit distance (LC#72), Shortest common supersequence, Minimum ASCII delete sum                         | Build solution by comparing characters         |
| String transformations            | Longest Common Subsequence | Delete operations for two strings, Distinct subsequences                                               | Compare characters and build solution matrix   |
| Palindromic subsequence           | Longest Common Subsequence | Longest palindromic subsequence (LC#516), Palindromic substrings, Longest palindromic substring (LC#5) | Compare string with its reverse                |
| State depends on previous states  | Fibonacci Pattern          | Climbing stairs (LC#70), House robber (LC#198), Min cost climbing stairs                               | Current state depends on 1-2 previous states   |
| Jump game variations              | Fibonacci Pattern          | Jump game (LC#55), Min jumps to reach end (LC#45), Frog jump (LC#403)                                  | Current position depends on previous positions |
| Grid traversal                    | 2D DP                      | Unique paths (LC#62), Minimum path sum (LC#64), Dungeon game                                           | Build solution cell by cell                    |
| Stock buying problems             | State Machine DP           | Best time to buy/sell stock (LC#121) with cooldown/transaction limit                                   | Define states based on holding stock or not    |
| Longest increasing subsequence    | LIS Pattern                | Longest increasing subsequence (LC#300), Russian doll envelopes (LC#354)                               | Track longest sequence ending at each position |
| Matrix chain multiplication       | Interval DP                | Burst balloons, Optimal matrix multiplication                                                          | Solve for increasingly larger intervals        |
| Game theory                       | Minimax DP                 | Stone game, Predict the winner, Can I win                                                              | Maximize score difference between players      |
| Largest square/rectangle          | 2D DP                      | Maximal square, Maximal rectangle                                                                      | Track maximum size ending at each cell         |
| Word break problems               | String Segmentation DP     | Word break (LC#139), Word break II (LC#140)                                                            | Check if prefixes can be segmented             |

### Backtracking Problems

| If you see this...               | Consider this pattern... | Example problems                                                          | Key characteristics                                  |
| -------------------------------- | ------------------------ | ------------------------------------------------------------------------- | ---------------------------------------------------- |
| Generating all combinations      | Subsets/Backtracking     | Subsets (LC#78), Permutations, Combinations, Combination sum              | Build solution incrementally, backtrack on dead ends |
| Letter combinations              | Subsets/Backtracking     | Letter combinations of phone number (LC#17), Generate parentheses (LC#22) | Map characters to possible options                   |
| Complex constraints              | Constraint Satisfaction  | N-Queens (LC#51), Sudoku solver, Palindrome partitioning (LC#131)         | Check validity at each step                          |
| Maze/grid paths with constraints | Constraint Satisfaction  | Unique paths with obstacles, Word search (LC#79), Robot room cleaner      | Explore all directions while tracking visited cells  |
| String permutations              | Permutation Generation   | Letter case permutation, Next permutation (LC#31)                         | Systematically generate all arrangements             |
| Partition problems               | Backtracking             | Palindrome partitioning (LC#131), Restore IP addresses                    | Try different ways to break input into valid pieces  |
| Game solving                     | Minimax + Backtracking   | Tic-tac-toe, 24 Game                                                      | Consider all possible moves                          |
| String splitting                 | Backtracking             | Word break II (LC#140), Add spaces                                        | Try different ways to split input string             |

### Heap/Priority Queue Problems

| If you see this...          | Consider this pattern... | Example problems                                                                              | Key characteristics                                 |
| --------------------------- | ------------------------ | --------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Top K elements              | Heap                     | Kth largest element (LC#215), K closest points, Top K frequent (LC#347)                       | Use min-heap of size K for largest elements         |
| Smallest K elements         | Heap                     | Kth smallest element in sorted matrix                                                         | Use max-heap of size K for smallest elements        |
| Merge K sorted arrays/lists | Heap                     | Merge K sorted lists (LC#23), K-way merge, Smallest range (LC#632)                            | Min-heap to track smallest current elements         |
| Frequency-based problems    | Heap                     | Top K frequent elements (LC#347), Sort characters by frequency, Top K frequent words (LC#692) | Count frequencies, then use heap                    |
| Find median                 | Two Heaps                | Find median from data stream (LC#295), Sliding window median                                  | Min-heap for larger half, max-heap for smaller half |
| Sliding window statistics   | Two Heaps                | Sliding window median, Sliding window maximum (LC#239)                                        | Maintain elements within current window             |
| Scheduler problems          | Heap                     | Task scheduler (LC#621), Meeting rooms II (LC#253)                                            | Sort by time, then process with heap                |
| Stream processing           | Heap                     | Maximum frequency stack, Online median                                                        | Maintain statistics of stream data                  |

### Searching Problems

| If you see this...           | Consider this pattern... | Example problems                                                                   | Key characteristics                                         |
| ---------------------------- | ------------------------ | ---------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Sorted array search          | Binary Search            | Search in rotated array (LC#33), Find peak element (LC#162), Search range (LC#34)  | Repeatedly divide search space in half                      |
| Search space halving         | Binary Search            | Sqrt(x), Search 2D sorted matrix, Find minimum in rotated sorted array (LC#153)    | Identify which half contains answer                         |
| Minimize maximum value       | Binary Search            | Split array largest sum, Capacity to ship packages, Koko eating bananas (LC#875)   | Binary search on possible answers                           |
| Matrix search                | Binary Search            | Search 2D matrix, Search 2D matrix II, LC#48 (Rotate Image)                        | Use binary search on rows/columns                           |
| Rotated array search         | Binary Search            | Search in rotated sorted array I and II (LC#33), LC#189 (Rotate Array)             | Identify sorted half, search accordingly                    |
| Finding boundary             | Binary Search            | First bad version, H-index, Find the duplicate number                              | Find first/last occurrence of condition                     |
| Floating point binary search | Binary Search            | Find median of two sorted arrays (LC#4), Sqrt(x), LC#528 (Random Pick with Weight) | Similar to integer binary search but with decimal precision |

### Stack & Queue Problems

| If you see this...       | Consider this pattern... | Example problems                                                                                                                              | Key characteristics                           |
| ------------------------ | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| Monotonic stack problems | Stack                    | Next greater element, Daily temperatures (LC#739), Largest rectangle in histogram                                                             | Maintain decreasing/increasing order in stack |
| Expression evaluation    | Stack                    | Calculator (LC#224, LC#227), Evaluate reverse polish notation (LC#150), Basic calculator                                                      | Process operators based on precedence         |
| Parenthesis matching     | Stack                    | Valid parentheses (LC#20), Remove invalid parentheses, Minimum add to make valid (LC#921), LC#1249 (Minimum Remove to Make Valid Parentheses) | Use stack to track opening brackets           |
| String parsing           | Stack                    | Decode string, Remove duplicate letters, Simplify path (LC#71), LC#341 (Flatten Nested List Iterator)                                         | Process characters sequentially with stack    |
| Min/max stack            | Stack                    | Min stack (LC#155), Max stack, Largest rectangle in histogram                                                                                 | Track minimum/maximum at each position        |
| Queue implementation     | Queue                    | Implement queue using stacks (LC#232), Design circular queue                                                                                  | FIFO data structure                           |
| BFS implementation       | Queue                    | Level order traversal (LC#102), Word ladder (LC#127)                                                                                          | Process elements in order they're found       |
| Sliding window maximum   | Deque                    | Sliding window maximum (LC#239), Sliding window minimum                                                                                       | Maintain relevant elements in window          |
| Browser history/stack    | Deque                    | Design browser history (LC#1472), Max sliding window, LC#228 (Summary Ranges)                                                                 | Support operations from both ends             |

### Additional Pattern Categories

| If you see this...           | Consider this pattern... | Example problems                                                                                                                                                               | Key characteristics                                   |
| ---------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------- |
| Local -> global optimization | Greedy                   | Jump game (LC#55), Gas station (LC#134), Task scheduler (LC#621)                                                                                                               | Make locally optimal choice at each step              |
| Activity scheduling          | Greedy                   | Meeting rooms (LC#253), Non-overlapping intervals (LC#435), Minimum number of arrows                                                                                           | Sort by end time and select non-overlapping intervals |
| Optimal ordering             | Greedy                   | Queue reconstruction by height, Create maximum number, Reorganize string (LC#767)                                                                                              | Sort by specific criteria                             |
| Binary operations            | Bit Manipulation         | Single number, Counting bits, Sum of two integers, LC#3191 (Minimum Operations to Make Binary Array Elements Equal to One I)                                                   | Use logical operations (&,                            |
| XOR properties               | Bit Manipulation         | Maximum XOR of two numbers, Find the duplicate, Single number II                                                                                                               | Exploit XOR characteristics (a^a=0, a^0=a)            |
| Bit counting                 | Bit Manipulation         | Hamming distance, Number of 1 bits, Power of two                                                                                                                               | Count or check specific bits                          |
| Interval problems            | Interval Merging/Sorting | Merge intervals (LC#56), Insert interval, Meeting rooms (LC#253), Non-overlapping intervals (LC#435)                                                                           | Sort intervals, then process in order                 |
| Rabin-Karp algorithm         | String Hashing           | Repeated substring pattern, Implement strStr() (LC#28), Longest duplicate substring                                                                                            | Use rolling hash to compare substrings                |
| Unique elements              | Hash Set                 | Contains duplicate, Intersection of arrays (LC#349), Find the difference                                                                                                       | Track seen elements                                   |
| Element counting             | Hash Map                 | Two sum (LC#1), First unique character (LC#387), Longest substring without repeating characters (LC#3), LC#219 (Contains Duplicate II), LC#609 (Find Duplicate File in System) | Count occurrences or map elements to indices          |
| LRU/LFU cache                | Hash Map + Linked List   | LRU cache (LC#146), LFU cache (LC#460), All O(1) data structure, LC#359 (Logger Rate Limiter), LC#2622 (Cache With Time Limit)                                                 | Combine fast lookup with ordered access               |
| Sparse data representation   | Matrix Manipulation      | Sparse matrix multiplication, Diagonal traverse                                                                                                                                | Efficiently store and process sparse matrices         |
| Island problems              | Flood Fill/DFS/BFS       | Number of islands (LC#200), Making a large island, Surrounded regions (LC#130)                                                                                                 | Connected components in 2D grid                       |
| Mathematical series          | Math                     | Pascal's triangle (LC#118), Gray code, Pow(x, n)                                                                                                                               | Use mathematical properties and patterns              |
| Integer manipulation         | Math                     | Reverse integer (LC#7), Palindrome number (LC#9), String to integer (LC#8)                                                                                                     | Handle overflow, digit manipulation                   |
| Factorials and combinations  | Math                     | Factorial trailing zeroes, Unique paths (LC#62), Binomial coefficients                                                                                                         | Use combinatorial formulas                            |
| Random selection             | Reservoir Sampling       | Random node in a linked list, Random pick index, Random pick with weight (LC#528)                                                                                              | Select items from stream with equal probability       |
| Randomized algorithms        | Shuffle/Fisher-Yates     | Shuffle an array, Random pick with weight (LC#528)                                                                                                                             | Generate permutations with equal probability          |
| Strings with constraints     | State Machines           | Valid number, Regular expression matching, LC#68 (Text Justification)                                                                                                          | Process input character by character                  |
| Design problems              | Object-Oriented Design   | Design HashMap (LC#706), Design Twitter, Design browser history (LC#1472), LC#380 (Insert Delete GetRandom O(1)), LC#981 (Time Based Key-Value Store)                          | Combine appropriate data structures                   |
| Circular array               | Circular Array           | Circular array loop, Maximum sum circular subarray                                                                                                                             | Handle wrapping around array bounds                   |
| Boyer-Moore Voting           | Majority Element         | Majority element (LC#169), Majority element II                                                                                                                                 | Find elements appearing more than n/k times           |
| Topological sort             | Directed Acyclic Graph   | Course schedule (LC#207), Course schedule II (LC#210), Alien dictionary                                                                                                        | Process nodes with no incoming edges first            |
| Sliding window maximum       | Monotonic Queue          | Sliding window maximum (LC#239), Sliding window minimum                                                                                                                        | Maintain queue with decreasing/increasing elements    |

## Netflix LeetCode Problems by Pattern

This section categorizes common Netflix interview problems from LeetCode by their algorithmic patterns.

### Array Patterns

#### Two Pointers

- 3: Longest Substring Without Repeating Characters
- 88: Merge Sorted Array
- 121: Best Time to Buy and Sell Stock
- 219: Contains Duplicate II
- 228: Summary Ranges

#### Sliding Window

- 3: Longest Substring Without Repeating Characters
- 2251: Number of Flowers in Full Bloom

#### Kadane's Algorithm

- 121: Best Time to Buy and Sell Stock

#### Binary Search

- 33: Search in Rotated Sorted Array
- 215: Kth Largest Element in an Array (can be solved using QuickSelect which uses binary search principles)
- 528: Random Pick with Weight
- 2251: Number of Flowers in Full Bloom

#### Prefix Sums

- 121: Best Time to Buy and Sell Stock
- 2251: Number of Flowers in Full Bloom

#### Matrix Manipulation

- 48: Rotate Image
- 54: Spiral Matrix
- 79: Word Search

### Sorting & Intervals

#### Interval Merging

- 56: Merge Intervals
- 253: Meeting Rooms II

### Stack Problems

#### Stack Applications

- 20: Valid Parentheses
- 232: Implement Queue using Stacks
- 341: Flatten Nested List Iterator
- 739: Daily Temperatures
- 1249: Minimum Remove to Make Valid Parentheses

### Heap Patterns

#### Top K Elements

- 215: Kth Largest Element in an Array
- 347: Top K Frequent Elements
- 692: Top K Frequent Words

### Dynamic Programming

#### 1D Dynamic Programming

- 139: Word Break
- 322: Coin Change

### Tree & Graph Patterns

#### Graph Algorithms

- 210: Course Schedule II (Topological Sort)
- 332: Reconstruct Itinerary (Eulerian Path)
- 743: Network Delay Time (Dijkstra's Algorithm)

### Backtracking

#### Constraint Satisfaction

- 22: Generate Parentheses
- 79: Word Search

### Design Problems

#### LRU Cache

- 146: LRU Cache
- 359: Logger Rate Limiter
- 2622: Cache With Time Limit

#### Data Structure Design

- 380: Insert Delete GetRandom O(1)
- 981: Time Based Key-Value Store
- 2622: Cache With Time Limit

### Greedy Algorithms

#### Array Manipulation

- 41: First Missing Positive (partially greedy)
- 189: Rotate Array
- 1249: Minimum Remove to Make Valid Parentheses

### String Manipulation

- 68: Text Justification
- 609: Find Duplicate File in System

### Hash Table Applications

- 3: Longest Substring Without Repeating Characters
- 219: Contains Duplicate II
- 347: Top K Frequent Elements
- 359: Logger Rate Limiter
- 609: Find Duplicate File in System

### Bit Manipulation

- 3191: Minimum Operations to Make Binary Array Elements Equal to One I

## Problem-to-Pattern Matching Table
