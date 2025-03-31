"""
Triplet_sum_close_to_target

Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible and
    return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

    Example 1:
    Input: [-2, 0, 1, 2], target=2
    Output: 1
    Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

    Example 2:
    Input: [-3, -1, 1, 2], target=1
    Output: 0
    Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

    Example 3:
    Input: [1, 0, 1, 1], target=100
    Output: 3
    Explanation: The triplet [1, 1, 1] has the closest sum to the target.
"""


def triplet_sum_close_to_target(arr: list[int], target_sum: int):
    """
    Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible and
    return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

    Example 1:
    Input: [-2, 0, 1, 2], target=2
    Output: 1
    Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

    Example 2:
    Input: [-3, -1, 1, 2], target=1
    Output: 0
    Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

    Example 3:
    Input: [1, 0, 1, 1], target=100
    Output: 3
    Explanation: The triplet [1, 1, 1] has the closest sum to the target.
    """
    # time: O(nlogn)
    # space: O(n)
    arr.sort()
    closest_sum: int = 0

    # time: O(n^2)
    # space: O(1)
    for i, val in enumerate(arr):
        start = i + 1
        end = len(arr) - 1
        while start < end:
            sum_ = val + arr[start] + arr[end]
            if sum_ == target_sum:
                return 0
            elif sum_ < target_sum:
                start += 1
            else:
                end -= 1

            diff = abs(target_sum - sum_)
            if diff < abs(target_sum - closest_sum):
                closest_sum = sum_
            elif diff == abs(target_sum - closest_sum):
                closest_sum = min(closest_sum, sum_)

    """
    Overall time: O(nlogn + n^2) -> O(n^2)
    Overall space: O(n)
    """
    return closest_sum


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to triplet_sum_close_to_target
    print(triplet_sum_close_to_target([]))
