"""
Dutch_flag_sort

Given an array containing 0s, 1s and 2s, sort the array in-place.
    You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

    The flag of the Netherlands consists of three colors: red, white and blue;
    And since our input array also consists of three different numbers, it is called Dutch National Flag problem.

    Example 1:
    Input: [1, 0, 2, 1, 0]
    Output: [0 0 1 1 2]

    Example 2:
    Input: [2, 2, 0, 1, 2, 0]
    Output: [0 0 1 2 2 2 ]
"""


def dutch_flag_sort(arr: list[int]) -> list[int]:
    """
    Given an array containing 0s, 1s and 2s, sort the array in-place.
    You should treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s to recreate the array.

    The flag of the Netherlands consists of three colors: red, white and blue;
    And since our input array also consists of three different numbers, it is called Dutch National Flag problem.

    Example 1:
    Input: [1, 0, 2, 1, 0]
    Output: [0 0 1 1 2]

    Example 2:
    Input: [2, 2, 0, 1, 2, 0]
    Output: [0 0 1 2 2 2 ]
    """
    low, high = 0, len(arr) - 1
    i = 0
    while i <= high:
        if arr[i] == 0:
            arr[i], arr[low] = arr[low], arr[i]
            # increment 'i' and 'low'
            i += 1
            low += 1
        elif arr[i] == 1:
            i += 1
        else:  # the case for arr[i] == 2
            arr[i], arr[high] = arr[high], arr[i]
            # decrement 'high' only, after the swap the number at index 'i' could be 0, 1 or 2
            high -= 1
    return arr


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to dutch_flag_sort
    print(dutch_flag_sort([]))
