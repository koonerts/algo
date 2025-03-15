# Additional Algorithm Patterns for SWE Interviews

## When to Use

- **Binary Search**: When searching in a sorted array or when the search space can be monotonically divided
- **Greedy Algorithms**: When making locally optimal choices leads to a global optimum solution
- **Divide and Conquer**: When a problem can be broken down into independent subproblems
- **Bucket Sort**: When the input is uniformly distributed over a range, or when linear time sorting is needed
- **Bit Manipulation**: When working with binary operations, optimizing space, or solving numeric problems
- **Cyclic Sort**: When array contains numbers in a given range and you need to sort in-place
- **Reservoir Sampling**: When sampling from a large or streaming dataset
- **Line Sweep**: When processing intervals, rectangles, or geometric problems
- **Meet in the Middle**: When the search space is too large for brute force but can be split
- **Monotonic Stack/Queue**: When finding the next greater/smaller element or when processing ranges

## Binary Search Variations

### Standard Binary Search and Its Variants

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

### Finding First and Last Occurrence

```python
def first_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            result = mid  # Found a target, but continue searching left side
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result

def last_occurrence(nums, target):
    left, right = 0, len(nums) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            result = mid  # Found a target, but continue searching right side
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return result
```

### Binary Search on Answer

```python
def minimum_capacity(weights, days):
    # Return whether we can ship all packages within 'days' days with 'capacity'
    def feasible(capacity):
        days_needed, current_load = 1, 0
        for weight in weights:
            if current_load + weight > capacity:
                days_needed += 1
                current_load = weight
            else:
                current_load += weight
        return days_needed <= days
    
    left = max(weights)  # Minimum capacity is the largest single weight
    right = sum(weights) # Maximum capacity is sum of all weights
    
    while left < right:
        mid = left + (right - left) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1
            
    return left
```

## Monotonic Stack/Queue

Monotonic stacks/queues maintain elements in monotonically increasing or decreasing order and are especially useful for problems involving the "next greater/smaller element".

### Next Greater Element

```python
def next_greater_element(nums):
    n = len(nums)
    result = [-1] * n
    stack = []  # Stack will store indices
    
    for i in range(n):
        # Pop elements from stack while current element is greater
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]
        
        # Push current index to stack
        stack.append(i)
        
    return result
```

### Largest Rectangle in Histogram

```python
def largest_rectangle_area(heights):
    stack = []  # (index, height)
    max_area = 0
    
    for i, h in enumerate(heights):
        start = i
        
        # Pop taller heights from stack
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            max_area = max(max_area, height * (i - index))
            start = index
            
        # Push current height with the earliest possible start index
        stack.append((start, h))
        
    # Process the remaining heights in the stack
    for i, h in stack:
        max_area = max(max_area, h * (len(heights) - i))
        
    return max_area
```

## BFS for Shortest Path in Unweighted Graph

```python
from collections import deque

def shortest_path(graph, start, end):
    if start == end:
        return 0
        
    visited = set([start])
    queue = deque([(start, 0)])  # (node, distance)
    
    while queue:
        node, distance = queue.popleft()
        
        for neighbor in graph[node]:
            if neighbor == end:
                return distance + 1
                
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))
                
    return -1  # No path found
```

## Bit Manipulation Techniques

### Counting Bits

```python
def count_bits(n):
    """Returns number of 1s in binary representation of n."""
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# More efficient for large numbers with few 1 bits
def count_bits_kernighan(n):
    """Kernighan's algorithm - only iterates through set bits."""
    count = 0
    while n:
        n &= (n - 1)  # Clear the least significant set bit
        count += 1
    return count
```

### Single Number Among Duplicates

```python
def single_number(nums):
    """Find the single number in an array where all others appear twice."""
    result = 0
    for num in nums:
        result ^= num
    return result
```

### Power of Two Check

```python
def is_power_of_two(n):
    """Check if n is a power of 2."""
    if n <= 0:
        return False
    return (n & (n - 1)) == 0
```

## Dutch National Flag / Three-Way Partitioning

Used for sorting arrays with limited distinct values, like the classic "Sort Colors" problem.

```python
def sort_colors(nums):
    """
    Sort array in-place where nums[i] is 0, 1, or 2.
    Aka Dutch National Flag problem.
    """
    low, mid, high = 0, 0, len(nums) - 1
    
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
```

## Boyer-Moore Voting Algorithm (Majority Element)

Finds the majority element (appears more than n/2 times) in linear time and constant space.

```python
def majority_element(nums):
    candidate = None
    count = 0
    
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
            
    return candidate
```

## Floyd's Cycle Finding (Tortoise and Hare)

Another variation useful for finding cycles in sequences.

```python
def find_duplicate(nums):
    """Find duplicate in array of n+1 integers in range 1 to n."""
    slow = fast = nums[0]
    
    # Find meeting point inside the cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
            
    # Find cycle entrance
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        
    return slow
```

## Greedy Algorithms

### Activity Selection

```python
def max_activities(start, finish):
    """Select maximum number of non-overlapping activities."""
    n = len(start)
    # Sort by finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])
    
    count = 0
    last_finish = 0
    
    for s, f in activities:
        if s >= last_finish:
            count += 1
            last_finish = f
            
    return count
```

### Interval Merging

```python
def merge_intervals(intervals):
    if not intervals:
        return []
        
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    result = [intervals[0]]
    
    for interval in intervals[1:]:
        # If current interval overlaps with the last merged interval
        if interval[0] <= result[-1][1]:
            # Update the end time of previous interval if needed
            result[-1][1] = max(result[-1][1], interval[1])
        else:
            # Add as a new interval
            result.append(interval)
            
    return result
```

## Matrix Traversal Techniques

### Spiral Traversal

```python
def spiral_order(matrix):
    if not matrix:
        return []
        
    result = []
    rows, cols = len(matrix), len(matrix[0])
    top, bottom = 0, rows - 1
    left, right = 0, cols - 1
    
    while top <= bottom and left <= right:
        # Traverse right
        for j in range(left, right + 1):
            result.append(matrix[top][j])
        top += 1
        
        # Traverse down
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        
        # Traverse left
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(matrix[bottom][j])
            bottom -= 1
            
        # Traverse up
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            
    return result
```

### Rotate Matrix

```python
def rotate_matrix(matrix):
    """Rotate matrix 90 degrees clockwise in-place."""
    n = len(matrix)
    
    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
```

## Reservoir Sampling

For sampling k elements from a stream of unknown length with equal probability.

```python
import random

def reservoir_sampling(stream, k):
    """Sample k elements from a stream with equal probability."""
    result = []
    
    for i, item in enumerate(stream):
        if i < k:
            result.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                result[j] = item
                
    return result
```

## Quick Select (Kth Largest Element)

```python
def find_kth_largest(nums, k):
    """Find the kth largest element in an unsorted array."""
    def partition(left, right, pivot_index):
        pivot = nums[pivot_index]
        # Move pivot to end
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        
        # Move all elements smaller than pivot to the left
        store_index = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[store_index], nums[i] = nums[i], nums[store_index]
                store_index += 1
                
        # Move pivot to its final position
        nums[store_index], nums[right] = nums[right], nums[store_index]
        
        return store_index
        
    def select(left, right, k_smallest):
        if left == right:
            return nums[left]
            
        # Select a random pivot
        pivot_index = random.randint(left, right)
        
        # Find the position of the pivot after partition
        pivot_index = partition(left, right, pivot_index)
        
        if k_smallest == pivot_index:
            return nums[k_smallest]
        elif k_smallest < pivot_index:
            return select(left, pivot_index - 1, k_smallest)
        else:
            return select(pivot_index + 1, right, k_smallest)
            
    # Find kth largest = (n - k)th smallest
    return select(0, len(nums) - 1, len(nums) - k)
```

## Rabin-Karp String Matching

```python
def rabin_karp(text, pattern):
    """Find all occurrences of pattern in text."""
    n, m = len(text), len(pattern)
    if m > n:
        return []
        
    prime = 101  # A prime number
    d = 256      # Number of characters in input alphabet
    
    # Calculate hash for pattern and first window of text
    pattern_hash = 0
    text_hash = 0
    h = 1
    
    # Calculate h = d^(m-1) % prime
    for i in range(m - 1):
        h = (h * d) % prime
        
    for i in range(m):
        pattern_hash = (d * pattern_hash + ord(pattern[i])) % prime
        text_hash = (d * text_hash + ord(text[i])) % prime
        
    result = []
    
    # Slide the pattern over text one by one
    for i in range(n - m + 1):
        # Check if hash values match
        if pattern_hash == text_hash:
            # Check for characters one by one
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
                    
            if match:
                result.append(i)
                
        # Calculate hash for next window
        if i < n - m:
            text_hash = (d * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % prime
            if text_hash < 0:
                text_hash += prime
                
    return result
```

## Time & Space Complexity Analysis

| Algorithm | Time Complexity | Space Complexity | Notes |
|-----------|----------------|-----------------|-------|
| Binary Search | O(log n) | O(1) | Requires sorted array |
| Monotonic Stack | O(n) | O(n) | One pass through array |
| BFS Shortest Path | O(V + E) | O(V) | For unweighted graphs |
| Bit Manipulation | O(1) to O(log n) | O(1) | Constant time for small integers |
| Dutch Flag | O(n) | O(1) | One-pass, in-place sort |
| Boyer-Moore Voting | O(n) | O(1) | Finds majority element |
| Greedy Interval | O(n log n) | O(n) | Sorting dominates time |
| Matrix Traversal | O(m×n) | O(1) | In-place algorithms |
| Reservoir Sampling | O(n) | O(k) | For k samples |
| Quick Select | O(n) average | O(log n) | O(n²) worst case |
| Rabin-Karp | O(n+m) average | O(1) | O(nm) worst case |

## Interview Tips

- **Binary Search**: Practice on boundary conditions; check for off-by-one errors
- **Monotonic Stack**: Great for "next greater/smaller" and "largest rectangle" type problems
- **BFS**: First choice for unweighted shortest path problems
- **Bit Manipulation**: Often gives the most efficient solution for certain problems
- **Three-way Partitioning**: Essential for variants of the Dutch Flag problem
- **Boyer-Moore**: Remember to verify the majority candidate with a second pass if needed
- **Greedy Algorithms**: Prove the greedy choice is optimal
- **Matrix Problems**: Be methodical about boundary conditions
- **Randomized Algorithms**: Understand probability behind reservoir sampling and quickselect

## Common Interview Questions

- Binary Search: "Search in Rotated Sorted Array", "Find Peak Element"
- Monotonic Stack: "Daily Temperatures", "Next Greater Element"
- Bit Manipulation: "Single Number", "Counting Bits"
- Three-way Partitioning: "Sort Colors", "Three-way Partition"
- Boyer-Moore: "Majority Element", "Majority Element II"
- Greedy: "Meeting Rooms", "Jump Game"
- Matrix: "Rotate Image", "Spiral Matrix"
- Reservoir Sampling: "Random Pick Index", "Linked List Random Node"
- Quick Select: "Kth Largest Element in an Array"
- Rabin-Karp: "Repeated DNA Sequences", "Implement strStr()"