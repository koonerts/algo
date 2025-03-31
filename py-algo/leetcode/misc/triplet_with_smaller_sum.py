"""
Triplet_with_smaller_sum

Given an array arr of unsorted numbers and a target sum, count all triplets in it
    such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
    Write a function to return the count of such triplets.

    Example 1:
    Input: [-1, 0, 2, 3], target=3
    Output: 2
    Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

    Example 2:
    Input: [-1, 4, 2, 1, 3], target=5
    Output: 4
    Explanation: There are four triplets whose sum is less than the target: [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
"""


def triplet_with_smaller_sum(arr: list[int], target: int) -> int:
    """
    Given an array arr of unsorted numbers and a target sum, count all triplets in it
    such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices.
    Write a function to return the count of such triplets.

    Example 1:
    Input: [-1, 0, 2, 3], target=3
    Output: 2
    Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

    Example 2:
    Input: [-1, 4, 2, 1, 3], target=5
    Output: 4
    Explanation: There are four triplets whose sum is less than the target: [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
    """
    count = 0
    arr.sort()

    for i, v in enumerate(arr):
        start = i + 1
        end = len(arr) - 1

        while start < end:
            sum_ = v + arr[start] + arr[end]
            if sum_ < target:
                count += end - start
                start += 1
            else:
                end -= 1

    return count


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to triplet_with_smaller_sum
    print(triplet_with_smaller_sum([]))
