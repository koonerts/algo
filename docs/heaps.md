# Heaps Algorithms Cheatsheet for SWE Interviews

## When to Use

- When you need to repeatedly find the minimum or maximum element efficiently
- When processing elements in order of priority or importance
- When tracking statistics about the median or middle elements of a dataset
- In streaming data scenarios where you need running statistics
- For implementing priority queues in algorithms like Dijkstra's or Prim's
- When you need to efficiently merge multiple sorted lists (using min heap)
- For problems requiring "top-k" or "k-largest/smallest" elements
- When balancing workloads or distributing resources optimally
- For efficient implementation of scheduling algorithms
- When you need to maintain a sorted subset of a larger collection

## Two Heaps Algorithm

The Two Heaps pattern uses two heaps (usually a min-heap and a max-heap) to efficiently track elements like medians or balancing values in a stream.

### Step 1: Understanding the Pattern

- **Max Heap**: Stores the smaller half of elements (allows access to the largest of the smaller half)
- **Min Heap**: Stores the larger half of elements (allows access to the smallest of the larger half)
- By balancing these heaps, we can efficiently track statistics about the middle of our data

### Step 2: Visualization

For finding the median of a stream of numbers:

```
Stream: [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]

After processing [5]:
Max Heap: [5]
Min Heap: []
Median: 5

After processing [5, 15]:
Max Heap: [5]
Min Heap: [15]
Median: (5 + 15) / 2 = 10

After processing [5, 15, 1]:
Max Heap: [5, 1]
Min Heap: [15]
Median: 5

After processing [5, 15, 1, 3]:
Max Heap: [5, 1, 3]
Min Heap: [15]
Median: 5

...and so on, constantly rebalancing the heaps.
```

### Step 3: Basic Implementation - Median Finder

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (negative values)
        self.large = []  # Min heap

    def addNum(self, num):
        # Add to max heap (smaller half)
        heapq.heappush(self.small, -num)

        # Ensure every element in small is <= every element in large
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Balance the heaps (at most 1 element difference)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        else:
            return (-self.small[0] + self.large[0]) / 2
```

### Step 4: Common Variations

#### Sliding Window Median

```python
def sliding_window_median(nums, k):
    result = []
    small = []  # Max heap (negative values)
    large = []  # Min heap

    # Helper function to remove element from either heap
    def remove(heap, element):
        index = heap.index(element)
        heap[index] = heap[-1]
        heap.pop()
        if index < len(heap):
            heapq._siftup(heap, index)
            heapq._siftdown(heap, 0, index)

    for i, num in enumerate(nums):
        # Add to heaps
        heapq.heappush(small, -num)

        # Balance step 1: Ensure small elements < large elements
        heapq.heappush(large, -heapq.heappop(small))

        # Balance step 2: Ensure size difference is at most 1
        if len(small) < len(large):
            heapq.heappush(small, -heapq.heappop(large))

        # If window is full size
        if i >= k - 1:
            # Calculate median
            if k % 2 == 1:
                result.append(-small[0])
            else:
                result.append((-small[0] + large[0]) / 2)

            # Remove the outgoing element
            outgoing = nums[i - k + 1]
            if outgoing <= -small[0]:
                remove(small, -outgoing)
            else:
                remove(large, outgoing)

            # Rebalance if necessary
            if len(small) > len(large) + 1:
                heapq.heappush(large, -heapq.heappop(small))
            elif len(large) > len(small):
                heapq.heappush(small, -heapq.heappop(large))

    return result
```

#### Maximum Capital for Projects

```python
def find_maximum_capital(capitals, profits, num_projects, initial_capital):
    n = len(capitals)
    current_capital = initial_capital

    # Min heap for capitals (projects we can afford)
    capital_min_heap = [(capitals[i], i) for i in range(n)]
    heapq.heapify(capital_min_heap)

    # Max heap for profits (negate for max heap in Python)
    profit_max_heap = []

    # Execute 'num_projects' projects
    for _ in range(num_projects):
        # Select projects we can afford
        while capital_min_heap and capital_min_heap[0][0] <= current_capital:
            capital, index = heapq.heappop(capital_min_heap)
            heapq.heappush(profit_max_heap, -profits[index])

        # If no project can be selected, break
        if not profit_max_heap:
            break

        # Execute the most profitable project
        current_capital += -heapq.heappop(profit_max_heap)

    return current_capital
```

#### Next Interval

```python
def find_next_interval(intervals):
    n = len(intervals)
    result = [-1] * n

    # Create max heap for end points
    end_max_heap = [(-intervals[i][1], i) for i in range(n)]
    heapq.heapify(end_max_heap)

    # Create max heap for start points
    start_max_heap = [(-intervals[i][0], i) for i in range(n)]
    heapq.heapify(start_max_heap)

    while end_max_heap:
        # Get interval with the largest end
        end, end_idx = heapq.heappop(end_max_heap)
        end = -end  # Convert back to positive

        # Save all start points that are greater than current end
        temp = []
        answer = -1

        # Find smallest start greater than or equal to current end
        while start_max_heap and -start_max_heap[0][0] >= end:
            start, start_idx = heapq.heappop(start_max_heap)
            # If this is a better start (smaller)
            if answer == -1 or -start < intervals[answer][0]:
                answer = start_idx
            temp.append((start, start_idx))

        # Push back all starts we popped
        for start_pair in temp:
            heapq.heappush(start_max_heap, start_pair)

        result[end_idx] = answer

    return result
```

## Interview Tips

- **Time & Space Complexity**:
  - Insertion/removal: O(log n)
  - Peek at top element: O(1)
  - Building a heap: O(n)
  - Space: O(n) for storing n elements

- **Edge Cases**:
  - Empty stream or single element
  - Even vs. odd number of elements
  - Duplicates in the stream

- **Balancing Strategies**:
  - Always ensure the size difference between heaps is at most 1
  - Make sure every element in the smaller half is <= every element in the larger half
  - Decide which heap should have the extra element if there's an odd number

- **Python Heap Implementation Notes**:
  - Python's heapq is a min-heap
  - For max-heap, negate values when inserting/removing
  - For custom objects, define `__lt__` method or use a tuple with the priority first
  - No built-in "remove" from middle of heap - use lazy deletion or custom implementation

## Common Interview Questions

1. Find Median from Data Stream (LeetCode #295)
2. Sliding Window Median (LeetCode #480)
3. IPO (LeetCode #502) - Maximum Capital
4. Find Right Interval (LeetCode #436) - Next Interval
5. Meeting Rooms II (LeetCode #253) - Can use two heaps approach
6. Task Scheduler (LeetCode #621) - Can use max heap
7. Reorganize String (LeetCode #767) - Max heap approach
8. K Closest Points to Origin (LeetCode #973) - Min heap approach
9. Top K Frequent Elements (LeetCode #347) - Min heap approach
10. Kth Largest Element in a Stream (LeetCode #703) - Min heap

## Real-world Applications

- **Median Finder**: Real-time analytics, streaming data processing
- **Two Heaps**: Resource allocation problems, scheduling problems with priorities
- **Priority Scheduling**: Operating systems, networking packets, task management
- **Load Balancing**: System design for distributing requests across servers
