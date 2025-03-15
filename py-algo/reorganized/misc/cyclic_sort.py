"""
Cyclic_sort

We are given an array containing ‘n’ objects. Each object, when created, was assigned a
    unique number from 1 to ‘n’ based on their creation sequence.

    This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.
    Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space.
    For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

    Example 1:
    Input: [3, 1, 5, 4, 2]
    Output: [1, 2, 3, 4, 5]

    Example 2:
    Input: [2, 6, 4, 3, 1, 5]
    Output: [1, 2, 3, 4, 5, 6]

    Example 3:
    Input: [1, 5, 6, 4, 3, 2]
    Output: [1, 2, 3, 4, 5, 6]
"""
def cyclic_sort(nums: list[int]) -> list[int]:
    """
    We are given an array containing ‘n’ objects. Each object, when created, was assigned a
    unique number from 1 to ‘n’ based on their creation sequence.

    This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.
    Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space.
    For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

    Example 1:
    Input: [3, 1, 5, 4, 2]
    Output: [1, 2, 3, 4, 5]

    Example 2:
    Input: [2, 6, 4, 3, 1, 5]
    Output: [1, 2, 3, 4, 5, 6]

    Example 3:
    Input: [1, 5, 6, 4, 3, 2]
    Output: [1, 2, 3, 4, 5, 6]
    """
    i = 0
    while i < len(nums):
        if nums[i] == i + 1:
            i += 1
        else:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
    return nums



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to cyclic_sort
    print(cyclic_sort([]))
