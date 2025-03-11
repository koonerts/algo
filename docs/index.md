# Algorithm & Data Structure Cheatsheets for SWE Interviews

## Introduction

Welcome to the Algorithm & Data Structure cheatsheets! This repository contains comprehensive resources for mastering algorithms and data structures commonly used in software engineering interviews and competitive programming.

### How to Use This Repository

- **Beginners**: Start with the [Getting Started Guide](#getting-started) below and follow the [Learning Plan](lesson-plan.md)
- **Interview Prep**: Focus on the algorithm references organized by category
- **Practice**: Use the [Ready-to-Use Activities](ready-to-use-activities.md) to test your knowledge

### Getting Started

If you're new to algorithms or need a refresher:

1. Begin with fundamental data structures: arrays, linked lists, stacks, and queues
2. Follow the structured [3-Week Learning Plan](lesson-plan.md)
3. Practice with examples of increasing difficulty (Easy → Medium → Hard)
4. Use the interactive activities to reinforce your understanding

## Algorithm References

### Arrays & Strings
- [Kadane's Algorithm](arrays.md#kadanes-algorithm-cheatsheet-for-swe-interviews) - Maximum subarray sum
- [Fixed Size Sliding Window](arrays.md#sliding-window-fixed-size-algorithm-cheatsheet) - Efficient subarray operations with fixed window
- [Variable Size Sliding Window](arrays.md#sliding-window-variable-size-cheatsheet) - Dynamic window sizing for constraints
- [Two Pointers Technique](arrays.md#two-pointers-cheatsheet) - Linear time operations with dual pointers
- [Prefix Sums](arrays.md#prefix-sums-cheatsheet) - Optimized range queries

### Linked Lists
- [Fast & Slow Pointers Algorithm](linked-lists.md#fast--slow-pointers-algorithm) - Cycle detection and middle finding
- [Iterative Linked List Reversal](linked-lists.md#iterative-linked-list-reversal-cheatsheet) - In-place linked list reversal

### Trees & Advanced Data Structures
- [Trie (Prefix Tree)](trees.md#trie-data-structure) - Efficient prefix operations and string storage
- [Union-Find (Disjoint Set)](trees.md#union-find-disjoint-set) - Dynamic connectivity and component tracking
- [Segment Tree](trees.md#segment-tree) - Range query operations with updates
- [Iterative DFS](trees.md#iterative-dfs-depth-first-search) - Non-recursive depth-first traversal

### Heaps
- [Two Heaps Algorithm](heaps.md#two-heaps-algorithm) - Median finding and partition-based problems

### Backtracking
- [Subsets Algorithm](backtracking.md#subsets-algorithm) - Generating all possible subsets
- [Combinations Algorithm](backtracking.md#combinations-algorithm) - Generating k-sized combinations
- [Permutations Algorithm](backtracking.md#permutations-algorithm) - Generating all possible arrangements

### Graphs
- [Dijkstra's Algorithm](graphs.md#dijkstras-algorithm) - Shortest path with positive weights
- [Prim's Algorithm](graphs.md#prims-algorithm) - Minimum spanning tree using greedy approach
- [Kruskal's Algorithm](graphs.md#kruskals-algorithm) - Minimum spanning tree using disjoint set
- [Topological Sort](graphs.md#topological-sort) - Ordering of directed acyclic graphs

### Dynamic Programming
- [0/1 Knapsack](dynamic-programming.md#01-knapsack-problem) - Item selection with weight constraints
- [Unbounded Knapsack](dynamic-programming.md#unbounded-knapsack) - Item selection with unlimited quantities
- [Longest Common Subsequence (LCS)](dynamic-programming.md#longest-common-subsequence-lcs) - Sequence matching
- [Palindrome Problems](dynamic-programming.md#palindrome-problems) - Palindromic substring identification

### Additional Patterns
- [Binary Search Variations](additional-patterns.md#binary-search-variations) - Modified binary search for complex scenarios
- [Monotonic Stack/Queue](additional-patterns.md#monotonic-stackqueue) - Next greater/smaller element problems
- [BFS for Shortest Path](additional-patterns.md#bfs-for-shortest-path-in-unweighted-graph) - Level-order traversal for distances
- [Bit Manipulation Techniques](additional-patterns.md#bit-manipulation-techniques) - Bitwise operations for optimization
- [Dutch National Flag / Three-Way Partitioning](additional-patterns.md#dutch-national-flag--three-way-partitioning) - Three-value sorting
- [Boyer-Moore Voting Algorithm](additional-patterns.md#boyer-moore-voting-algorithm-majority-element) - Majority element finding
- [Floyd's Cycle Finding](additional-patterns.md#floyds-cycle-finding-tortoise-and-hare) - Cycle detection in sequences
- [Greedy Algorithms](additional-patterns.md#greedy-algorithms) - Local optimization techniques
- [Matrix Traversal Techniques](additional-patterns.md#matrix-traversal-techniques) - 2D array traversal patterns
- [Reservoir Sampling](additional-patterns.md#reservoir-sampling) - Random sampling from streams
- [Quick Select](additional-patterns.md#quick-select-kth-largest-element) - Finding kth smallest/largest element
- [Rabin-Karp String Matching](additional-patterns.md#rabin-karp-string-matching) - Substring search using hashing

## Learning Resources

### Study Plans
- [Algorithm Learning Acceleration Plan](lesson-plan.md) - Comprehensive 3-week plan with prioritized algorithm tiers and study strategies

### Learning Activities
- [Interactive Learning Activities & Games](learning-activities.md) - Collection of engaging activities to reinforce algorithm patterns
- [Ready-to-Use Digital Activities](ready-to-use-activities.md) - Practice resources you can use immediately:
  - Algorithm Flash Cards
  - Template Skeleton Exercises
  - Algorithm Decision Tree
  - Time Attack Implementation Challenges
  - Complexity Analysis Quizzes
  - Pattern Matching Games
  - Memory Optimization Challenges

### Reference Materials
- [Algorithm & Data Structure Glossary](glossary.md) - Comprehensive definitions of terms used throughout the documentation

## Difficulty Levels

Throughout this repository, algorithm implementations and practice problems are marked with difficulty indicators:

- ⭐ **Easy**: Fundamental concepts with straightforward implementation
- ⭐⭐ **Medium**: Intermediate complexity requiring deeper understanding
- ⭐⭐⭐ **Hard**: Advanced concepts often combining multiple techniques

## Implementation Languages

Examples and implementations are provided in:

- **Python**: Primary language with comprehensive coverage
- **Go**: Performance and concurrency-focused implementations

## Getting Help

If you're stuck on a specific algorithm or pattern:

1. Check the respective documentation page for detailed explanations
2. Look for the "Common Mistakes" section that highlights frequent errors
3. Review the visualization and step-by-step examples
4. Try the practice problems with increasing difficulty

## Contributing

If you'd like to contribute to this repository, please follow these guidelines:

### Adding New Algorithms
1. Use the [standard template](template.md) for consistency
2. Include implementations in Python and Go
3. Add difficulty indicators to all problems
4. Include visualizations and clear explanations
5. Follow the existing file naming and organization conventions

### Improving Documentation
1. Maintain the standardized section structure
2. Add real-world examples where applicable
3. Ensure explanations are accessible to various skill levels
4. Include references to scholarly sources where appropriate

### Creating Visualizations
1. Use ASCII diagrams for simple visualizations that work in Markdown
2. For complex visualizations, use SVG or PNG files in the assets directory
3. Ensure visualizations are clear and properly labeled
4. Consider creating animations for step-by-step algorithm execution

### Adding Language Implementations
1. Follow Python or Go best practices and coding standards
2. Include comments explaining non-obvious parts of the implementation
3. Ensure implementations are efficient and handle edge cases
4. Test implementations with various inputs before submitting

---

*Last Updated: March 10, 2025*