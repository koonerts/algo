# Kadane's Algorithm Cheatsheet for SWE Interviews

> **Difficulty**: ⭐⭐ Medium

## Overview

Kadane's algorithm efficiently finds the maximum sum contiguous subarray within a one-dimensional array of numbers. It uses dynamic programming to track the maximum sum ending at each position.

## When to Use

- Finding maximum/minimum sum subarray
- Problems requiring contiguous elements with optimal value
- When you need O(n) solution for subarray sum problems

## Step 1: Understanding Kadane's Algorithm

Kadane's algorithm finds the maximum sum subarray in a one-dimensional array by making a single pass through the array.

### Key Insight

At each position, we have two choices:

1. Start a new subarray from current position
2. Extend the previous subarray by including current element

### Visualization

For array: `[-2, 1, -3, 4, -1, 2, 1, -5, 4]`

```
Index:     0   1   2   3   4   5   6   7   8
Array:    -2   1  -3   4  -1   2   1  -5   4
Current:  -2   1  -2   4   3   5   6   1   5
Max:      -2   1   1   4   4   5   6   6   6
```

Maximum subarray: `[4, -1, 2, 1]` with sum = 6

## Step 2: Basic Implementation (Brute Force)

```python
def brute_force_max_subarray(nums):
    n = len(nums)
    max_sum = float('-inf')

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)

    return max_sum
# Time: O(n²), Space: O(1)

# Test cases
if __name__ == "__main__":
    # Example 1: Standard case with positive and negative numbers
    test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # Expected: 6 (subarray [4, -1, 2, 1])
    print(f"Test 1 result: {brute_force_max_subarray(test1)}")

    # Example 2: All negative numbers
    test2 = [-1, -2, -3, -4]
    # Expected: -1 (subarray [-1])
    print(f"Test 2 result: {brute_force_max_subarray(test2)}")

    # Example 3: All positive numbers
    test3 = [1, 2, 3, 4]
    # Expected: 10 (entire array)
    print(f"Test 3 result: {brute_force_max_subarray(test3)}")
```

## Step 3: Optimized Kadane's Algorithm

```python
def kadane(nums):
    max_so_far = float('-inf')
    max_ending_here = 0

    for num in nums:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
# Time: O(n), Space: O(1)

# Test cases
if __name__ == "__main__":
    # Example 1: Standard case with positive and negative numbers
    test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # Expected: 6 (subarray [4, -1, 2, 1])
    print(f"Test 1 result: {kadane(test1)}")

    # Example 2: All negative numbers
    test2 = [-1, -2, -3, -4]
    # Expected: -1 (subarray [-1])
    print(f"Test 2 result: {kadane(test2)}")

    # Example 3: All positive numbers
    test3 = [1, 2, 3, 4]
    # Expected: 10 (entire array)
    print(f"Test 3 result: {kadane(test3)}")

    # Compare brute force vs optimized results
    for test in [test1, test2, test3]:
        bf_result = brute_force_max_subarray(test)
        kadane_result = kadane(test)
        assert bf_result == kadane_result, f"Results don't match for {test}"
    print("All tests passed! Brute force and Kadane's algorithm give same results.")
```

## Step 4: Common Variations

### Return Subarray Indices

```python
def kadane_with_indices(nums):
    max_so_far = float('-inf')
    max_ending_here = 0
    start = 0
    end = 0
    s = 0  # potential start

    for i, num in enumerate(nums):
        max_ending_here += num

        if max_ending_here < 0:
            max_ending_here = 0
            s = i + 1
        elif max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = s
            end = i

    return max_so_far, start, end

# Test cases
if __name__ == "__main__":
    # Example 1: Standard case with positive and negative numbers
    test1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum, start, end = kadane_with_indices(test1)
    print(f"Max sum: {max_sum}, Subarray: {test1[start:end+1]} (indices {start}-{end})")
    # Expected: Max sum: 6, Subarray: [4, -1, 2, 1] (indices 3-6)

    # Example 2: All positive numbers
    test2 = [1, 2, 3, 4]
    max_sum, start, end = kadane_with_indices(test2)
    print(f"Max sum: {max_sum}, Subarray: {test2[start:end+1]} (indices {start}-{end})")
    # Expected: Max sum: 10, Subarray: [1, 2, 3, 4] (indices 0-3)

    # Example 3: Test with a different pattern
    test3 = [5, -4, 3, 4, -2, 1, 7, -8, 6]
    max_sum, start, end = kadane_with_indices(test3)
    print(f"Max sum: {max_sum}, Subarray: {test3[start:end+1]} (indices {start}-{end})")
    # Expected: Max sum: 13, Subarray: [5, -4, 3, 4, -2, 1, 7] or [3, 4, -2, 1, 7] (depends on implementation)
```

### Handling All Negative Numbers

```python
def kadane_all_negative(nums):
    max_so_far = nums[0]
    max_ending_here = nums[0]

    for num in nums[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far

# Test cases
if __name__ == "__main__":
    # Example 1: All negative numbers
    test1 = [-1, -2, -3, -4]
    print(f"Max sum: {kadane_all_negative(test1)}")
    # Expected: -1 (the largest single element)

    # Example 2: Mixed numbers with negative result
    test2 = [-5, -1, -8, -9]
    print(f"Max sum: {kadane_all_negative(test2)}")
    # Expected: -1

    # Example 3: Negative and positive numbers
    test3 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(f"Max sum: {kadane_all_negative(test3)}")
    # Expected: 6

    # Check if standard Kadane fails but all-negative version works
    test4 = [-10, -5, -2, -1, -7]
    standard_result = kadane(test4) if 'kadane' in globals() else float('-inf')
    all_neg_result = kadane_all_negative(test4)
    print(f"Standard Kadane: {standard_result}, All-negative version: {all_neg_result}")
```

### Circular Array Maximum Sum

```python
def max_circular_subarray(nums):
    # Case 1: Max subarray does not wrap around
    max_kadane = kadane(nums)

    # Case 2: Max subarray wraps around
    total_sum = sum(nums)
    # Invert signs to find minimum subarray
    inverted = [-x for x in nums]
    # Maximum wrap-around sum = total sum - minimum subarray sum
    max_wrap = total_sum + kadane(inverted)

    # Edge case: All negative values
    if max_wrap == 0:
        return max_kadane

    return max(max_kadane, max_wrap)
```

### 2D Version: Maximum Sum Submatrix

```python
def max_submatrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    max_sum = float('-inf')

    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            # Update temp to represent submatrix from left to right
            for i in range(rows):
                temp[i] += matrix[i][right]

            # Apply Kadane on temp array
            current_max = kadane(temp)
            max_sum = max(max_sum, current_max)

    return max_sum
```

### Maximum Product Subarray

```python
def max_product_subarray(nums):
    if not nums:
        return 0

    max_product = min_product = result = nums[0]

    for num in nums[1:]:
        max_product, min_product = max(num, max_product * num, min_product * num), min(num, max_product * num, min_product * num)
        result = max(result, max_product)

    return result
```

## Interview Tips

- **Time & Space Complexity**:
  - Kadane's algorithm: O(n) time, O(1) space

- **Edge Cases**:
  - Empty array
  - All negative numbers
  - Single element array

- **Common Patterns**:
  - Dynamic programming (local vs global optimum)
  - Greedy approach aspect (extending the current subarray)

- **Follow-up Questions**:
  - What if we need to find the minimum sum subarray?
  - What if the array is circular?
  - Can we solve it without modifying the original array?

## Common Mistakes

- **Initialization Error**: Forgetting to initialize `max_so_far` to the first element rather than negative infinity when dealing with arrays that might contain all negative values
- **Not Handling Empty Arrays**: Failing to check if the array is empty before processing
- **Incorrect Subarray Tracking**: When tracking subarray indices, forgetting to update them at the right time
- **Confusion with Circular Arrays**: Misunderstanding how to handle the circular case (missing the edge case where all values are negative)

## Multi-language Implementation

### Go Implementation

```go
func maxSubArray(nums []int) int {
    maxSoFar := nums[0]
    maxEndingHere := nums[0]

    for i := 1; i < len(nums); i++ {
        maxEndingHere = max(nums[i], maxEndingHere + nums[i])
        maxSoFar = max(maxSoFar, maxEndingHere)
    }

    return maxSoFar
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
```

## Practice Problems

### Easy ⭐

- Maximum Subarray (LeetCode #53) - Find the contiguous subarray with the largest sum
- Best Time to Buy and Sell Stock (LeetCode #121) - Apply Kadane's to find maximum profit

### Medium ⭐⭐

- Maximum Sum Circular Subarray (LeetCode #918) - Handle wrapping around the array
- Maximum Product Subarray (LeetCode #152) - Adapt for multiplication instead of addition

### Hard ⭐⭐⭐

- Maximum Sum Rectangle in a 2D Matrix (variant of LeetCode #363) - Apply in 2D context
- Maximum Absolute Sum of Any Subarray (LeetCode #1749) - Find both maximum and minimum

## Further Reading

- [The Maximum Subarray Problem - Algorithms with Attitude](https://algorithmsattitude.com/maximum-subarray-problem/)
- [Dynamic Programming - Maximum Subarray Problem](https://en.wikipedia.org/wiki/Maximum_subarray_problem)
- [Kadane's Algorithm - cp-algorithms](https://cp-algorithms.com/sequences/maximum_subarray.html)

---

# Sliding Window Fixed Size Algorithm Cheatsheet

> **Difficulty**: ⭐ Easy

## Overview

The fixed-size sliding window algorithm is a technique for processing arrays or strings by maintaining a window of fixed size `k` that moves from left to right. It's particularly efficient for computing running statistics over a dataset.

## When to Use

- Computing running averages, sums, or statistics over a fixed-size range
- Finding subarrays/substrings of fixed length with certain properties
- Problems requiring consecutive elements with fixed count
- When you need to avoid recomputation of overlapping elements

## Step 1: Understanding and Visualization

The fixed-size sliding window algorithm maintains a subarray/substring of constant length `k` that "slides" through the data from left to right, updating results at each step.

### Key Insight

Instead of recomputing the entire window contents at each step, we only:

1. Add the new element entering the window
2. Remove the oldest element leaving the window

### Visualization

```
Array: [1, 3, 5, 7, 9, 11] with window size k=3

Initial window: [1, 3, 5] (sum = 9)
             ↓
Slide 1:      [3, 5, 7] (sum = 15)  // Remove 1, add 7
                ↓
Slide 2:         [5, 7, 9] (sum = 21)  // Remove 3, add 9
                   ↓
Slide 3:            [7, 9, 11] (sum = 27)  // Remove 5, add 11
```

## Step 2: Brute Force Approach

```python
def brute_force(arr, k):
    n = len(arr)
    max_sum = float('-inf')

    # Check every possible window of size k
    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum += arr[i + j]
        max_sum = max(max_sum, current_sum)

    return max_sum
```

Time Complexity: O(n*k)

## Step 3: Optimized Solution Template

```python
def sliding_window(arr, k):
    # 1. Initialize window and result
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # 2. Slide window from left to right
    for i in range(k, len(arr)):
        # 3. Update window: add new element, remove oldest
        window_sum = window_sum + arr[i] - arr[i-k]

        # 4. Update result
        max_sum = max(max_sum, window_sum)

    return max_sum
```

Time Complexity: O(n)
Space Complexity: O(1)

## Common Problem Patterns

### 1. Maximum Sum Subarray of Size K

```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum + arr[i] - arr[i-k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### 2. Average of Subarrays of Size K

```python
def find_averages(arr, k):
    result = []
    window_sum = sum(arr[:k])
    result.append(window_sum/k)

    for i in range(k, len(arr)):
        window_sum = window_sum + arr[i] - arr[i-k]
        result.append(window_sum/k)

    return result
```

### 3. Count Occurrences of Anagrams

```python
from collections import Counter

def count_anagrams(text, pattern):
    result = 0
    pattern_count = Counter(pattern)
    window_count = Counter(text[:len(pattern)])

    if window_count == pattern_count:
        result += 1

    for i in range(len(pattern), len(text)):
        # Add new character
        window_count[text[i]] += 1
        # Remove oldest character
        window_count[text[i-len(pattern)]] -= 1

        # Clean up counter
        if window_count[text[i-len(pattern)]] == 0:
            del window_count[text[i-len(pattern)]]

        if window_count == pattern_count:
            result += 1

    return result
```

### 4. Maximum of All Subarrays of Size K

```python
from collections import deque

def max_of_subarrays(arr, k):
    result = []
    window = deque()  # Will store indices

    for i in range(len(arr)):
        # Remove elements outside current window
        while window and window[0] <= i - k:
            window.popleft()

        # Remove smaller elements (they won't be maximum)
        while window and arr[window[-1]] < arr[i]:
            window.pop()

        window.append(i)

        # Add maximum of current window to result
        if i >= k - 1:
            result.append(arr[window[0]])

    return result
```

## Interview Tips

- **Identify the window**: Always clarify if you're dealing with a fixed or variable-sized window.
- **Initialization**: Remember to initialize your window with the first k elements.
- **Efficient updates**: The key optimization is updating the window in O(1) time by adding new elements and removing old ones.
- **Data structure choice**: Use arrays for simple counting, hashmaps for character frequency, or deques for maintaining order with efficient operations at both ends.
- **Edge cases**: Handle empty arrays and k values greater than array length.

## Complexity Analysis

- **Time Complexity**: O(n) for most implementations, where n is the array length
- **Space Complexity**: Typically O(1) or O(k) depending on what you store

## Common Mistakes

- **Off-by-one errors**: Miscalculating the window boundaries, especially at the beginning and end of the array
- **Not handling edge cases**: Forgetting to check if k > array length
- **Inefficient updates**: Recomputing the entire window sum instead of just updating with new/old elements
- **Incorrect initialization**: Not properly initializing the first window before sliding

## Multi-language Implementation

### Java Implementation

```java
public double[] findAverages(int[] arr, int k) {
    double[] result = new double[arr.length - k + 1];
    double windowSum = 0;
    int windowStart = 0;

    for (int windowEnd = 0; windowEnd < arr.length; windowEnd++) {
        windowSum += arr[windowEnd]; // Add the next element

        // When we hit the window size, calculate average and slide the window
        if (windowEnd >= k - 1) {
            result[windowStart] = windowSum / k;
            windowSum -= arr[windowStart]; // Remove the element going out
            windowStart++; // Slide the window
        }
    }

    return result;
}
```

### JavaScript Implementation

```javascript
function findAverages(arr, k) {
    const result = [];
    let windowSum = 0;
    let windowStart = 0;

    for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
        windowSum += arr[windowEnd];

        if (windowEnd >= k - 1) {
            result.push(windowSum / k);
            windowSum -= arr[windowStart];
            windowStart++;
        }
    }

    return result;
}
```

## Practice Problems

### Easy ⭐

- Find Maximum Average Subarray I (LeetCode #643)
- Containing Duplicates II (LeetCode #219) - Find if duplicates are within k distance

### Medium ⭐⭐

- Count Subarrays with Product Less Than K (LeetCode #713)
- Frequency of the Most Frequent Element (LeetCode #1838)

### Hard ⭐⭐⭐

- Sliding Window Maximum (LeetCode #239) - Find maximums in each window using deque

## Further Reading

- [Sliding Window Technique - GeeksforGeeks](https://www.geeksforgeeks.org/window-sliding-technique/)
- [Sliding Window Algorithm - Medium](https://medium.com/techie-delight/sliding-window-algorithm-technique-8c92cdbeedda)
- [Efficient Sliding Window Implementations - CP-Algorithms](https://cp-algorithms.com/string/z-function.html)

---

# Sliding Window (Variable Size) Cheatsheet

**Overview:**

- Technique to find subarrays/substrings that satisfy certain conditions
- Window size changes dynamically based on conditions
- Time complexity typically O(n) as elements are processed at most twice

**Key Concepts:**

- Two pointers (left, right) define window boundaries
- Expand window by moving right pointer when more elements needed
- Contract window by moving left pointer when conditions are violated

**Template:**

```python
def sliding_window_variable(arr, condition):
    left = 0
    result = initial_value
    current_state = {}  # or other tracking mechanism

    for right in range(len(arr)):
        # Expand window by including arr[right]
        # Update current_state

        # Contract window if needed
        while condition_to_shrink:
            # Remove arr[left] from window consideration
            # Update current_state
            left += 1

        # Update result based on current window

    return result
```

**Common Problems:**

```python
# Minimum Size Subarray Sum
def min_subarray_with_sum(nums, target):
    left, current_sum, min_length = 0, 0, float('inf')

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum >= target:
            min_length = min(min_length, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return min_length if min_length != float('inf') else 0

# Longest Substring with K Distinct Characters
def longest_substring_with_k_distinct(s, k):
    left, max_length = 0, 0
    char_count = {}

    for right in range(len(s)):
        char_count[s[right]] = char_count.get(s[right], 0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length
```

# Two Pointers Cheatsheet

**Overview:**

- Uses two pointers to solve problems in linear time O(n)
- Eliminates need for nested loops in many scenarios
- Pointers can move in same or opposite directions

**Key Patterns:**

- From both ends: left → | ← right
- Same direction: slow → fast →
- Fast/slow: slow → fast →→ (different speeds)

**Template - From Both Ends:**

```python
def two_pointers_from_ends(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        # Process elements at left and right

        if condition:
            left += 1
        else:
            right -= 1

    return result
```

**Template - Same Direction:**

```python
def two_pointers_same_direction(arr):
    slow = 0

    for fast in range(len(arr)):
        # Process using both pointers

        if condition:
            # Update slow pointer (often with swap or assignment)
            slow += 1

    return result
```

**Common Problems:**

```python
# Two Sum (sorted array)
def two_sum_sorted(numbers, target):
    left, right = 0, len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            return [left + 1, right + 1]  # 1-indexed
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]

# Remove Duplicates from Sorted Array
def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1  # Length of deduplicated array
```

# Prefix Sums Cheatsheet

**Overview:**

- Precompute cumulative sums to efficiently answer range queries
- Transforms O(n) range sum operations into O(1)
- Enables efficient subarray sum calculations

**Key Concepts:**

- prefix_sum[i] = sum of all elements from index 0 to i-1
- Sum of range [i,j] = prefix_sum[j+1] - prefix_sum[i]
- Often uses a hashmap to track seen prefix sums

**Template:**

```python
def prefix_sum_setup(arr):
    n = len(arr)
    prefix = [0] * (n + 1)  # +1 for convenience

    for i in range(n):
        prefix[i+1] = prefix[i] + arr[i]

    return prefix

# Get sum of range [i,j] inclusive (0-indexed)
def range_sum(prefix, i, j):
    return prefix[j+1] - prefix[i]
```

**Common Problems:**

```python
# Range Sum Query
class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right+1] - self.prefix[left]

# Subarray Sum Equals K
def subarray_sum_equals_k(nums, k):
    count = 0
    current_sum = 0
    prefix_counts = {0: 1}  # Empty subarray has sum 0

    for num in nums:
        current_sum += num
        # If we've seen (current_sum - k) before, we found subarrays with sum k
        if current_sum - k in prefix_counts:
            count += prefix_counts[current_sum - k]

        prefix_counts[current_sum] = prefix_counts.get(current_sum, 0) + 1

    return count
```

**Variations:**

- 2D prefix sums for matrix range queries
- Combine with modular arithmetic for divisibility problems
- Use with two pointers for optimized subarray problems
