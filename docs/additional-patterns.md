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

---

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
# Time: O(log n), Space: O(1)
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
# Time: O(log n), Space: O(1)
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
# Time: O(n log W) where W is the sum of weights, Space: O(1)
```

---

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
# Time: O(n), Space: O(n)
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
# Time: O(n), Space: O(n)
```

---

## BFS for Shortest Path

Breadth-First Search is the go-to algorithm for finding shortest paths in unweighted graphs.

```python
from collections import deque

def shortest_path(graph, start, target):
    if start == target:
        return 0

    queue = deque([(start, 0)])  # (node, distance)
    visited = set([start])

    while queue:
        node, distance = queue.popleft()

        for neighbor in graph[node]:
            if neighbor == target:
                return distance + 1

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, distance + 1))

    return -1  # No path found
# Time: O(V + E), Space: O(V)
```

---

## Bit Manipulation

Bit manipulation techniques are useful for optimizing space and solving numeric problems.

### Common Bit Operations

```python
# Check if the i-th bit is set
def is_bit_set(num, i):
    return (num & (1 << i)) != 0

# Set the i-th bit
def set_bit(num, i):
    return num | (1 << i)

# Clear the i-th bit
def clear_bit(num, i):
    return num & ~(1 << i)

# Toggle the i-th bit
def toggle_bit(num, i):
    return num ^ (1 << i)

# Count number of set bits (1s)
def count_set_bits(num):
    count = 0
    while num:
        num &= (num - 1)  # Clear the least significant set bit
        count += 1
    return count
```

### XOR Properties for Solving Problems

```python
# Find the single non-duplicated number in an array where others appear twice
def find_single(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
# Time: O(n), Space: O(1)
```

---

## Dutch National Flag

An algorithm for three-way partitioning, commonly used for sorting arrays with three distinct values.

```python
def dutch_national_flag(nums, pivot):
    """
    Partition array into three parts:
    - Values less than pivot
    - Values equal to pivot
    - Values greater than pivot
    """
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] < pivot:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] > pivot:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        else:
            mid += 1

    return nums
# Time: O(n), Space: O(1)
```

---

## Boyer-Moore Voting Algorithm

Used to find the majority element (occurring more than n/2 times) in linear time and constant space.

```python
def majority_element(nums):
    candidate = None
    count = 0

    # Find candidate
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    # Verify candidate (optional if guaranteed to have majority)
    count = sum(1 for num in nums if num == candidate)
    return candidate if count > len(nums) // 2 else None
# Time: O(n), Space: O(1)
```

---

## Floyd's Cycle Finding (Tortoise and Hare)

Algorithm for cycle detection in sequences, especially useful for linked lists.

```python
def detect_cycle(head):
    # Phase 1: Detect if there's a cycle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None  # No cycle

    # Phase 2: Find the start of the cycle
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # Cycle start node
# Time: O(n), Space: O(1)
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
