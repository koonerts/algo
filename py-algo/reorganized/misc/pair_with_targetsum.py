"""
Pair_with_targetsum

Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
    Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

    Example 1:
    Input: [1, 2, 3, 4, 6], target=6
    Output: [1, 3]
    Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

    Example 2:
    Input: [2, 5, 9, 11], target=11
    Output: [0, 2]
    Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
"""
def pair_with_targetsum(arr: list[int], target_sum: int) -> list[int]:
    """
    Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.
    Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

    Example 1:
    Input: [1, 2, 3, 4, 6], target=6
    Output: [1, 3]
    Explanation: The numbers at index 1 and 3 add up to 6: 2+4=6

    Example 2:
    Input: [2, 5, 9, 11], target=11
    Output: [0, 2]
    Explanation: The numbers at index 0 and 2 add up to 11: 2+9=11
    """
    start, end = 0, len(arr) - 1
    while start < end:
        sum_ = arr[start] + arr[end]
        if sum_ == target_sum:
            return [start, end]
        elif sum_ > target_sum:
            end -= 1
        else:
            start += 1

    return [-1, -1]



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to pair_with_targetsum
    print(pair_with_targetsum([]))
