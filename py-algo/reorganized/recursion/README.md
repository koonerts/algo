# Recursion and Backtracking Algorithms

This directory contains algorithm problems solved using recursion and backtracking techniques.

## Table of Contents

| Problem | Description |
|---------|-------------|
| [crack_safe](./crack_safe.py) | Find the shortest string that contains all possible combinations of a safe code |
| [exist](./exist.py) | Word search in a 2D board - check if a word exists in a grid of characters |
| [partition](./partition.py) | Palindrome partitioning - split a string into palindromic substrings |
| [print_slice](./print_slice.py) | Recursive helper for printing slices of data structures |
| [reverse_string](./reverse_string.py) | Reverse a string using recursion |
| [solve_sudoku](./solve_sudoku.py) | Solve a Sudoku puzzle using backtracking |
| [swap_pairs](./swap_pairs.py) | Swap every two adjacent nodes in a linked list using recursion |
| [total_n_queens](./total_n_queens.py) | Solve the N-Queens problem and count valid solutions |

## Key Recursion Patterns

- **Base Case and Recursive Case**: Every recursive solution has base cases to terminate recursion
- **Backtracking**: Systematically explore all possible solutions by trying options and undoing them if they don't work
- **State Space Tree**: Visualizing recursion as a tree of states helps understand the search space
- **Memoization**: Optimize recursive solutions by caching results of expensive function calls
- **Divide and Conquer**: Break problems into smaller subproblems, solve them recursively, and combine results

## Applications

- **Grid-based Problems**: Word search (exist.py), Sudoku solving (solve_sudoku.py)
- **Combinatorial Problems**: N-Queens (total_n_queens.py), permutations, combinations
- **String Manipulation**: Palindrome partitioning (partition.py), string reversal (reverse_string.py)
- **Linked List Operations**: Swapping pairs (swap_pairs.py)
- **Cryptographic Problems**: Cracking safe combinations (crack_safe.py)

## Tips for Approaching Recursive Problems

1. Identify the base case(s) that terminate recursion
2. Define the recursive relationship clearly
3. Track state between recursive calls appropriately
4. Consider memoization for optimization when overlapping subproblems exist
5. Be mindful of stack space consumption in deeply nested recursion