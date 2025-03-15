# Dynamic Programming Algorithms

This directory contains algorithm problems solved using dynamic programming techniques.

## Table of Contents

| Problem | Description |
|---------|-------------|
| [can_jump](./can_jump.py) | Determine if you can reach the last index of an array by jumping |
| [can_partition_to_equal_subsets_memoized](./can_partition_to_equal_subsets_memoized.py) | Partition array into two equal sum subsets (memoization approach) |
| [can_partition_to_equal_subsets_tabulated](./can_partition_to_equal_subsets_tabulated.py) | Partition array into two equal sum subsets (tabulation approach) |
| [can_partition_with_subset_sum_equal_to_s_memoized](./can_partition_with_subset_sum_equal_to_s_memoized.py) | Find if subset with given sum exists (memoization) |
| [can_partition_with_subset_sum_equal_to_s_tabulated](./can_partition_with_subset_sum_equal_to_s_tabulated.py) | Find if subset with given sum exists (tabulation) |
| [climb_stairs](./climb_stairs.py) | Count ways to climb stairs when taking 1 or 2 steps at a time |
| [coin_change](./coin_change.py) | Find minimum number of coins to make a given amount |
| [count_subsets](./count_subsets.py) | Count number of subsets with a given sum |
| [find_target_subsets](./find_target_subsets.py) | Find ways to assign + and - to make expression equal target sum |
| [knapsack_memoized](./knapsack_memoized.py) | 0/1 Knapsack problem with memoization |
| [knapsack_problem](./knapsack_problem.py) | 0/1 Knapsack problem with tabulation |
| [knapsack_problem_recursive](./knapsack_problem_recursive.py) | 0/1 Knapsack problem with recursion |
| [levenshtein_distance](./levenshtein_distance.py) | Calculate edit distance between two strings |
| [longest_arith_seq_length](./longest_arith_seq_length.py) | Find length of longest arithmetic sequence in an array |
| [longest_palindrome](./longest_palindrome.py) | Find the longest palindromic substring |
| [max_profit_brute_force](./max_profit_brute_force.py) | Maximum profit from stock trading (brute force) |
| [max_subset_sum_no_adjacent](./max_subset_sum_no_adjacent.py) | Find maximum sum of non-adjacent elements |
| [max_sum_increasing_subsequence](./max_sum_increasing_subsequence.py) | Find maximum sum of increasing subsequence |
| [min_number_of_coins_for_change](./min_number_of_coins_for_change.py) | Find minimum coins needed to make change |
| [min_number_of_jumps](./min_number_of_jumps.py) | Minimum jumps required to reach end of array |
| [number_of_options](./number_of_options.py) | Count number of options to combine items within constraints |
| [number_of_options2](./number_of_options2.py) | Variation of counting options problem |
| [number_of_ways_to_make_change](./number_of_ways_to_make_change.py) | Count ways to make change with given denominations |
| [partition_to_min_subset_difference_memoized](./partition_to_min_subset_difference_memoized.py) | Partition array to minimize subset sum difference (memoization) |
| [partition_to_min_subset_difference_tabulated](./partition_to_min_subset_difference_tabulated.py) | Partition array to minimize subset sum difference (tabulation) |
| [rob](./rob.py) | House robber problem - maximum value without adjacent houses |
| [solve_knapsack](./solve_knapsack.py) | Generic knapsack problem solver |
| [split_primes](./split_primes.py) | Split a string into prime numbers |
| [unique_paths](./unique_paths.py) | Count unique paths in a grid with obstacles |
| [word_break](./word_break.py) | Determine if a string can be segmented into dictionary words |

## Common Dynamic Programming Patterns

- **Memoization (Top-down)**: Store results of expensive function calls to avoid redundant calculations
- **Tabulation (Bottom-up)**: Build solution iteratively from smaller subproblems
- **State Transition**: Define clear state transitions with recurrence relations
- **Overlapping Subproblems**: Break down problems into smaller, overlapping subproblems
- **Optimal Substructure**: Overall optimal solution incorporates optimal solutions to subproblems

## Approaches

1. **0/1 Knapsack Pattern**: Used in problems like knapsack, can_partition, and subset sum
2. **Unbounded Knapsack Pattern**: Used in coin_change and related problems
3. **Fibonacci Pattern**: Used in climb_stairs and similar sequence problems
4. **Longest Common Subsequence Pattern**: Used in string comparison problems
5. **Grid Traversal Pattern**: Used in unique_paths and similar grid-based problems