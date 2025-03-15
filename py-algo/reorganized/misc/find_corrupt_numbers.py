"""
Find_corrupt_numbers

We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
    The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the
    numbers got duplicated which also resulted in one number going missing.
    Find both these numbers.

    Example 1:
    Input: [3, 1, 2, 5, 2]
    Output: [2, 4]
    Explanation: '2' is duplicated and '4' is missing.

    Example 2:
    Input: [3, 1, 2, 3, 6, 4]
    Output: [3, 5]
    Explanation: '3' is duplicated and '5' is missing.
"""
def find_corrupt_numbers(nums):
    """
    We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
    The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the
    numbers got duplicated which also resulted in one number going missing.
    Find both these numbers.

    Example 1:
    Input: [3, 1, 2, 5, 2]
    Output: [2, 4]
    Explanation: '2' is duplicated and '4' is missing.

    Example 2:
    Input: [3, 1, 2, 3, 6, 4]
    Output: [3, 5]
    Explanation: '3' is duplicated and '5' is missing.
    """
    i = 0
    return_list = []
    while i < len(nums):
        if nums[i] == i + 1 or nums[i] == nums[nums[i] - 1]:
            i += 1
        else:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

    for i, num in enumerate(nums):
        if i + 1 != num:
            return_list.append(num)
            return_list.append(i + 1)

    return return_list



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_corrupt_numbers
    print(find_corrupt_numbers([]))
