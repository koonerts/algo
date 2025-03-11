# Algorithm Learning Acceleration Plan

## Strategic Learning Framework

This plan is designed to help you efficiently learn and internalize algorithm patterns for technical interviews with maximum retention and minimal time investment.

## Priority Tiers (Focus on Highest ROI First)

### Tier 1 (Must Master)
- **Arrays & Strings**: 
  - [Sliding Window (Fixed)](arrays.md#sliding-window-fixed-size-algorithm-cheatsheet) & [Variable](arrays.md#sliding-window-variable-size-cheatsheet)
  - [Two Pointers](arrays.md#two-pointers-cheatsheet)
  - [Prefix Sums](arrays.md#prefix-sums-cheatsheet)
  - [Kadane's Algorithm](arrays.md#kadanes-algorithm-cheatsheet-for-swe-interviews)
- **Binary Search**: [Standard implementation and variants](additional-patterns.md#binary-search-variations)
- **Graph Traversals**: [BFS](additional-patterns.md#bfs-for-shortest-path-in-unweighted-graph) & [DFS](trees.md#iterative-dfs-depth-first-search) fundamentals
- **Linked Lists**: [Fast & Slow Pointers pattern](linked-lists.md#fast--slow-pointers-algorithm)
- **Hash Table Techniques**: Frequency counters, maps
- **Basic Dynamic Programming**: 
  - [0/1 Knapsack pattern](dynamic-programming.md#01-knapsack-problem)
  - [Longest Common Subsequence](dynamic-programming.md#longest-common-subsequence-lcs)

### Tier 2 (High Value)
- **Backtracking**: [Subsets](backtracking.md#subsets-algorithm), [Combinations](backtracking.md#combinations-algorithm), [Permutations](backtracking.md#permutations-algorithm)
- **Two Heaps Pattern**: [Median finding and similar problems](heaps.md#two-heaps-algorithm)
- **Monotonic Stack/Queue**: [Next greater element, histogram problems](additional-patterns.md#monotonic-stackqueue)
- **Union-Find (Disjoint Set)**: [Connected components, cycle detection](trees.md#union-find-disjoint-set)
- **Bit Manipulation**: [Basic operations and patterns](additional-patterns.md#bit-manipulation-techniques)
- **Greedy Algorithms**: [Activity selection, interval merging](additional-patterns.md#greedy-algorithms)

### Tier 3 (Good to Know)
- **Advanced Tree Structures**: [Trie](trees.md#trie-data-structure), [Segment Tree](trees.md#segment-tree)
- **Graph Algorithms**: [Dijkstra's](graphs.md#dijkstras-algorithm), [Topological Sort](graphs.md#topological-sort), [MST](graphs.md#prims-algorithm)
- **Advanced Dynamic Programming**: [Palindrome problems](dynamic-programming.md#palindrome-problems), Matrix chains
- **Specialized Algorithms**: 
  - [Rabin-Karp String Matching](additional-patterns.md#rabin-karp-string-matching)
  - [Reservoir Sampling](additional-patterns.md#reservoir-sampling)
  - [Floyd's Cycle Detection](additional-patterns.md#floyds-cycle-finding-tortoise-and-hare)
  - [Quick Select](additional-patterns.md#quick-select-kth-largest-element)

## Accelerated Learning Strategies

### 1. Pattern Recognition Framework
- **Pattern Trigger List**: Create a list of "problem signatures" that map to specific algorithms
  - "Find all subarrays that sum to X" → Sliding Window or Prefix Sum
  - "Find shortest/longest in sorted array" → Binary Search
  - "Find if path exists" → BFS/DFS
- **Problem Classification**: Before solving, identify which pattern category it belongs to
- **Pattern First, Code Second**: Think of the algorithmic approach before writing any code

### 2. Interleaved Practice Method
- **Learn → Implement → Review Cycle**:
  1. Study pattern (1 hour max)
  2. Implement 2-3 problems using the pattern (2 hours)
  3. Review and optimize solutions (1 hour)
  4. Move to next pattern
- **Spaced Repetition**: Return to previously learned patterns every 3-4 days
- **Mixed Practice Sessions**: After learning 3-4 patterns, do mixed problems without knowing the pattern in advance

### 3. Strategic Problem Mapping
- **Pattern-to-Problem Matrix**: Create a grid mapping each pattern to 3-5 representative problems
- **Difficulty Progression**: For each pattern, solve in increasing difficulty order
- **Common Edge Cases Library**: Maintain a list of edge cases relevant to each pattern
- **Solution Comparisons**: After solving, compare your approach with optimal solutions

### 4. Visual Learning Acceleration
- **Algorithm Flowcharts**: Create simple diagrams for each algorithm pattern
- **State Transition Diagrams**: Visual representations of how data changes through algorithm steps
- **Memory Model Visualization**: Draw memory/pointer states for complex data structure operations
- **Decision Tree Maps**: For recursive/backtracking problems, sketch the decision tree

### 5. Implementation Templates
- **Create skeleton templates** for each pattern with well-commented sections:
  ```python
  def sliding_window_fixed(arr, k):
      # 1. Initialize window sum and result
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
- **Language-Specific Idioms**: Learn the standard library functions that simplify implementations
- **Pattern Variations**: Create template variations for common pattern adaptations

### 6. Time-Boxing Technique
- **25-Minute Rule**: Set a timer; if unable to identify the approach within 25 minutes, review the pattern
- **Implementation Time Limits**: 20-30 minutes per easy problem, 45 minutes per medium problem
- **5-Minute Planning**: Before coding, spend 5 minutes planning your approach on paper
- **Focused Review**: If you fail to solve in allocated time, study only what you missed, not the entire solution

### 7. Deliberate Simplification
- **Build-Up Method**: Start with simplest working solution, then optimize
- **Subproblem Mastery**: Break complex algorithms into smaller techniques and master each separately
- **Constraints Relaxation**: First solve without caring about optimal space/time, then optimize
- **Test-Driven Approach**: Write test cases first to clarify your understanding

### 8. Language-Specific Optimization
- **Standard Library Proficiency**: Master built-in functions relevant to algorithms
- **Data Structure Syntax**: Memorize syntax for common operations (e.g., heap push/pop, queue operations)
- **Common Patterns Cheatsheet**: Create reference for frequently used code snippets

## 3-Week Study Schedule

### Week 1: Foundations
- **Day 1**: Sliding Window Fixed & Variable
  - Study pattern (1h)
  - Implement: Max Sum Subarray of Size K, Longest Substring with K Distinct Characters
  - Review solutions and optimizations

- **Day 2**: Two Pointers & Prefix Sums
  - Study patterns (1h)
  - Implement: Pair with Target Sum, Subarrays with Product Less than K, Subarray Sum Equals K
  - Review and compare approaches

- **Day 3**: Binary Search Variations
  - Study standard and variations (1h)
  - Implement: Search in Rotated Sorted Array, Find First and Last Position, Median of Two Sorted Arrays
  - Analyze boundary conditions and edge cases

- **Day 4**: More Binary Search & Kadane's Algorithm
  - Continue with binary search on answer (1h)
  - Study Kadane's Algorithm (1h)
  - Implement: Capacity To Ship Packages, Maximum Subarray
  - Review optimizations

- **Day 5**: Graph Traversals - BFS
  - Study BFS pattern (1h)
  - Implement: Level Order Traversal, Shortest Path in Binary Matrix, Walls and Gates
  - Analyze performance characteristics

- **Day 6**: Graph Traversals - DFS
  - Study DFS pattern (1h)
  - Implement: Number of Islands, Max Area of Island, Course Schedule
  - Compare recursive vs. iterative implementations

- **Day 7**: Review & Mixed Practice
  - Mixed problem set (no pattern hints)
  - Self-assessment on pattern recognition
  - Review weak areas

### Week 2: Intermediate
- **Day 8**: Dynamic Programming - 0/1 Knapsack
  - Study pattern and variations (1.5h)
  - Implement: Subset Sum, Equal Subset Sum Partition
  - Review space optimization techniques

- **Day 9**: Dynamic Programming - LCS Pattern
  - Study pattern and variations (1.5h)
  - Implement: Longest Common Subsequence, Shortest Common Supersequence
  - Review solution construction techniques

- **Day 10**: Binary Trees - DFS
  - Study tree DFS patterns (1h)
  - Implement: Path Sum, Validate BST, Max Depth of Binary Tree
  - Compare recursive vs. iterative approaches

- **Day 11**: Linked List Patterns
  - Study Fast & Slow Pointers, reversal techniques (1h)
  - Implement: Middle of Linked List, Detect Cycle, Reverse Linked List
  - Review edge cases handling

- **Day 12**: Backtracking - Subsets & Combinations
  - Study pattern (1.5h)
  - Implement: Subsets, Combinations, Combination Sum
  - Analyze decision space exploration

- **Day 13**: Backtracking - Permutations & More
  - Study variations (1h)
  - Implement: Permutations, N-Queens, Word Search
  - Review pruning techniques

- **Day 14**: Mixed Practice & Review
  - Timed problem solving sessions
  - Pattern identification practice
  - Revisit week 1 patterns briefly

### Week 3: Advanced
- **Day 15**: Heaps & Priority Queues
  - Study Two Heaps pattern (1h)
  - Implement: Find Median from Data Stream, Top K Frequent Elements
  - Review heap operations efficiencies

- **Day 16**: Monotonic Stack & Queue
  - Study pattern (1h)
  - Implement: Next Greater Element, Largest Rectangle in Histogram
  - Analyze stack operations and complexity

- **Day 17**: Union Find & Disjoint Set
  - Study pattern (1h)
  - Implement: Number of Connected Components, Redundant Connection
  - Review path compression and union by rank optimizations

- **Day 18**: Greedy Algorithms
  - Study pattern and common problems (1h)
  - Implement: Jump Game, Task Scheduler, Meeting Rooms
  - Analyze proof of optimality

- **Day 19**: Bit Manipulation & Math
  - Study bit operations (1h)
  - Implement: Single Number, Counting Bits, Power of Two
  - Review bit manipulation tricks

- **Day 20**: Specialized Techniques
  - Study Trie, Rabin-Karp, Reservoir Sampling (1.5h)
  - Implement: Implement Trie, Find Duplicate File in System
  - Review complexity analysis

- **Day 21**: Comprehensive Review
  - Full pattern review
  - Mixed difficulty problem solving
  - Assessment of learning gaps

## Learning Acceleration Techniques

### 1. Active Recall
- After learning a pattern, close all resources and try to rewrite the implementation from memory
- Verbalize the algorithm steps before coding
- Create flash cards for key algorithm insights, not just code

### 2. Concept Mapping
- Create mind maps connecting related algorithm patterns
- Develop a decision tree for selecting which algorithm to apply
- Map edge cases to specific patterns

### 3. Deliberate Practice
- Focus specifically on areas of weakness
- Time your problem-solving and track improvement
- Regularly revisit problems you initially failed

### 4. Teaching & Verbalization
- Explain algorithms out loud as if teaching someone
- Write simplified explanations for each pattern
- Record yourself explaining complex algorithms

### 5. Error Analysis
- Keep a "mistake log" tracking recurring errors
- Categorize mistakes: conceptual, implementation, edge cases
- Review mistake patterns regularly

## Assessment & Progress Tracking

### Weekly Self-Evaluation
- **Pattern Recognition Test**: Identify the appropriate pattern for 10 problem descriptions
- **Implementation Speed**: Track how long it takes to implement each pattern
- **Success Rate**: Percentage of problems solved without hints

### Pattern Mastery Checklist
For each algorithm pattern, track:
- [ ] Can recognize when to apply
- [ ] Can implement from memory
- [ ] Can handle common edge cases
- [ ] Can optimize the solution
- [ ] Can explain time/space complexity

### Final Readiness Assessment
- Solve 2-3 problems from each major pattern category
- Complete 2-3 mock interviews
- Review all pattern templates one final time

## Remember
Understanding the underlying principles is far more valuable than memorizing specific implementations. Focus on recognizing when to apply each pattern, and the implementations will become more intuitive with practice.

**The key is pattern recognition → selection → adaptation → implementation.**