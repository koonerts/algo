# Algorithm Pattern Identification Guide

This guide helps you identify which algorithm pattern to use based on problem characteristics. For each pattern, we provide:

1. **How to Identify:** Key signs that suggest using this pattern
2. **Example Problem Types:** Typical problems that use this pattern
3. **Time & Space Complexity:** General complexity characteristics

> **New Feature:** You can now use the algorithm migration tool to convert implementations between languages. Install it with `./migrate-installer.sh` and run `algo-migrate --help` for usage instructions. Example pattern implementations are available in `py-algo/example_patterns/`.

---

## Array Patterns

### Sliding Window

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

### Breadth-First Search (BFS)

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

**Example Problem Types:**

- Network routing
- GPS navigation
- Flight scheduling

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

## Problem-to-Pattern Matching Table

### Array & String Problems

| If you see this...                                      | Consider this pattern...               | Example problems                                  | Key characteristics |
| ------------------------------------------------------- | -------------------------------------- | ------------------------------------------------- | ------------------ |
| Contiguous subarrays/substrings                         | Sliding Window                         | Max sum subarray of size K, Longest substring with K distinct chars | Fixed or variable size window that "slides" through array |
| Need max/min/sum over window of elements                | Sliding Window                         | Minimum size subarray with given sum, Fruit into baskets | Often involves expanding/contracting window based on conditions |
| String pattern matching within another string           | Sliding Window                         | Find all anagrams in a string, Permutation in string, Minimum window substring | Track character frequencies within current window |
| Repeated characters in window                           | Sliding Window                         | Longest substring without repeating characters, Longest repeating character replacement | Use hash map/set to track seen characters |
| Paired elements in sorted array                         | Two Pointers                           | Two Sum, Container with most water, Trapping rain water | Start pointers at opposite ends, move based on comparison |
| Remove duplicates                                       | Two Pointers                           | Remove duplicates from sorted array, Remove element | Fast/slow pointers tracking write position |
| Palindrome verification                                 | Two Pointers                           | Valid palindrome, Valid palindrome with removal allowance | Pointers start at opposite ends, move inward |
| Triplets/quadruplets with constraints                   | Two Pointers                           | 3Sum, 4Sum, 3Sum closest, 3Sum smaller | Sort array first, then use two pointers inside loop |
| Merging sorted arrays                                   | Two Pointers                           | Merge sorted array, Intersection of arrays | Maintain position in each array with separate pointers |
| Max/min subarray sum                                    | Kadane's Algorithm                     | Maximum subarray, Maximum product subarray | Track current sum and max sum seen so far |
| Circular array max/min                                  | Kadane's Algorithm                     | Maximum circular subarray sum | Compare regular max sum vs total - min sum |
| Local vs global maxima                                  | Kadane's Algorithm                     | Best time to buy/sell stock | Reset when subarray becomes negative |
| Range queries                                           | Prefix Sums                            | Range sum queries, Subarray sum equals K, Continuous subarray sum | Precompute cumulative sums to make queries O(1) |
| Count subarrays with property                           | Prefix Sums                            | Subarrays with sum divisible by K, Count nice subarrays | Use (prefix_sum % k) frequency dictionary |
| Product of array except self                            | Prefix Products                        | Product of array except self, Maximum product subarray | Calculate prefix and suffix products, combine results |
| Equilibrium index                                       | Prefix Sums                            | Find equilibrium index where left sum equals right sum, Find pivot index | Compare prefix sum with total sum |
| Minimum/maximum subsequence                             | Greedy + Array                         | Increasing triplet subsequence, Longest increasing subsequence | Maintain minimum values seen so far |
| Array rotation problems                                 | Array Manipulation                     | Rotate array, Search in rotated sorted array | Identify pattern after rotation |
| Majority element                                        | Boyer-Moore Voting                     | Majority element, Majority element II | Cancel out non-majority elements |
| Cyclic sort                                             | In-place Sorting                       | Missing number, Find all disappeared numbers | Place each number in its correct position |

### Linked List Problems

| If you see this...                                      | Consider this pattern...               | Example problems                                  | Key characteristics |
| ------------------------------------------------------- | -------------------------------------- | ------------------------------------------------- | ------------------ |
| Cycle detection                                         | Fast & Slow Pointers                   | Detect cycle in linked list, Find cycle start | Fast pointer moves 2x speed of slow pointer |
| Finding middle element                                  | Fast & Slow Pointers                   | Middle of linked list, Reorder list | Fast pointer moves 2x speed until it reaches end |
| Nth element from end                                    | Fast & Slow Pointers                   | Remove Nth node from end, Find Nth from end | Maintain gap of N between pointers |
| Linked list palindrome                                  | Fast & Slow Pointers                   | Palindrome linked list | Find middle, reverse second half, compare |
| Reverse linked list                                     | Linked List Reversal                   | Reverse linked list, Reverse in K groups | Track prev, current, and next pointers |
| Alternate K nodes                                       | Linked List Reversal                   | Reverse alternating K elements, Swap nodes in pairs | Reverse specific segments conditionally |
| Reorder linked list                                     | Linked List Reversal + Fast & Slow     | Reorder list (first half with second half reversed) | Split list, reverse second half, merge |
| Intersection of linked lists                            | Two Pointers                           | Intersection of two linked lists | Align pointers by switching lists |
| Linked list operations                                  | Dummy Head Node                        | Remove duplicates, Partition list | Use dummy head to simplify edge cases |
| Copy linked list with random pointer                    | Hash Map                               | Copy list with random pointer | Map original nodes to copied nodes |

### Tree Problems

| If you see this...                                      | Consider this pattern...               | Example problems                                  | Key characteristics |
| ------------------------------------------------------- | -------------------------------------- | ------------------------------------------------- | ------------------ |
| Tree node relationships                                 | Tree Traversal                         | Common ancestor, Path sum, Node distance | Choose traversal based on problem requirements |
| Collect values from tree nodes                          | Tree Traversal                         | Level order traversal, Zigzag traversal, Right side view | Process nodes based on specific order (pre/in/post) |
| Tree serialization/deserialization                      | Tree Traversal                         | Serialize/deserialize binary tree, Construct from preorder/inorder | Carefully encode tree structure in string format |
| Binary tree path problems                               | DFS + Backtracking                     | Binary tree paths, Path sum II, Sum root to leaf numbers | Use recursion with path tracking |
| Tree transformation                                     | Tree Traversal                         | Flatten binary tree to linked list, Convert sorted array to BST | Choose traversal order that matches desired result |
| Diameter/height problems                                | Post-order Traversal                   | Diameter of binary tree, Maximum path sum, Balanced binary tree | Process child results before parent |
| Tree construction                                       | Recursive Construction                 | Construct binary tree from traversal, Build tree from preorder/inorder | Identify root, recursively build subtrees |
| Symmetric tree verification                             | Tree Traversal                         | Symmetric tree, Same tree | Compare corresponding subtrees |
| Node distance problems                                  | LCA + Distance                         | Distance between nodes, All nodes at distance K | First find LCA, then calculate distances |
| Tree pruning                                            | Post-order Traversal                   | Trim BST, Binary tree pruning | Process child results before deciding parent action |

### Binary Search Tree Problems

| If you see this...                                      | Consider this pattern...               | Example problems                                  | Key characteristics |
| ------------------------------------------------------- | -------------------------------------- | ------------------------------------------------- | ------------------ |
| Validate BST                                            | Binary Search Tree                     | Validate binary search tree, Convert sorted list to BST | Use inorder traversal or min/max constraints |
| K-th smallest/largest                                   | Binary Search Tree                     | Kth smallest element in BST, K closest values | Inorder traversal gives sorted order |
| Floor/ceiling values                                    | Binary Search Tree                     | Closest value in BST, Successor/predecessor | Binary search with tracking closest |
| BST construction                                        | Binary Search Tree                     | Convert sorted array to BST, Construct BST from preorder | Use binary search approach for balanced tree |
| BST modification                                        | Binary Search Tree                     | Delete node in BST, Insert into BST | Preserve BST property during operations |
| Range queries                                           | Binary Search Tree                     | Range sum of BST, Count nodes in range | Use BST property to prune search paths |
| BST iterator                                            | Controlled Traversal                   | BST iterator, Flatten BST to sorted list | Implement inorder traversal iteratively |

### Graph Problems

| If you see this...                                      | Consider this pattern...               | Example problems                                  | Key characteristics |
| ------------------------------------------------------- | -------------------------------------- | ------------------------------------------------- | ------------------ |
| Tree/graph path finding                                 | DFS                                    | Path sum, All paths from source to target, Word search | Recursive exploration with backtracking |
| Exhaustive exploration                                  | DFS                                    | Word search, Islands count, Max area of island | Mark visited nodes, explore all directions |
| Topological sorting                                     | DFS                                    | Course schedule, Alien dictionary, Task scheduling | Track visited nodes and process in post-order |
| Shortest path (unweighted)                              | BFS                                    | Word ladder, Shortest path in binary matrix, Rotting oranges | Use queue to process nodes level by level |
| Level-wise tree traversal                               | BFS                                    | Level order traversal, Average of levels, Right side view | Process nodes level by level, track depth |
| Minimum distance queries                                | BFS                                    | Distance from all buildings, Rot oranges, 01 Matrix | Start BFS from multiple source points |
| Shortest path (weighted)                                | Dijkstra's                             | Network delay time, Cheapest flights within K stops, Path with maximum probability | Use priority queue to process nodes by distance |
| Minimum spanning tree                                   | Prim's/Kruskal's                       | Connecting cities with minimum cost, Min cost to connect all points | Build connected graph with minimum edge weight sum |
| Connected components                                    | Union-Find                             | Number of islands II, Redundant connection, Accounts merge | Track sets of connected components |
| Cycle detection in undirected graph                     | Union-Find                             | Graph valid tree, Detect cycle, Redundant connection | Check if new edge connects already connected components |
| Strongly connected components                           | Kosaraju's/Tarjan's                    | Critical connections, Find all critical edges | Find components that remain connected after edge removal |
| Bipartite graph checking                                | Graph Coloring                         | Is graph bipartite, Possible bipartition | Color nodes with alternating colors |
| Graph representation                                    | Adjacency List/Matrix                  | Clone graph, Find the town judge, Course schedule | Choose representation based on graph density |
| All pairs shortest path                                 | Floyd-Warshall                         | Find city with smallest number of neighbors, Network delay time | Consider paths through intermediate vertices |
| Maximum flow                                            | Ford-Fulkerson/Edmonds-Karp            | Maximum flow problems, Maximum bipartite matching | Find augmenting paths to increase flow |
| Eulerian path                                           | Eulerian Path Algorithm                | Reconstruct itinerary, Valid arrangement of pairs | Find path that uses each edge exactly once |

### Dynamic Programming Problems

| If you see this...                                      | Consider this pattern...               | Example problems                                  | Key characteristics |
| ------------------------------------------------------- | -------------------------------------- | ------------------------------------------------- | ------------------ |
| Choice of items under constraints                       | 0/1 Knapsack                           | Subset sum, Partition equal subset sum, Target sum | Can either include or exclude each item |
| Target sum combinations                                 | 0/1 Knapsack                           | Target sum, Coin change (limited supply), Partition to K equal sum subsets | Binary decision for each item |
| Unlimited supply of items                               | Unbounded Knapsack                     | Coin change, Rod cutting, Integer break | Can reuse items multiple times |
| Ways to make change                                     | Unbounded Knapsack                     | Coin change II (total ways), Combination sum IV | Count ways to reach target with reuse |
| String comparison                                       | Longest Common Subsequence             | Edit distance, Shortest common supersequence, Minimum ASCII delete sum | Build solution by comparing characters |
| String transformations                                  | Longest Common Subsequence             | Delete operations for two strings, Distinct subsequences | Compare characters and build solution matrix |
| Palindromic subsequence                                 | Longest Common Subsequence             | Longest palindromic subsequence, Palindromic substrings | Compare string with its reverse |
| State depends on previous states                        | Fibonacci Pattern                      | Climbing stairs, House robber, Min cost climbing stairs | Current state depends on 1-2 previous states |
| Jump game variations                                    | Fibonacci Pattern                      | Jump game, Min jumps to reach end, Frog jump | Current position depends on previous positions |
| Grid traversal                                          | 2D DP                                  | Unique paths, Minimum path sum, Dungeon game | Build solution cell by cell |
| Stock buying problems                                   | State Machine DP                       | Best time to buy/sell stock with cooldown/transaction limit | Define states based on holding stock or not |
| Longest increasing subsequence                          | LIS Pattern                            | Longest increasing subsequence, Russian doll envelopes | Track longest sequence ending at each position |
| Matrix chain multiplication                             | Interval DP                            | Burst balloons, Optimal matrix multiplication | Solve for increasingly larger intervals |
| Game theory                                             | Minimax DP                             | Stone game, Predict the winner, Can I win | Maximize score difference between players |
| Largest square/rectangle                                | 2D DP                                  | Maximal square, Maximal rectangle | Track maximum size ending at each cell |
| Word break problems                                     | String Segmentation DP                 | Word break, Word break II | Check if prefixes can be segmented |

### Backtracking Problems

| If you see this...                                      | Consider this pattern...               | Example problems                                  | Key characteristics |
| ------------------------------------------------------- | -------------------------------------- | ------------------------------------------------- | ------------------ |
| Generating all combinations                             | Subsets/Backtracking                   | Subsets, Permutations, Combinations, Combination sum | Build solution incrementally, backtrack on dead ends |
| Letter combinations                                     | Subsets/Backtracking                   | Letter combinations of phone number, Generate parentheses | Map characters to possible options |
| Complex constraints                                     | Constraint Satisfaction                 | N-Queens, Sudoku solver, Palindrome partitioning | Check validity at each step |
| Maze/grid paths with constraints                        | Constraint Satisfaction                 | Unique paths with obstacles, Word search, Robot room cleaner | Explore all directions while tracking visited cells |
| String permutations                                     | Permutation Generation                  | Letter case permutation, Next permutation | Systematically generate all arrangements |
| Partition problems                                      | Backtracking                           | Palindrome partitioning, Restore IP addresses | Try different ways to break input into valid pieces |
| Game solving                                            | Minimax + Backtracking                 | Tic-tac-toe, 24 Game | Consider all possible moves |
| String splitting                                        | Backtracking                           | Word break II, Add spaces | Try different ways to split input string |

### Heap/Priority Queue Problems

| If you see this...                                      | Consider this pattern...               | Example problems                                  | Key characteristics |
| ------------------------------------------------------- | -------------------------------------- | ------------------------------------------------- | ------------------ |
| Top K elements                                          | Heap                                   | Kth largest element, K closest points, Top K frequent | Use min-heap of size K for largest elements |
| Smallest K elements                                     | Heap                                   | Kth smallest element in sorted matrix | Use max-heap of size K for smallest elements |
| Merge K sorted arrays/lists                             | Heap                                   | Merge K sorted lists, K-way merge, Smallest range | Min-heap to track smallest current elements |
| Frequency-based problems                                | Heap                                   | Top K frequent elements, Sort characters by frequency | Count frequencies, then use heap |
| Find median                                             | Two Heaps                              | Find median from data stream, Sliding window median | Min-heap for larger half, max-heap for smaller half |
| Sliding window statistics                               | Two Heaps                              | Sliding window median, Sliding window maximum | Maintain elements within current window |
| Scheduler problems                                      | Heap                                   | Task scheduler, Meeting rooms II | Sort by time, then process with heap |
| Stream processing                                       | Heap                                   | Maximum frequency stack, Online median | Maintain statistics of stream data |

### Searching Problems

| If you see this...                                      | Consider this pattern...               | Example problems                                  | Key characteristics |
| ------------------------------------------------------- | -------------------------------------- | ------------------------------------------------- | ------------------ |
| Sorted array search                                     | Binary Search                          | Search in rotated array, Find peak element, Search range | Repeatedly divide search space in half |
| Search space halving                                    | Binary Search                          | Sqrt(x), Search 2D sorted matrix, Find minimum in rotated sorted array | Identify which half contains answer |
| Minimize maximum value                                  | Binary Search                          | Split array largest sum, Capacity to ship packages, Koko eating bananas | Binary search on possible answers |
| Matrix search                                           | Binary Search                          | Search 2D matrix, Search 2D matrix II | Use binary search on rows/columns |
| Rotated array search                                    | Binary Search                          | Search in rotated sorted array I and II | Identify sorted half, search accordingly |
| Finding boundary                                        | Binary Search                          | First bad version, H-index, Find the duplicate number | Find first/last occurrence of condition |
| Floating point binary search                            | Binary Search                          | Find median of two sorted arrays, Sqrt(x) | Similar to integer binary search but with decimal precision |

### Stack & Queue Problems

| If you see this...                                      | Consider this pattern...               | Example problems                                  | Key characteristics |
| ------------------------------------------------------- | -------------------------------------- | ------------------------------------------------- | ------------------ |
| Monotonic stack problems                                | Stack                                  | Next greater element, Daily temperatures, Largest rectangle in histogram | Maintain decreasing/increasing order in stack |
| Expression evaluation                                   | Stack                                  | Calculator, Evaluate reverse polish notation, Basic calculator | Process operators based on precedence |
| Parenthesis matching                                    | Stack                                  | Valid parentheses, Remove invalid parentheses, Minimum add to make valid | Use stack to track opening brackets |
| String parsing                                          | Stack                                  | Decode string, Remove duplicate letters, Simplify path | Process characters sequentially with stack |
| Min/max stack                                           | Stack                                  | Min stack, Max stack, Largest rectangle in histogram | Track minimum/maximum at each position |
| Queue implementation                                    | Queue                                  | Implement queue using stacks, Design circular queue | FIFO data structure |
| BFS implementation                                      | Queue                                  | Level order traversal, Word ladder | Process elements in order they're found |
| Sliding window maximum                                  | Deque                                  | Sliding window maximum, Sliding window minimum | Maintain relevant elements in window |
| Browser history/stack                                   | Deque                                  | Design browser history, Max sliding window | Support operations from both ends |

### Additional Pattern Categories

| If you see this...                                      | Consider this pattern...               | Example problems                                  | Key characteristics |
| ------------------------------------------------------- | -------------------------------------- | ------------------------------------------------- | ------------------ |
| Local -> global optimization                            | Greedy                                 | Jump game, Gas station, Task scheduler | Make locally optimal choice at each step |
| Activity scheduling                                     | Greedy                                 | Meeting rooms, Non-overlapping intervals, Minimum number of arrows | Sort by end time and select non-overlapping intervals |
| Optimal ordering                                        | Greedy                                 | Queue reconstruction by height, Create maximum number | Sort by specific criteria |
| Binary operations                                       | Bit Manipulation                       | Single number, Counting bits, Sum of two integers | Use logical operations (&, |, ^, ~, <<, >>) |
| XOR properties                                          | Bit Manipulation                       | Maximum XOR of two numbers, Find the duplicate, Single number II | Exploit XOR characteristics (a^a=0, a^0=a) |
| Bit counting                                            | Bit Manipulation                       | Hamming distance, Number of 1 bits, Power of two | Count or check specific bits |
| Interval problems                                       | Interval Merging/Sorting               | Merge intervals, Insert interval, Meeting rooms, Non-overlapping intervals | Sort intervals, then process in order |
| Rabin-Karp algorithm                                    | String Hashing                         | Repeated substring pattern, Implement strStr(), Longest duplicate substring | Use rolling hash to compare substrings |
| Unique elements                                         | Hash Set                               | Contains duplicate, Intersection of arrays, Find the difference | Track seen elements |
| Element counting                                        | Hash Map                               | Two sum, First unique character, Longest substring without repeating characters | Count occurrences or map elements to indices |
| LRU/LFU cache                                           | Hash Map + Linked List                 | LRU cache, LFU cache, All O(1) data structure | Combine fast lookup with ordered access |
| Sparse data representation                              | Matrix Manipulation                    | Sparse matrix multiplication, Diagonal traverse | Efficiently store and process sparse matrices |
| Island problems                                         | Flood Fill/DFS/BFS                     | Number of islands, Making a large island, Surrounded regions | Connected components in 2D grid |
| Mathematical series                                     | Math                                   | Pascal's triangle, Gray code, Pow(x, n) | Use mathematical properties and patterns |
| Integer manipulation                                    | Math                                   | Reverse integer, Palindrome number, String to integer | Handle overflow, digit manipulation |
| Factorials and combinations                             | Math                                   | Factorial trailing zeroes, Unique paths, Binomial coefficients | Use combinatorial formulas |
| Random selection                                        | Reservoir Sampling                     | Random node in a linked list, Random pick index | Select items from stream with equal probability |
| Randomized algorithms                                   | Shuffle/Fisher-Yates                   | Shuffle an array, Random pick with weight | Generate permutations with equal probability |
| Strings with constraints                                | State Machines                         | Valid number, Regular expression matching | Process input character by character |
| Design problems                                         | Object-Oriented Design                 | Design HashMap, Design Twitter, Design search autocomplete | Combine appropriate data structures |
| Circular array                                          | Circular Array                         | Circular array loop, Maximum sum circular subarray | Handle wrapping around array bounds |
| Boyer-Moore Voting                                      | Majority Element                       | Majority element, Majority element II | Find elements appearing more than n/k times |
| Topological sort                                        | Directed Acyclic Graph                 | Course schedule, Alien dictionary | Process nodes with no incoming edges first |
| Sliding window maximum                                  | Monotonic Queue                        | Sliding window maximum, Sliding window minimum | Maintain queue with decreasing/increasing elements |
