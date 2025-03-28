# Backtracking Algorithms Cheatsheet for SWE Interviews

## Overview

Backtracking is an algorithmic technique that builds solutions incrementally by exploring all possible candidates and abandoning a candidate ("backtracking") when it's determined that it cannot lead to a valid solution.

## When to Use

- Problems requiring exhaustive search of all possible solutions
- Constraint satisfaction problems (e.g., Sudoku, N-Queens)
- When you need to find all combinations, permutations, or subsets
- Problems that involve making sequential decisions with constraints
- Scenarios where you need to explore all paths in a decision tree
- When greedy or dynamic programming approaches aren't applicable
- When the problem involves recursive enumeration of possibilities

## Step 1: Understanding Backtracking

### Key Components

1. **Choice**: What choices do we have at each step?
2. **Constraints**: When do we stop exploring a path?
3. **Goal**: When have we found a valid solution?

### Visualization

Decision tree for generating all subsets of [1,2,3]:

```
                 []
          /      |       \
        [1]     [2]      [3]
       /  \     / \      /
    [1,2] [1,3] [2,3]
     /
 [1,2,3]
```

## Subsets Algorithm

The subsets pattern generates all possible subsets (power set) of a given set/array.

### Implementation

```python
def subsets(nums):
    result = []

    def backtrack(start, current):
        # Add the current subset to our results
        result.append(current[:])

        # Explore all possible candidates
        for i in range(start, len(nums)):
            # Include nums[i] in the current subset
            current.append(nums[i])

            # Move to the next element
            backtrack(i + 1, current)

            # Backtrack - remove nums[i] to try the next candidate
            current.pop()

    backtrack(0, [])
    return result
```

### Variations

#### Subsets with Duplicates

```python
def subsets_with_duplicates(nums):
    result = []
    nums.sort()  # Sort to handle duplicates

    def backtrack(start, current):
        result.append(current[:])

        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i-1]:
                continue

            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
```

#### Subsets of Size K

```python
def subsets_of_size_k(nums, k):
    result = []

    def backtrack(start, current):
        # Base case: we have a subset of size k
        if len(current) == k:
            result.append(current[:])
            return

        # Not enough remaining elements to form a subset of size k
        if len(current) + (len(nums) - start) < k:
            return

        for i in range(start, len(nums)):
            current.append(nums[i])
            backtrack(i + 1, current)
            current.pop()

    backtrack(0, [])
    return result
```

## Combinations Algorithm

The combinations pattern generates all possible combinations of k elements from a set of n elements.

### Implementation

```python
def combinations(n, k):
    result = []

    def backtrack(start, current):
        # Base case: we have a combination of size k
        if len(current) == k:
            result.append(current[:])
            return

        # Explore all possible candidates
        for i in range(start, n + 1):
            # Include i in the current combination
            current.append(i)

            # Move to the next element
            backtrack(i + 1, current)

            # Backtrack - remove i to try the next candidate
            current.pop()

    backtrack(1, [])
    return result
```

### Variations

#### Combination Sum

```python
def combination_sum(candidates, target):
    result = []

    def backtrack(start, current, remaining):
        # Base case: we've found a valid combination
        if remaining == 0:
            result.append(current[:])
            return

        # Base case: remaining sum is negative
        if remaining < 0:
            return

        # Explore all possible candidates
        for i in range(start, len(candidates)):
            current.append(candidates[i])

            # Allow reusing the same element
            backtrack(i, current, remaining - candidates[i])

            current.pop()

    backtrack(0, [], target)
    return result
```

#### Combination Sum II (No Duplicates)

```python
def combination_sum2(candidates, target):
    result = []
    candidates.sort()  # Sort to handle duplicates

    def backtrack(start, current, remaining):
        if remaining == 0:
            result.append(current[:])
            return

        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            # Skip duplicates
            if i > start and candidates[i] == candidates[i-1]:
                continue

            current.append(candidates[i])

            # Each element can be used only once, so move to next index
            backtrack(i + 1, current, remaining - candidates[i])

            current.pop()

    backtrack(0, [], target)
    return result
```

## Permutations Algorithm

The permutations pattern generates all possible arrangements of elements in a set.

### Implementation

```python
def permutations(nums):
    result = []
    n = len(nums)

    def backtrack(current):
        # Base case: we have a full permutation
        if len(current) == n:
            result.append(current[:])
            return

        # Try all remaining elements
        for num in nums:
            # Skip if this element is already used
            if num in current:
                continue

            # Add the number to our current permutation
            current.append(num)

            # Recursively build the rest of the permutation
            backtrack(current)

            # Backtrack
            current.pop()

    backtrack([])
    return result
```

### More Efficient Implementation (Swap-based)

```python
def permutations_swap(nums):
    result = []

    def backtrack(index):
        # Base case: we have a full permutation
        if index == len(nums):
            result.append(nums[:])
            return

        # Try all possibilities for the current position
        for i in range(index, len(nums)):
            # Swap characters
            nums[index], nums[i] = nums[i], nums[index]

            # Recursively build the rest of the permutation
            backtrack(index + 1)

            # Swap back (backtrack)
            nums[index], nums[i] = nums[i], nums[index]

    backtrack(0)
    return result
```

### Variations

#### Permutations with Duplicates

```python
def permutations_with_duplicates(nums):
    result = []
    nums.sort()  # Sort to handle duplicates

    def backtrack(current, used):
        if len(current) == len(nums):
            result.append(current[:])
            return

        for i in range(len(nums)):
            # Skip used elements
            if used[i]:
                continue

            # Skip duplicates
            if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                continue

            used[i] = True
            current.append(nums[i])

            backtrack(current, used)

            used[i] = False
            current.pop()

    backtrack([], [False] * len(nums))
    return result
```

#### Next Permutation

```python
def next_permutation(nums):
    n = len(nums)

    # Find the first decreasing element from the right
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        # Find the element just larger than nums[i]
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1

        # Swap
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse suffix starting at i+1
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums
```

## Interview Tips

- **Time & Space Complexity**:
  - Subsets: O(2^n * n) time, O(n) space (excluding output)
  - Combinations: O(C(n,k) * k) time, O(k) space (excluding output)
  - Permutations: O(n! * n) time, O(n) space (excluding output)

- **Template Approach**:
  1. Define a recursive backtracking function
  2. Add base case to know when to stop and add to the result
  3. Iterate through all possible choices at current step
  4. For each choice:
     - Make the choice
     - Recursively explore further
     - Undo the choice (backtrack)

- **Optimization Tips**:
  - Prune early: Check constraints as soon as possible
  - Avoid unnecessary copies: Use references where possible
  - Sort the input when duplicates are present
  - Use swapping for permutations instead of tracking used elements

- **Edge Cases**:
  - Empty input
  - Single element
  - Duplicate elements
  - Negative numbers (for sum-related problems)

## Common Interview Questions

1. Subsets (LeetCode #78)
2. Subsets II (LeetCode #90)
3. Combinations (LeetCode #77)
4. Combination Sum (LeetCode #39)
5. Combination Sum II (LeetCode #40)
6. Permutations (LeetCode #46)
7. Permutations II (LeetCode #47)
8. Palindrome Partitioning (LeetCode #131)
9. Letter Combinations of a Phone Number (LeetCode #17)
10. N-Queens (LeetCode #51)
11. Sudoku Solver (LeetCode #37)
12. Generate Parentheses (LeetCode #22)
