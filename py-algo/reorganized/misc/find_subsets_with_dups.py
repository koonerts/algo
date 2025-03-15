"""
Find_subsets_with_dups

Given a set of numbers that might contain duplicates, find all of its distinct subsets.

    Example 1:
    Input: [1, 3, 3]
    Output: [], [1], [3], [1,3], [3,3], [1,3,3]

    Example 2:
    Input: [1, 5, 3, 3]
    Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]
"""
def find_subsets_with_dups(nums: list[int]):
    """
    Given a set of numbers that might contain duplicates, find all of its distinct subsets.

    Example 1:
    Input: [1, 3, 3]
    Output: [], [1], [3], [1,3], [3,3], [1,3,3]

    Example 2:
    Input: [1, 5, 3, 3]
    Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]
    """
    if not nums: return [[]]

    nums.sort()
    subsets = [[]]
    start, end = 0, 0

    for i, num in enumerate(nums):
        start = 0
        if i > 0 and nums[i-1] == nums[i]:
            start = end + 1
        end = len(subsets) - 1
        for j in range(start, end + 1):
            subsets.append(subsets[j] + [num])
    return subsets



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_subsets_with_dups
    print(find_subsets_with_dups([]))
