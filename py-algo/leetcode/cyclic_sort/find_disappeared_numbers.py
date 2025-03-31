"""
Disappeared Numbers

Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
        Find all the elements of [1, n] inclusive that do not appear in this array.
        Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

        Input: [4,3,2,7,8,2,3,1]
        Output: [5,6]
"""


def findDisappearedNumbers(nums: list[int]) -> list[int]:
    """
    Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
    Find all the elements of [1, n] inclusive that do not appear in this array.
    Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

    Input: [4,3,2,7,8,2,3,1]
    Output: [5,6]
    """
    for i in range(len(nums)):
        new_index = abs(nums[i]) - 1
        if nums[new_index] > 0:
            nums[new_index] *= -1

    return [i + 1 for i in range(len(nums)) if nums[i] > 0]


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to findDisappearedNumbers
    print(findDisappearedNumbers([]))
