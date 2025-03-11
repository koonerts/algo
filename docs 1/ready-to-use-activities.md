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
```
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
```
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
```
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
```
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
```
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
```
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
```
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
```
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
```
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
```
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

```
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

---

These ready-to-use activities provide immediate practice opportunities for various algorithm learning strategies. Use them to test your current knowledge, reinforce pattern recognition, and improve implementation skills. As you get comfortable with these exercises, you can create your own variations or move on to more complex challenges.