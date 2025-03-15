# Dynamic Programming Algorithms Cheatsheet for SWE Interviews

## When to Use

- Problems with overlapping subproblems (computed results can be reused)
- Problems with optimal substructure (optimal solution can be built from optimal solutions of subproblems)
- When you need to find a minimum, maximum, or optimal count
- Optimization problems where you need to make choices to achieve the best result
- When a problem can be broken down recursively, but direct recursion would be too slow
- Problems involving sequences (arrays, strings) where decision at each step depends on previous decisions
- Resource allocation problems with constraints
- Many counting problems (number of ways to achieve a certain goal)
- When the problem exhibits the principle of choice (take or not take an item)

## 0/1 Knapsack Problem

The 0/1 Knapsack problem involves selecting items with given weights and values to maximize total value without exceeding a weight capacity.

### Visualization

```
Items: [(weight=1, value=6), (weight=2, value=10), (weight=3, value=12)]
Capacity: 5

DP Table:
    0   1   2   3   4   5   <- Capacity
0   0   0   0   0   0   0
1   0   6   6   6   6   6   <- Consider item 1 only
2   0   6  10  16  16  16   <- Consider items 1-2
3   0   6  10  16  18  22   <- Consider items 1-3

Maximum value: 22
```

### Implementation - Bottom-Up

```python
def knapsack_01(weights, values, capacity):
    n = len(weights)
    # Initialize DP table with zeros
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # If current item is too heavy, skip it
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                # Max of (1) not taking item or (2) taking item
                dp[i][w] = max(dp[i-1][w], 
                               dp[i-1][w-weights[i-1]] + values[i-1])
    
    # Return maximum value
    return dp[n][capacity]
```

### Space Optimization

```python
def knapsack_01_optimized(weights, values, capacity):
    n = len(weights)
    # Use only 1D array
    dp = [0] * (capacity + 1)
    
    for i in range(n):
        # Iterate in reverse to avoid using items multiple times
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
            
    return dp[capacity]
```

### Reconstructing the Solution

```python
def knapsack_01_with_items(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], 
                               dp[i-1][w-weights[i-1]] + values[i-1])
    
    # Reconstruct solution
    w = capacity
    selected_items = []
    
    for i in range(n, 0, -1):
        # If item i is included
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)
            w -= weights[i-1]
            
    return dp[n][capacity], selected_items
```

### Time & Space Complexity

- **Time**: O(n * W) where n is number of items and W is capacity
- **Space**: O(n * W) for 2D DP, O(W) for optimized solution

## Unbounded Knapsack

Unlike 0/1 Knapsack, the Unbounded version allows using each item any number of times.

### Visualization

```
Items: [(weight=1, value=15), (weight=3, value=50), (weight=4, value=60)]
Capacity: 8

DP Table:
    0   1   2   3   4   5   6   7   8   <- Capacity
    0  15  30  45  60  75  90 105 120   <- Max value
```

### Implementation

```python
def unbounded_knapsack(weights, values, capacity):
    n = len(weights)
    # Initialize DP array
    dp = [0] * (capacity + 1)
    
    # Fill the DP array
    for w in range(1, capacity + 1):
        for i in range(n):
            if weights[i] <= w:
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
                
    return dp[capacity]
```

### Variations

#### Rod Cutting Problem

```python
def rod_cutting(prices, rod_length):
    # prices[i] is the price of a rod of length i+1
    dp = [0] * (rod_length + 1)
    
    for length in range(1, rod_length + 1):
        for cut in range(1, min(length, len(prices)) + 1):
            dp[length] = max(dp[length], dp[length - cut] + prices[cut - 1])
            
    return dp[rod_length]
```

#### Coin Change Problem (Minimum Coins)

```python
def min_coins(coins, amount):
    # Initialize with infinity
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
            
    return dp[amount] if dp[amount] != float('inf') else -1
```

### Time & Space Complexity

- **Time**: O(n * W) where n is number of items and W is capacity
- **Space**: O(W)

## Longest Common Subsequence (LCS)

LCS finds the longest subsequence that appears in the same relative order within two sequences.

### Visualization

```
Strings: "ABCBDAB" and "BDCABA"
LCS: "BCBA" (length 4)

DP Table:
      ""  B  D  C  A  B  A
   "" 0  0  0  0  0  0  0
    A 0  0  0  0  1  1  1
    B 0  1  1  1  1  2  2
    C 0  1  1  2  2  2  2
    B 0  1  1  2  2  3  3
    D 0  1  2  2  2  3  3
    A 0  1  2  2  3  3  4
    B 0  1  2  2  3  4  4
```

### Implementation

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

### Reconstructing the LCS

```python
def print_lcs(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Reconstruct LCS
    lcs = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            lcs.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    return ''.join(reversed(lcs))
```

### Variations

#### Longest Common Substring

```python
def longest_common_substring(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    max_length = 0
    end_position = 0
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                
                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_position = i
                    
    return text1[end_position - max_length:end_position]
```

#### Shortest Common Supersequence

```python
def shortest_common_supersequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill DP table for LCS
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    # Construct the SCS
    scs = []
    i, j = m, n
    
    while i > 0 and j > 0:
        if text1[i-1] == text2[j-1]:
            scs.append(text1[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            scs.append(text1[i-1])
            i -= 1
        else:
            scs.append(text2[j-1])
            j -= 1
    
    # Add remaining characters
    while i > 0:
        scs.append(text1[i-1])
        i -= 1
    while j > 0:
        scs.append(text2[j-1])
        j -= 1
        
    return ''.join(reversed(scs))
```

### Time & Space Complexity

- **Time**: O(m * n) where m and n are the string lengths
- **Space**: O(m * n)

## Palindrome Problems

### Longest Palindromic Subsequence

Finds the longest subsequence that is also a palindrome.

```python
def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    
    # Every single character is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1
    
    # Fill DP table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j] and length == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    
    return dp[0][n-1]
```

### Longest Palindromic Substring

```python
def longest_palindromic_substring(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    
    start = 0
    max_length = 1
    
    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True
    
    # Check for 2 character strings
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            start = i
            max_length = 2
    
    # Check lengths 3 and above
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                
                if length > max_length:
                    start = i
                    max_length = length
    
    return s[start:start + max_length]
```

### Palindromic Substrings Count

```python
def count_palindromic_substrings(s):
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    count = 0
    
    # All single characters are palindromes
    for i in range(n):
        dp[i][i] = True
        count += 1
    
    # Check for 2 character strings
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            count += 1
    
    # Check lengths 3 and above
    for length in range(3, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                count += 1
    
    return count
```

### Minimum Insertions to Make Palindrome

```python
def min_insertions_to_palindrome(s):
    n = len(s)
    
    # Find the length of longest palindromic subsequence
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        dp[i][i] = 1
        
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2 if i + 1 <= j - 1 else 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    
    # Minimum insertions = length of string - length of longest palindromic subsequence
    return n - dp[0][n - 1]
```

### Time & Space Complexity

- **Longest Palindromic Subsequence**: O(n²) time, O(n²) space
- **Longest Palindromic Substring**: O(n²) time, O(n²) space
- **Count Palindromic Substrings**: O(n²) time, O(n²) space

## Interview Tips

- **0/1 Knapsack**:
  - Classic choice problem: take or don't take
  - Space optimization by using 1D array and iterating backward
  - Practice reconstructing the actual items chosen

- **Unbounded Knapsack**:
  - Similar to 0/1, but can reuse items
  - Iterate forward through the capacity to allow for reuse
  - Often used in problems like coin change, cutting problems

- **LCS**:
  - Base case: empty string has LCS of 0
  - Transition: either characters match (add to LCS) or they don't (take max)
  - Often a subproblem in other string DP problems

- **Palindromes**:
  - Build on smaller palindromes: dp[i][j] depends on dp[i+1][j-1]
  - Two types: subsequence (can skip chars) vs substring (must be consecutive)
  - Consider optimizations like expanding around centers for palindromic substrings

- **General DP Tips**:
  - Start with the recursive solution, identify overlapping subproblems
  - Convert to bottom-up DP to avoid stack overflow and improve efficiency
  - Look for space optimization opportunities
  - Practice reconstructing the actual solution, not just the optimal value

## Common Interview Questions

1. 0/1 Knapsack (Standard)
2. Partition Equal Subset Sum (LeetCode #416) - Special case of 0/1 Knapsack
3. Coin Change (LeetCode #322) - Unbounded Knapsack variant
4. Longest Common Subsequence (LeetCode #1143)
5. Longest Palindromic Substring (LeetCode #5)
6. Palindromic Substrings (LeetCode #647)
7. Edit Distance (LeetCode #72) - Combination of LCS and insertion/deletion concepts
8. Interleaving String (LeetCode #97) - String DP 
9. Minimum Insertion Steps to Make a String Palindrome (LeetCode #1312)
10. Longest Increasing Subsequence (LeetCode #300) - Related DP pattern