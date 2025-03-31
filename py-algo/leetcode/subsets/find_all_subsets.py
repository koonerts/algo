def find_all_subsets(nums):
    """Generates all possible subsets (the power set) of a given set of numbers."""
    result = [[]]
    for num in nums:
        # For each number, iterate through the current subsets
        # and create new subsets by adding the current number to each existing subset.
        new_subsets = []
        for subset in result:
            new_subsets.append(subset + [num])
        # Add the newly created subsets to the result list.
        result.extend(new_subsets)
    return result

def find_all_subsets_backtracking(nums):
    """Generates all possible subsets (the power set) of a given set of numbers."""
    result = []
    n = len(nums)

    def backtrack(start_index, current_subset):
        # Add the current subset to the result list (make a copy)
        result.append(list(current_subset))

        # Explore adding more elements
        for i in range(start_index, n):
            # Include nums[i] in the current subset
            current_subset.append(nums[i])
            # Move on to the next element
            backtrack(i + 1, current_subset)
            # Exclude nums[i] from the current subset (backtrack)
            current_subset.pop()

    # Start the backtracking process
    backtrack(0, [])
    return result