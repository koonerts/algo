"""
Find_subsets

Given a set with distinct elements, find all of its distinct subsets.

    Example 1:
    Input: [1, 3]
    Output: [], [1], [3], [1,3]

    Example 2:
    Input: [1, 5, 3]
    Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""


def find_subsets(nums: list[int]):
    """
    Given a set with distinct elements, find all of its distinct subsets.

    Example 1:
    Input: [1, 3]
    Output: [], [1], [3], [1,3]

    Example 2:
    Input: [1, 5, 3]
    Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
    """
    subsets = [[]]

    for num in nums:
        for i in range(len(subsets)):
            subsets.append(list(subsets[i]) + [num])
    return subsets


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_subsets
    print(find_subsets([]))
