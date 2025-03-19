# Ready-to-Use Algorithm Learning Activities

These activities are ready to use right now without physical materials. Just follow the instructions and use these digital resources.

## 1. Algorithm Pattern Recognition Flash Cards

Use these digital flash cards to practice identifying algorithm patterns from problem descriptions.

### Instructions:

1. Read the problem description
2. Try to identify the algorithm pattern before revealing the answer
3. Track how many you get correct

### Flash Cards:

**Problem 1:**

```python-repl
Find the maximum sum of a contiguous subarray within an array of numbers.

Example:
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6 (the subarray [4, -1, 2, 1])
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Kadane's Algorithm**

  **Why**: This is the classic maximum subarray problem that Kadane's algorithm is designed to solve in O(n) time.

  **Key Insight**: At each position, you need to decide whether to start a new subarray or extend the existing one.

</details>

**Problem 2:**

```python-repl
Find a pair of numbers in a sorted array that add up to a target sum.

Example:
Input: [1, 3, 4, 5, 7, 10, 11], target=9
Output: [3, 6] (indices of numbers 4 and 5)
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Two Pointers**

  **Why**: With a sorted array and target sum, two pointers from opposite ends is optimal.

  **Key Insight**: When sum is too small, increase left pointer; when too large, decrease right pointer.

</details>

**Problem 3:**

```python-repl
Find the longest substring with at most K distinct characters.

Example:
Input: "eceba", K=2
Output: 3 ("ece")
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Sliding Window (Variable Size)**

  **Why**: We need to find a contiguous substring that meets a constraint.

  **Key Insight**: Expand window until constraint violation, then contract from left.

</details>

**Problem 4:**

```python-repl
Search for a target in a rotated sorted array.

Example:
Input: [4, 5, 6, 7, 0, 1, 2], target=0
Output: 4 (index of target)
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Modified Binary Search**

  **Why**: Despite rotation, we can determine which half is sorted and whether target lies in that half.

  **Key Insight**: Check which half is sorted, then determine if target is in that half.

</details>

**Problem 5:**

```python-repl
Check if a linked list has a cycle.

Example:
Input: A->B->C->D->B (pointing back to B)
Output: true
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Fast & Slow Pointers**

  **Why**: Using two pointers at different speeds will detect a cycle when they meet.

  **Key Insight**: If there's a cycle, a fast pointer will eventually catch up to a slow pointer.

</details>

**Problem 6:**

```python-repl
Find all subsets of a set of distinct integers.

Example:
Input: [1, 2, 3]
Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Backtracking - Subsets**

  **Why**: We need to generate all possible combinations.

  **Key Insight**: For each element, we have two choices - include it or exclude it.

</details>

**Problem 7:**

```python-repl
Given a grid of 1s (land) and 0s (water), count the number of islands.

Example:
Input: [
  [1, 1, 0, 0, 0],
  [1, 1, 0, 0, 0],
  [0, 0, 1, 0, 0],
  [0, 0, 0, 1, 1]
]
Output: 3
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: DFS/BFS on Matrix**

  **Why**: We need to identify connected components in a graph.

  **Key Insight**: Each island is a connected component that can be fully explored from any of its cells.

</details>

**Problem 8:**

```python-repl
Find the median of two sorted arrays.

Example:
Input: [1, 3], [2]
Output: 2.0
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Binary Search on Arrays**

  **Why**: Efficient solution requires binary search on the smaller array to find the partition point.

  **Key Insight**: The problem reduces to finding the correct partition that divides all elements into two equal halves.

</details>

**Problem 9:**

```python-repl
Determine if a string can be segmented into words from a dictionary.

Example:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Dynamic Programming**

  **Why**: Optimal substructure - if we can segment up to position i, we only need to check if the remaining substring is a word.

  **Key Insight**: Build a DP array where dp[i] indicates if the substring up to position i can be segmented.

</details>

**Problem 10:**

```python-repl
Design a data structure that supports insert, remove, and getRandom operations in O(1) time.

Example:
insert(1)
insert(2)
getRandom() // should return 1 or 2 with equal probability
remove(1)
getRandom() // should return 2
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Hash Table + Array**

  **Why**: Combination of data structures to achieve O(1) for all operations.

  **Key Insight**: Use array for O(1) random access, hash table for O(1) lookup, and array swap trick for O(1) removal.

</details>

**Problem 11:**

```python-repl
Given a knapsack with capacity W and a list of items with weights and values, determine the maximum value that can be obtained by selecting items such that their total weight doesn't exceed W. Each item can only be selected once.

Example:
Input: capacity = 10, weights = [2, 3, 5, 7], values = [1, 5, 2, 4]
Output: 9 (by selecting items with weights 3 and 7, values 5 and 4)
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: 0/1 Knapsack (Dynamic Programming)**

  **Why**: Need to make binary decisions (include/exclude) for each item while maximizing value under a weight constraint.

  **Key Insight**: Build a 2D DP table where dp[i][w] represents the maximum value achievable with first i items and weight limit w.

</details>

**Problem 12:**

```python-repl
Given a set of coins with different denominations and a total amount of money, find the minimum number of coins needed to make up that amount. You may assume you have an infinite supply of each coin.

Example:
Input: coins = [1, 2, 5], amount = 11
Output: 3 (5 + 5 + 1)
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Unbounded Knapsack**

  **Why**: Items (coins) can be used multiple times to achieve a target sum while optimizing a value (minimum coins).

  **Key Insight**: Use DP where each state represents the minimum coins needed for a specific amount, and transitions consider using each coin denomination repeatedly.

</details>

**Problem 13:**

```python-repl
Given two strings text1 and text2, return the length of their longest common subsequence. A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example:
Input: text1 = "abcde", text2 = "ace" 
Output: 3 (The longest common subsequence is "ace")
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Longest Common Subsequence (LCS)**

  **Why**: Need to compare and find common elements between two sequences while maintaining their relative order.

  **Key Insight**: Use a 2D DP table to build the solution character by character, considering two options at each step: include the character if matching or skip it.

</details>

**Problem 14:**

```python-repl
You are climbing a staircase. It takes n steps to reach the top. Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example:
Input: n = 3
Output: 3 (1+1+1, 1+2, 2+1)
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Fibonacci Sequence**

  **Why**: The number of ways to reach step n depends on ways to reach steps n-1 and n-2, forming a recursive relation.

  **Key Insight**: Each step can be reached from either one or two steps before, creating the recurrence relation f(n) = f(n-1) + f(n-2).

</details>

**Problem 15:**

```python-repl
Design and implement a data structure for a prefix tree (Trie) that supports insert, search, and startsWith operations.

Example:
insert("apple")
search("apple")   // returns true
search("app")     // returns false
startsWith("app") // returns true
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Trie (Prefix Tree)**

  **Why**: Efficient storage and retrieval of words with prefix matching capabilities.

  **Key Insight**: Use a tree structure where each node represents a character, and paths from root to nodes form words or prefixes.

</details>

**Problem 16:**

```python-repl
Given an array of meeting time intervals where intervals[i] = [start_i, end_i], determine the minimum number of conference rooms required.

Example:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Heap (Priority Queue)**

  **Why**: Need to track the ending times of ongoing meetings to determine resource allocation.

  **Key Insight**: Sort intervals by start time and use a min-heap to track the earliest ending meeting room, allocating a new room only when no existing room is available.

</details>

**Problem 17:**

```python-repl
Implement a data structure that can efficiently find the median from a stream of numbers. The median is the middle value in an ordered list of numbers.

Example:
addNum(1)
addNum(2)
findMedian() // returns 1.5
addNum(3)
findMedian() // returns 2
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Two Heaps**

  **Why**: Need to efficiently maintain the median as new elements arrive.

  **Key Insight**: Use a max-heap for the smaller half and a min-heap for the larger half, ensuring they remain balanced to easily calculate the median.

</details>

**Problem 18:**

```python-repl
Given a network of nodes represented as a weighted graph, find the shortest time it takes for a signal to reach all nodes from a given source node.

Example:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2 (Time to reach node 1 is 1, node 3 is 1, node 4 is 2)
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Dijkstra's Algorithm**

  **Why**: Finding shortest paths in a weighted graph with non-negative weights.

  **Key Insight**: Use a priority queue to greedily explore the closest unvisited nodes first, updating distances as shorter paths are found.

</details>

**Problem 19:**

```python-repl
There are n computers numbered from 0 to n-1 connected by ethernet cables forming a network where connections[i] = [a, b] represents a connection between computers a and b. Determine if all computers can communicate with each other, either directly or indirectly.

Example:
Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: false (Computer 3 cannot communicate with others)
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Union-Find (Disjoint Set)**

  **Why**: Need to track connected components and determine if all elements belong to the same component.

  **Key Insight**: Use union-find data structure to efficiently merge connected components and count distinct groups.

</details>

**Problem 20:**

```python-repl
Given a set of activities with start and finish times, select the maximum number of activities that can be performed by a single person, assuming the person can only work on a single activity at a time.

Example:
Input: start = [1, 3, 0, 5, 8, 5], finish = [2, 4, 6, 7, 9, 9]
Output: 4 (Activities at index 0, 1, 3, 4)
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Greedy Algorithm**

  **Why**: Local optimal choice (selecting activity that ends earliest) leads to global optimum.

  **Key Insight**: Sort activities by finish time and always select the next compatible activity that ends earliest.

</details>

**Problem 21:**

```python-repl
Given an array where every element appears twice except for one element which appears only once, find that single element.

Example:
Input: [2, 2, 1, 3, 3, 4, 4]
Output: 1
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Bit Manipulation**

  **Why**: XOR operations allow efficient cancellation of duplicate numbers.

  **Key Insight**: XOR of all elements will result in the single number because a⊕a=0 and a⊕0=a.

</details>

**Problem 22:**

```python-repl
Given a collection of intervals, merge all overlapping intervals.

Example:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Interval Merging**

  **Why**: Need to identify and combine overlapping intervals.

  **Key Insight**: Sort intervals by start time, then iterate through them, merging when current interval overlaps with the previous merged interval.

</details>

**Problem 23:**

```python-repl
There are a total of n courses you have to take, labeled from 0 to n-1. Some courses have prerequisite courses that must be completed first. Determine if it's possible to finish all courses.

Example:
Input: n = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: true (One possible order: 0,1,2,3)
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Topological Sort**

  **Why**: Need to find a valid ordering of nodes in a directed graph that respects dependencies.

  **Key Insight**: Use DFS or BFS to detect cycles and find a valid ordering. If a cycle exists, no valid ordering is possible.

</details>

**Problem 24:**

```python-repl
Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all elements of nums except nums[i].

Example:
Input: [1,2,3,4]
Output: [24,12,8,6]
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Prefix/Suffix Products**

  **Why**: Efficiently compute products that depend on all elements except the current one.

  **Key Insight**: Calculate products from left to right (prefix) and right to left (suffix), then multiply corresponding prefix and suffix for each position.

</details>

**Problem 25:**

```python-repl
Given a 2D grid of '1's (land) and '0's (water), count the number of islands (connected components of land).

Example:
Input: [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Flood Fill (DFS/BFS on Matrix)**

  **Why**: Need to identify and count connected components in a grid.

  **Key Insight**: Use DFS or BFS to explore each land cell and mark connected cells as visited to avoid counting them again.

</details>

### Netflix Interview Problem Flash Cards

The following flash cards contain common problems from Netflix interviews. Use these to practice pattern recognition specific to Netflix's interview process.

**Netflix Problem 1:**

```python-repl
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Example:
set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1
get("foo", 1);         // return "bar"
get("foo", 3);         // return "bar" since it was the value at the most recent time
set("foo", "bar2", 4); // store key "foo", value "bar2", timestamp = 4
get("foo", 4);         // return "bar2"
get("foo", 5);         // return "bar2"
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Binary Search + Hash Map**

  **Why**: Need to efficiently store and retrieve values based on timestamps.

  **Key Insight**: Use a hash map where each key maps to a list of [timestamp, value] pairs sorted by timestamp. Then use binary search to find the closest timestamp.

</details>

**Netflix Problem 2:**

```python-repl
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
'*' can be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.

Example:
Input: s = "(*)"
Output: true
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Stack + Greedy**

  **Why**: Need to track opening and closing parentheses while handling wildcards optimally.

  **Key Insight**: Track the minimum and maximum possible open parentheses as you scan from left to right, considering * as either open, close, or empty.

</details>

**Netflix Problem 3:**

```python-repl
Given an array of meeting time intervals where intervals[i] = [start_i, end_i], determine the minimum number of meeting rooms required.

Example:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Heap (Priority Queue) + Sorting**

  **Why**: Need to track overlapping intervals to determine resource allocation.

  **Key Insight**: Sort intervals by start time and use a min-heap to track end times of active meetings. The size of the heap represents the number of rooms needed.

</details>

**Netflix Problem 4:**

```python-repl
Design and implement a data structure for Least Recently Used (LRU) cache.
It should support get and put operations with O(1) time complexity.

Example:
LRUCache cache = new LRUCache(2); // capacity = 2
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Hash Map + Doubly Linked List**

  **Why**: Need O(1) access time and a way to track usage order.

  **Key Insight**: Use a hash map for O(1) lookup and a doubly linked list to maintain order of usage, moving elements to the front when accessed.

</details>

**Netflix Problem 5:**

```python-repl
Given an array of integers temperatures representing daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.

Example:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Monotonic Stack**

  **Why**: Need to find the next greater element for each temperature efficiently.

  **Key Insight**: Use a stack to keep track of indices of temperatures in decreasing order. When you find a higher temperature, pop from the stack and calculate the difference in days.

</details>

**Netflix Problem 6:**

```python-repl
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order. Merge all the linked-lists into one sorted linked-list and return it.

Example:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Heap (Priority Queue) + Linked List**

  **Why**: Need to efficiently select the smallest element from multiple sorted lists.

  **Key Insight**: Use a min-heap to track the smallest current node from each list, continuously extracting the minimum and adding the next node from that list.

</details>

**Netflix Problem 7:**

```python-repl
Implement the RandomizedSet class:
- insert(val): Inserts an item val if not present, returns true if inserted, false otherwise
- remove(val): Removes an item val if present, returns true if removed, false otherwise
- getRandom(): Returns a random element from the current set of elements with equal probability

Example:
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // return true
randomizedSet.remove(2); // return false
randomizedSet.insert(2); // return true
randomizedSet.getRandom(); // return 1 or 2 randomly
randomizedSet.remove(1); // return true
randomizedSet.insert(2); // return false (already exists)
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Hash Map + Array**

  **Why**: Need O(1) operations for all methods, including random access.

  **Key Insight**: Use a hash map for O(1) lookup and an array for O(1) random access. When removing, swap the element with the last element in the array to maintain O(1) time.

</details>

**Netflix Problem 8:**

```python-repl
Given a string containing digits from 2-9, return all possible letter combinations that the number could represent (like on a phone keypad).

Example:
Input: "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Backtracking**

  **Why**: Need to generate all possible combinations.

  **Key Insight**: Use recursive backtracking to build each combination, mapping each digit to its corresponding letters and exploring all possibilities.

</details>

**Netflix Problem 9:**

```python-repl
Given n courses and a list of prerequisites where prerequisites[i] = [ai, bi] indicates you must take course bi before course ai, return the ordering of courses you should take to finish all courses.

Example:
Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3] (both valid)
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Topological Sort**

  **Why**: Need to find a valid order of courses that respects prerequisites.

  **Key Insight**: Create a directed graph from prerequisites and use topological sorting (either BFS with in-degree tracking or DFS with three states) to find a valid course order.

</details>

**Netflix Problem 10:**

```python-repl
You are given a network delay time matrix representing how long it takes for a signal to travel from source to destination. Return the maximum signal travel time. If it's impossible for all nodes to receive the signal, return -1.

Example:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
```

<details>
  <summary>Click to reveal pattern</summary>

  **Pattern: Dijkstra's Algorithm**

  **Why**: Finding shortest paths in a weighted graph with non-negative weights.

  **Key Insight**: Use Dijkstra's algorithm to find the shortest path from the source to every other node. The answer is the maximum path length among all nodes.

</details>

## 2. Template Skeleton Exercise

### Instructions:

1. Complete the missing parts of these algorithm templates
2. Test with the provided example
3. Compare your solution with the complete implementation

### Sliding Window Template:

```python
def sliding_window_fixed(arr, k):
    # 1. Initialize window and result
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # 2. Slide window from left to right
    for i in range(k, len(arr)):
        # 3. Update window by adding new element and removing oldest
        window_sum = ______

        # 4. Update result
        max_sum = ______

    return max_sum

# Example: Find maximum sum subarray of size 3
# test_array = [2, 1, 5, 1, 3, 2]
# Expected output: 9 (subarray [5, 1, 3])
```

<details>
  <summary>Solution</summary>

```python
def sliding_window_fixed(arr, k):
    # 1. Initialize window and result
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # 2. Slide window from left to right
    for i in range(k, len(arr)):
        # 3. Update window by adding new element and removing oldest
        window_sum = window_sum + arr[i] - arr[i-k]

        # 4. Update result
        max_sum = max(max_sum, window_sum)

    return max_sum
```

</details>

### Two Pointers Template:

```python
def two_sum_sorted(arr, target):
    # 1. Initialize pointers at both ends
    left = ______
    right = ______

    # 2. Move pointers towards each other
    while left < right:
        current_sum = arr[left] + arr[right]

        # 3. Check if we found the target
        if current_sum == target:
            return [left, right]
        # 4. Adjust pointers based on sum
        elif current_sum < target:
            ______
        else:
            ______

    return [-1, -1]  # No solution found

# Example: Find pair with sum 9 in sorted array
# test_array = [1, 3, 4, 5, 7, 10, 11]
# Expected output: [1, 5] (indices of 3 and 10)
```

<details>
  <summary>Solution</summary>

```python
def two_sum_sorted(arr, target):
    # 1. Initialize pointers at both ends
    left = 0
    right = len(arr) - 1

    # 2. Move pointers towards each other
    while left < right:
        current_sum = arr[left] + arr[right]

        # 3. Check if we found the target
        if current_sum == target:
            return [left, right]
        # 4. Adjust pointers based on sum
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]  # No solution found
```

</details>

### Binary Search Template:

```python
def binary_search(arr, target):
    # 1. Initialize pointers
    left = ______
    right = ______

    # 2. Search while search space is valid
    while ______:
        # 3. Calculate mid point
        mid = ______

        # 4. Check if target is found
        if arr[mid] == target:
            return mid
        # 5. Adjust search space
        elif arr[mid] < target:
            left = ______
        else:
            right = ______

    return -1  # Target not found

# Example: Find element 7 in sorted array
# test_array = [1, 2, 4, 7, 9, 10, 11, 13, 15]
# Expected output: 3 (index of 7)
```

<details>
  <summary>Solution</summary>

```python
def binary_search(arr, target):
    # 1. Initialize pointers
    left = 0
    right = len(arr) - 1

    # 2. Search while search space is valid
    while left <= right:
        # 3. Calculate mid point
        mid = left + (right - left) // 2

        # 4. Check if target is found
        if arr[mid] == target:
            return mid
        # 5. Adjust search space
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Target not found
```

</details>

## 3. Algorithm Decision Tree

Use this decision tree to help identify which algorithm pattern to use for a given problem.

### Instructions:

1. Start at the top question
2. Follow the path based on your answers about the problem
3. The leaf nodes suggest algorithm patterns to consider

```text
Is the problem about finding a subarray/substring?
├── Yes → Does it involve fixed size segments?
│   ├── Yes → Use SLIDING WINDOW (FIXED)
│   │   Examples: Max sum subarray of size K, Find all anagrams
│   │
│   └── No → Does it involve optimizing a constraint?
│       ├── Yes → Use SLIDING WINDOW (VARIABLE)
│       │   Examples: Longest substring with K distinct chars, Minimum window substring
│       │
│       └── No → Is it about the sum of subarrays?
│           ├── Yes → Consider PREFIX SUM
│           │   Examples: Subarray sum equals K, Maximum size subarray sum equals K
│           │
│           └── No → Consider KADANE'S ALGORITHM (for max/min subarray sum)
│               Examples: Maximum subarray, Maximum circular subarray sum
│
└── No → Is the problem about searching in a collection?
    ├── Yes → Is the collection sorted (or partially sorted)?
    │   ├── Yes → Consider BINARY SEARCH
    │   │   Examples: Search in rotated sorted array, Find first and last position
    │   │
    │   └── No → Does it involve two sorted arrays/lists?
    │       ├── Yes → Consider TWO POINTERS
    │       │   Examples: Merge two sorted arrays, Intersection of two arrays
    │       │
    │       └── No → Is it a graph-like structure?
    │           ├── Yes → Is it about finding the shortest path?
    │           │   ├── Yes → Use BFS or DIJKSTRA'S ALGORITHM
    │           │   │   Examples: Word ladder, Network delay time
    │           │   │
    │           │   └── No → Consider DFS or TOPOLOGICAL SORT
    │           │       Examples: Course schedule, Clone graph
    │           │
    │           └── No → Is it about combinations or permutations?
    │               ├── Yes → Use BACKTRACKING
    │               │   Examples: Subsets, Permutations, N-Queens
    │               │
    │               └── No → Does it have overlapping subproblems?
    │                   ├── Yes → Use DYNAMIC PROGRAMMING
    │                   │   Examples: Knapsack, Longest common subsequence
    │                   │
    │                   └── No → Consider DIVIDE & CONQUER or GREEDY
    │                       Examples: Merge sort, Meeting rooms
    │
    └── No → Does it involve a linked list?
        ├── Yes → Does it involve detecting a cycle or finding middle?
        │   ├── Yes → Use FAST & SLOW POINTERS
        │   │   Examples: Linked list cycle, Middle of linked list
        │   │
        │   └── No → Consider ITERATIVE REVERSAL or RECURSION
        │       Examples: Reverse linked list, Merge K sorted lists
        │
        └── No → Does it involve dynamic statistics (median, top-K, etc.)?
            ├── Yes → Consider HEAP or TWO HEAPS
            │   Examples: Find median from data stream, Kth largest element
            │
            └── No → Is it about tracking frequencies or lookups?
                ├── Yes → Use HASH MAP
                │   Examples: Two sum, Group anagrams
                │
                └── No → Consider other specialized DATA STRUCTURES
                    Examples: LRU cache, Implement Trie
```

## 4. Time Attack Implementation Challenge

### Instructions:

1. Set a timer for the specified time
2. Implement the algorithm from memory
3. Compare your implementation with the reference solution
4. Note areas where you struggled

### Challenge 1: Implement Kadane's Algorithm (5 minutes)

**Problem**: Find the maximum sum of a contiguous subarray within a one-dimensional array of numbers.

**Example**:

```
Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
Output: 6
```

**Timer**: 5 minutes

<details>
  <summary>Reference Solution</summary>

```python
def kadane(nums):
    max_so_far = float('-inf')
    max_ending_here = 0

    for num in nums:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
```

</details>

### Challenge 2: Implement Binary Search (5 minutes)

**Problem**: Find the index of a target value in a sorted array. Return -1 if target doesn't exist.

**Example**:

```
Input: [1, 2, 3, 4, 5, 6, 7, 8, 9], target = 6
Output: 5
```

**Timer**: 5 minutes

<details>
  <summary>Reference Solution</summary>

```python
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

</details>

### Challenge 3: Implement BFS for Shortest Path (10 minutes)

**Problem**: Find the shortest path from source to destination in an unweighted graph.

**Example**:

```
Input:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
source = 'A'
destination = 'F'

Output: 2 (A -> C -> F)
```

**Timer**: 10 minutes

<details>
  <summary>Reference Solution</summary>

```python
from collections import deque

def shortest_path(graph, start, end):
    if start == end:
        return 0

    visited = set([start])
    queue = deque([(start, 0)])  # (node, distance)

    while queue:
        node, distance = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor == end:
                return distance + 1

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1  # No path found
```

</details>

## 5. Algorithm Complexity Quiz

Test your understanding of time and space complexity for different algorithms.

### Instructions:

1. For each algorithm, identify the time and space complexity
2. Check your answers against the solutions

**Question 1:** What is the time and space complexity of the following two-pointer algorithm?

```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]
```

<details>
  <summary>Answer</summary>

  **Time Complexity**: O(n) - we're making one pass through the array

  **Space Complexity**: O(1) - we only use two pointer variables regardless of input size

</details>

**Question 2:** What is the time and space complexity of the following backtracking algorithm?

```python
def subsets(nums):
    result = []

    def backtrack(start, current):
        result.append(current[:])

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
```

<details>
  <summary>Answer</summary>

  **Time Complexity**: O(2^n * n) - There are 2^n possible subsets, and each subset might require O(n) time to copy

  **Space Complexity**: O(n) - excluding the output storage, the recursion stack and current subset can go up to n elements deep

</details>

**Question 3:** What is the time and space complexity of the following sliding window algorithm?

```python
def longest_substring_with_k_distinct(s, k):
    char_frequency = {}
    start = 0
    max_length = 0

    for end in range(len(s)):
        char_frequency[s[end]] = char_frequency.get(s[end], 0) + 1

        while len(char_frequency) > k:
            char_frequency[s[start]] -= 1
            if char_frequency[s[start]] == 0:
                del char_frequency[s[start]]
            start += 1

        max_length = max(max_length, end - start + 1)

    return max_length
```

<details>
  <summary>Answer</summary>

  **Time Complexity**: O(n) - we process each character at most twice (once when adding to the window, once when removing)

  **Space Complexity**: O(k) - the character frequency map will have at most k+1 entries

</details>

**Question 4:** What is the time and space complexity of this dynamic programming solution?

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]
```

<details>
  <summary>Answer</summary>

  **Time Complexity**: O(n * W) - where n is the number of items and W is the capacity

  **Space Complexity**: O(n * W) - for the 2D dp array

</details>

**Question 5:** What is the time and space complexity of the following quick sort implementation?

```python
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
```

<details>
  <summary>Answer</summary>

  **Time Complexity**:

- Average Case: O(n log n)
- Worst Case: O(n²) - when the array is already sorted and we choose the last element as pivot

  **Space Complexity**:
- Average Case: O(log n) - for the recursion stack
- Worst Case: O(n) - when the recursion is unbalanced

</details>

## 6. Algorithm Pattern Matching Game

### Instructions:

1. For each problem description, identify the most appropriate algorithm pattern
2. Check your answer against the solution
3. Try to solve the problem using that pattern

**Problem 1:**

```
You are given a string and a dictionary of words. Determine if the string can be segmented into a space-separated sequence of dictionary words.

Example:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: The string can be segmented as "apple pen apple".
```

<details>
  <summary>Appropriate Pattern</summary>

  **Pattern: Dynamic Programming**

  **Approach**:

1. Create a DP array where dp[i] represents whether the substring s[0...i-1] can be segmented
2. Base case: dp[0] = true (empty string)
3. For each position i, check if any prefix s[0...j-1] can be segmented (dp[j] is true) AND the remaining suffix s[j...i-1] is in the dictionary

  **Implementation**:

```python
  def word_break(s, word_dict):
      n = len(s)
      dp = [False] * (n + 1)
      dp[0] = True  # Empty string is always valid

      for i in range(1, n + 1):
          for j in range(i):
              if dp[j] and s[j:i] in word_dict:
                  dp[i] = True
                  break

      return dp[n]
```

</details>

**Problem 2:**

```
Given a string, find the length of the longest substring without repeating characters.

Example:
Input: "abcabcbb"
Output: 3
Explanation: The longest substring is "abc", with length 3.
```

<details>
  <summary>Appropriate Pattern</summary>

  **Pattern: Sliding Window**

  **Approach**:

1. Use a sliding window to track the current substring
2. Use a hash map or set to track characters in the current window
3. Expand window to the right, and contract from left if duplicate found

  **Implementation**:

```python
  def length_of_longest_substring(s):
      char_index_map = {}
      max_length = 0
      start = 0

      for end in range(len(s)):
          # If character already in window, update start position
          if s[end] in char_index_map:
              start = max(start, char_index_map[s[end]] + 1)

          # Update character position and max length
          char_index_map[s[end]] = end
          max_length = max(max_length, end - start + 1)

      return max_length
```

</details>

**Problem 3:**

```
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

Example:
Input: [1,3,5,6], target = 5
Output: 2
```

<details>
  <summary>Appropriate Pattern</summary>

  **Pattern: Binary Search**

  **Approach**:

1. Use binary search to find the target or insertion position
2. The loop condition and return value need to be carefully handled to find the insertion position

  **Implementation**:

```python
  def search_insert(nums, target):
      left, right = 0, len(nums) - 1

      while left <= right:
          mid = left + (right - left) // 2

          if nums[mid] == target:
              return mid
          elif nums[mid] < target:
              left = mid + 1
          else:
              right = mid - 1

      return left  # This will be the insertion point
```

</details>

**Problem 4:**

```
Given a string containing digits from 2-9, return all possible letter combinations that the number could represent (like on a phone keypad).

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

<details>
  <summary>Appropriate Pattern</summary>

  **Pattern: Backtracking**

  **Approach**:

1. Create a mapping from digits to letters
2. Use backtracking to generate all combinations

  **Implementation**:

```python
  def letter_combinations(digits):
      if not digits:
          return []

      # Mapping of digits to letters
      mapping = {
          '2': 'abc',
          '3': 'def',
          '4': 'ghi',
          '5': 'jkl',
          '6': 'mno',
          '7': 'pqrs',
          '8': 'tuv',
          '9': 'wxyz'
      }

      result = []

      def backtrack(index, current):
          # Base case: we've processed all digits
          if index == len(digits):
              result.append(current)
              return

          # Get the letters for current digit
          letters = mapping[digits[index]]

          # Try each letter
          for letter in letters:
              backtrack(index + 1, current + letter)

      backtrack(0, "")
      return result
```

</details>

**Problem 5:**

```
Given a linked list, determine if it has a cycle.

Example:
Input: head -> node1 -> node2 -> node3 -> node1 (points back to node1)
Output: true
```

<details>
  <summary>Appropriate Pattern</summary>

  **Pattern: Fast & Slow Pointers**

  **Approach**:

1. Use two pointers: slow (moves one step) and fast (moves two steps)
2. If there's a cycle, fast will eventually catch up to slow

  **Implementation**:

```python
  def has_cycle(head):
      if not head or not head.next:
          return False

      slow = head
      fast = head.next

      while slow != fast:
          if not fast or not fast.next:
              return False
          slow = slow.next
          fast = fast.next.next

      return True
```

</details>

## 7. Memory Optimization Challenge

### Instructions:

1. Each problem below has a solution that works but uses non-optimal space
2. Your task is to optimize it to use less memory
3. Compare your solution with the optimized version

**Challenge 1: Optimize 0/1 Knapsack**

Original solution (O(n*W) space):

```python
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w-weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]
```

<details>
  <summary>Optimized Solution (O(W) space)</summary>

```python
def knapsack_optimized(weights, values, capacity):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        # Process in reverse to avoid using items multiple times
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

    return dp[capacity]
```

**Optimization**: We only need the previous row's results to calculate the current row, so we can use a 1D array and process weight capacity in reverse order.

</details>

**Challenge 2: Optimize Longest Common Subsequence**

Original solution (O(m*n) space):

```python
def longest_common_subsequence(text1, text2):
    m, n = len(text1), len(text2)

    # Initialize DP table
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

<details>
  <summary>Optimized Solution (O(min(m,n)) space)</summary>

```python
def longest_common_subsequence_optimized(text1, text2):
    # Ensure text1 is the shorter string for optimization
    if len(text1) > len(text2):
        text1, text2 = text2, text1

    m, n = len(text1), len(text2)

    # We only need two rows: current and previous
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)

    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if text1[i-1] == text2[j-1]:
                curr[i] = prev[i-1] + 1
            else:
                curr[i] = max(curr[i-1], prev[i])

        # Swap rows
        prev, curr = curr, prev

    return prev[m]
```

**Further Optimization**: We can optimize to O(min(m,n)) space by ensuring we work with the shorter string in the inner loop. We only need to store two rows - the current and previous.

</details>

**Challenge 3: Optimize Fibonacci Number**

Original solution (O(n) space):

```python
def fibonacci(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]
```

<details>
  <summary>Optimized Solution (O(1) space)</summary>

```python
def fibonacci_optimized(n):
    if n <= 1:
        return n

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b
```

**Optimization**: Since each Fibonacci number only depends on the previous two numbers, we can use two variables instead of an array, reducing space to O(1).

</details>

## 8. Algorithm Pattern Drill Cards

Use these drill cards to help you quickly identify which algorithm patterns to apply based on key problem characteristics.

### Instructions:

1. Read the problem characteristic
2. Try to identify which algorithm pattern would be most appropriate
3. Check the answer and review examples

**Card 1: Contiguous Subarrays**

When you see problems involving:
- Finding maximum/minimum subarrays of fixed or variable size
- Finding longest substring with a condition
- Processing a "window" of elements

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Sliding Window**
  
  **Examples:**
  - Maximum sum subarray of size K
  - Longest substring with K distinct characters
  - Minimum size subarray with a given sum
  - Find all anagrams in a string
  
  **Time Complexity:** O(n) where n is array length (each element processed at most twice)
  
  **Space Complexity:** O(1) for fixed window, O(k) where k is window size for variable window
</details>

**Card 2: Sorted Arrays or Linked Lists**

When you see problems involving:
- Finding pairs in sorted arrays
- Removing duplicates
- Palindrome verification
- Merging sorted arrays

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Two Pointers**
  
  **Examples:**
  - Two Sum in sorted array
  - Remove duplicates from sorted array
  - Container with Most Water
  - Palindrome verification
  
  **Time Complexity:** O(n) for most implementations or O(n²) for nested two pointers
  
  **Space Complexity:** O(1) as typically implemented in-place
</details>

**Card 3: Maximum/Minimum Subarray Sum**

When you see problems involving:
- Finding maximum sum contiguous subarray
- Maximum product subarray
- Local vs global optimal values

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Kadane's Algorithm**
  
  **Examples:**
  - Maximum sum subarray
  - Maximum product subarray
  - Circular array maximum sum
  
  **Time Complexity:** O(n)
  
  **Space Complexity:** O(1)
</details>

**Card 4: Range Sum Queries**

When you see problems involving:
- Cumulative operations on arrays
- Checking for specific sum conditions over subarrays
- Range-based queries

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Prefix Sums**
  
  **Examples:**
  - Range sum queries
  - Subarray sum equals K
  - Count number of subarrays with specific properties
  
  **Time Complexity:** O(n) for preprocessing, O(1) for queries
  
  **Space Complexity:** O(n) for storing prefix sums
</details>

**Card 5: Cycle Detection in Linked Lists**

When you see problems involving:
- Finding cycles in linked list
- Finding middle element
- Finding nth element from the end

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Fast & Slow Pointers**
  
  **Examples:**
  - Detect cycle in linked list
  - Find cycle start point
  - Find middle of linked list
  - Palindrome linked list
  
  **Time Complexity:** O(n)
  
  **Space Complexity:** O(1)
</details>

**Card 6: Linked List Reversal**

When you see problems involving:
- Reversing all or part of a linked list
- Problems with K-groups or alternative operations

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Linked List Reversal**
  
  **Examples:**
  - Reverse linked list
  - Reverse nodes in K-group
  - Reverse alternating K elements
  
  **Time Complexity:** O(n)
  
  **Space Complexity:** O(1) for iterative solutions, O(n) for recursive solutions
</details>

**Card 7: Tree Traversal**

When you see problems involving:
- Visiting all nodes in a tree
- Node relationship problems
- Collecting data from all nodes

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Tree Traversal**
  
  **Examples:**
  - Preorder, inorder, postorder traversal
  - Level order traversal
  - Path sum problems
  - Tree serialization/deserialization
  
  **Time Complexity:** O(n) where n is number of nodes
  
  **Space Complexity:** O(h) where h is tree height for recursion, O(n) worst case
</details>

**Card 8: Path Finding**

When you see problems involving:
- Finding shortest path in unweighted graph/tree
- Level-order traversal
- Finding nodes at k distance

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Breadth-First Search (BFS)**
  
  **Examples:**
  - Shortest path in unweighted graph
  - Level order traversal
  - Word ladder problems
  - Connected components
  
  **Time Complexity:** O(V + E) where V is vertices and E is edges
  
  **Space Complexity:** O(w) where w is maximum width of tree/graph
</details>

**Card 9: Exhaustive Exploration**

When you see problems involving:
- Exhaustive tree/graph exploration
- Path finding problems
- Problems requiring backtracking

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Depth-First Search (DFS)**
  
  **Examples:**
  - Path existence between nodes
  - Connected components
  - Topological sorting
  - Cycle detection
  
  **Time Complexity:** O(V + E) where V is vertices and E is edges
  
  **Space Complexity:** O(h) for recursion stack where h is maximum depth
</details>

**Card 10: Binary Search Applications**

When you see problems involving:
- Sorted arrays or matrices
- Search space that can be halved each time
- Minimize maximum value problems

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Binary Search Variations**
  
  **Examples:**
  - Search in rotated sorted array
  - Find peak element
  - Find minimum in rotated sorted array
  - Search for a range
  
  **Time Complexity:** O(log n)
  
  **Space Complexity:** O(1) iterative, O(log n) recursive
</details>

**Card 11: Knapsack Problems**

When you see problems involving:
- Items with values/weights and capacity constraints
- Including/excluding items to maximize value
- Subset sum problems

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: 0/1 Knapsack**
  
  **Examples:**
  - 0/1 Knapsack problem
  - Subset Sum
  - Partition Equal Subset Sum
  - Minimum Subset Sum Difference
  
  **Time Complexity:** O(n*W) where n is number of items and W is capacity
  
  **Space Complexity:** O(n*W), can be optimized to O(W)
</details>

**Card 12: Problems with Reusable Items**

When you see problems involving:
- Items that can be used multiple times
- Combinations to achieve a target sum
- Coin change problems

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Unbounded Knapsack**
  
  **Examples:**
  - Coin Change (minimum coins)
  - Coin Change II (number of ways)
  - Rod Cutting
  - Maximum Ribbon Cut
  
  **Time Complexity:** O(n*W) where n is item types and W is capacity
  
  **Space Complexity:** O(W)
</details>

**Card 13: String Comparison**

When you see problems involving:
- Finding common elements between strings
- Edit distance variations
- String transformations

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Longest Common Subsequence (LCS)**
  
  **Examples:**
  - Longest Common Subsequence
  - Shortest Common Supersequence
  - Edit Distance
  - Longest Palindromic Subsequence
  
  **Time Complexity:** O(m*n) where m and n are string lengths
  
  **Space Complexity:** O(m*n)
</details>

**Card 14: Sequence with Recursive Relation**

When you see problems involving:
- Current state depends on previous states
- Pattern like f(n) = f(n-1) + f(n-2)
- Counting ways to reach a target

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Fibonacci Sequence**
  
  **Examples:**
  - Fibonacci Numbers
  - Climbing Stairs
  - House Robber
  - Jump Game variations
  
  **Time Complexity:** O(n)
  
  **Space Complexity:** O(n), can be optimized to O(1)
</details>

**Card 15: Generating Combinations**

When you see problems involving:
- Generate all possible subsets/combinations
- Permutations of elements
- Building combinations with specific constraints

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Subsets/Backtracking**
  
  **Examples:**
  - Generate All Subsets
  - Letter Combinations of Phone Number
  - Permutations
  - Combinations
  
  **Time Complexity:** O(2^n) for subsets, O(n!) for permutations
  
  **Space Complexity:** O(n) for recursion stack
</details>

**Card 16: Complex Constraints**

When you see problems involving:
- Complex rule-based constraints
- Need to explore all valid solutions
- Search space can be pruned early

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Constraint Satisfaction**
  
  **Examples:**
  - N-Queens
  - Sudoku Solver
  - Word Search
  - Palindrome Partitioning
  
  **Time Complexity:** Exponential, but pruning reduces actual runtime
  
  **Space Complexity:** O(n) for recursion stack
</details>

**Card 17: Finding Top/Smallest K Elements**

When you see problems involving:
- Finding top/smallest K elements
- Processing stream with limited memory
- K frequent elements

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Top K Elements**
  
  **Examples:**
  - Kth Largest Element
  - K Closest Points to Origin
  - Top K Frequent Elements
  - Sort K-sorted Array
  
  **Time Complexity:** O(n log k) for processing n elements with heap of size k
  
  **Space Complexity:** O(k) for the heap
</details>

**Card 18: Median Calculation Problems**

When you see problems involving:
- Finding median from data stream
- Maintaining statistics on both sides of a midpoint
- Balancing elements

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Two Heaps**
  
  **Examples:**
  - Find Median from Data Stream
  - Sliding Window Median
  - IPO (maximize capital)
  
  **Time Complexity:** O(log n) per insertion
  
  **Space Complexity:** O(n) for storing all elements
</details>

**Card 19: Shortest Path in Weighted Graphs**

When you see problems involving:
- Finding shortest path in weighted graph
- Path finding with cost considerations
- Network routing problems

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Dijkstra's Algorithm**
  
  **Examples:**
  - Network Delay Time
  - Cheapest Flights Within K Stops
  - Path With Maximum Probability
  
  **Time Complexity:** O((V+E) log V) with binary heap
  
  **Space Complexity:** O(V)
</details>

**Card 20: Connected Components**

When you see problems involving:
- Grouping connected elements
- Dynamic connectivity
- Component membership queries

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Union-Find (Disjoint Set)**
  
  **Examples:**
  - Number of Connected Components
  - Redundant Connection
  - Account Merge
  - Graph Valid Tree
  
  **Time Complexity:** O(α(n)) amortized per operation (α is inverse Ackermann function)
  
  **Space Complexity:** O(n)
</details>

**Card 21: Prefix Tree Operations**

When you see problems involving:
- Dictionary operations on strings
- Prefix matching
- Autocomplete functionality

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Trie (Prefix Tree)**
  
  **Examples:**
  - Implement Trie
  - Word Search II
  - Replace Words
  - Design Search Autocomplete System
  
  **Time Complexity:** O(m) for operations, where m is key length
  
  **Space Complexity:** O(n*m) where n is number of keys and m is average key length
</details>

**Card 22: Locally Optimal Choices**

When you see problems involving:
- Local optimal choice leads to global optimum
- Optimization with "obvious" next steps
- Activity selection problems

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Greedy Algorithms**
  
  **Examples:**
  - Activity Selection
  - Minimum Number of Arrows
  - Task Scheduler
  - Gas Station
  
  **Time Complexity:** Often O(n log n) due to sorting
  
  **Space Complexity:** Usually O(1) or O(n)
</details>

**Card 23: Binary Representation**

When you see problems involving:
- Binary operations (AND, OR, XOR)
- Bit counting or manipulation
- Space optimization with bits

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Bit Manipulation**
  
  **Examples:**
  - Single Number
  - Counting Bits
  - Number of 1 Bits
  - Power of Two
  
  **Time Complexity:** O(1) to O(n) depending on problem
  
  **Space Complexity:** Usually O(1)
</details>

**Card 24: Overlapping Intervals**

When you see problems involving:
- Merging intervals
- Finding non-overlapping intervals
- Minimum rooms/resources needed

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Interval Merging/Sorting**
  
  **Examples:**
  - Merge Intervals
  - Insert Interval
  - Meeting Rooms
  - Non-overlapping Intervals
  
  **Time Complexity:** O(n log n) due to sorting
  
  **Space Complexity:** O(n) or O(1) depending on in-place operation
</details>

**Card 25: Dependency Ordering**

When you see problems involving:
- Task scheduling with prerequisites
- Detecting cycles in directed graphs
- Finding valid processing order

<details>
  <summary>Recommended Pattern</summary>

  **Pattern: Topological Sort**
  
  **Examples:**
  - Course Schedule
  - Course Schedule II
  - Alien Dictionary
  - Reconstruct Itinerary
  
  **Time Complexity:** O(V+E)
  
  **Space Complexity:** O(V+E)
</details>

## 9. Problem-to-Pattern Matching Exercise

This exercise will help you develop the skill of identifying which algorithm pattern to use when faced with different problem types.

### Instructions:

1. For each problem statement, analyze the key characteristics
2. Match it to the most appropriate algorithm pattern
3. Explain your reasoning
4. Check your answer with the solution

**Problem 1:**

```python-repl
You are given an array of integers and a target value. Find all unique quadruplets in the array which give the sum of the target.

Example:
Input: nums = [1, 0, -1, 0, -2, 2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
```

<details>
  <summary>Analysis & Pattern Match</summary>

  **Pattern: Two Pointers (with nested loops)**
  
  **Reasoning:**
  - We're looking for combinations of values that sum to a target
  - The problem involves finding elements that satisfy a condition
  - Since we need all combinations, we'll need nested loops, but two pointers pattern can optimize the inner loop
  
  **Approach:**
  1. Sort the array
  2. Use two nested loops to fix the first two elements
  3. Use two pointers for the remaining elements
  4. Skip duplicates to ensure unique quadruplets
  
  **Time Complexity:** O(n³)
  
  **Space Complexity:** O(1) excluding output space
</details>

**Problem 2:**

```python-repl
Given a string, find the length of the longest substring that contains at most k distinct characters.

Example:
Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.
```

<details>
  <summary>Analysis & Pattern Match</summary>

  **Pattern: Sliding Window (Variable Size)**
  
  **Reasoning:**
  - We're looking for a contiguous substring
  - The constraint is a maximum number of distinct characters
  - The window size needs to be adjusted dynamically based on this constraint
  
  **Approach:**
  1. Use a sliding window approach with two pointers (start and end)
  2. Use a hash map to track character frequencies within the window
  3. Expand window until constraint is violated (more than k distinct characters)
  4. Shrink window from left until constraint is satisfied again
  5. Track maximum valid window size
  
  **Time Complexity:** O(n)
  
  **Space Complexity:** O(k) for the character frequency map
</details>

**Problem 3:**

```python-repl
Given a matrix of 0s and 1s, count the number of islands. An island is a connected group of 1s (horizontally or vertically) surrounded by 0s.

Example:
Input: 
[
  [1,1,0,0,0],
  [1,1,0,0,0],
  [0,0,1,0,0],
  [0,0,0,1,1]
]
Output: 3
```

<details>
  <summary>Analysis & Pattern Match</summary>

  **Pattern: Depth-First Search (DFS) or Breadth-First Search (BFS) on Matrix**
  
  **Reasoning:**
  - We need to identify connected components in a graph
  - Each cell is connected to its four adjacent cells
  - Once we find a '1', we need to explore and mark all connected '1's as visited
  
  **Approach:**
  1. Iterate through each cell in the matrix
  2. When we find a '1', increment our island count
  3. Use DFS or BFS to explore all connected '1's and mark them as visited (change to '0')
  4. Continue until all cells are checked
  
  **Time Complexity:** O(m*n) where m is number of rows and n is number of columns
  
  **Space Complexity:** O(m*n) in worst case for recursion stack
</details>

**Problem 4:**

```python-repl
Find the kth largest element in an unsorted array.

Example:
Input: [3,2,1,5,6,4], k = 2
Output: 5
```

<details>
  <summary>Analysis & Pattern Match</summary>

  **Pattern: Heap (Priority Queue) / QuickSelect**
  
  **Reasoning:**
  - We need to find an element based on its order statistic
  - Sorting would work but is not optimal
  - Heap or QuickSelect are more efficient
  
  **Approach 1 (Heap):**
  1. Build a min-heap of size k
  2. Insert the first k elements from the array
  3. For remaining elements, if larger than the root, replace root and heapify
  4. The root of the heap will be the kth largest element
  
  **Time Complexity:** O(n log k)
  
  **Space Complexity:** O(k)
  
  **Approach 2 (QuickSelect):**
  1. Use a variation of quicksort where we only recurse into the half that contains our target
  2. Partition the array around a pivot
  3. If the pivot index is our target, return it
  4. Otherwise, recurse into the appropriate half
  
  **Time Complexity:** O(n) average case, O(n²) worst case
  
  **Space Complexity:** O(1)
</details>

**Problem 5:**

```python-repl
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

Example:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
```

<details>
  <summary>Analysis & Pattern Match</summary>

  **Pattern: Interval Merging/Sorting**
  
  **Reasoning:**
  - We're working with intervals that may need to be merged
  - We need to handle overlapping intervals
  - The intervals are already sorted
  
  **Approach:**
  1. Initialize result list
  2. Add all intervals that come before newInterval (end < newInterval.start)
  3. Merge overlapping intervals with newInterval (update newInterval boundaries)
  4. Add the merged newInterval to result
  5. Add all remaining intervals
  
  **Time Complexity:** O(n)
  
  **Space Complexity:** O(n) for the result list
</details>

---

These ready-to-use activities provide immediate practice opportunities for various algorithm learning strategies. Use them to test your current knowledge, reinforce pattern recognition, and improve implementation skills. As you get comfortable with these exercises, you can create your own variations or move on to more complex challenges.

