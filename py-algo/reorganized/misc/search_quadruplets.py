"""
Search_quadruplets

Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

    Example 1:
    Input: [4, 1, 2, -1, 1, -3], target=1
    Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
    Explanation: Both the quadruplets add up to the target.

    Example 2:
    Input: [2, 0, -1, 1, -2, 2], target=2
    Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
    Explanation: Both the quadruplets add up to the target.
"""
def search_quadruplets(arr: list[int], target: int) -> list[list[int]]:
    """
    Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

    Example 1:
    Input: [4, 1, 2, -1, 1, -3], target=1
    Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
    Explanation: Both the quadruplets add up to the target.

    Example 2:
    Input: [2, 0, -1, 1, -2, 2], target=2
    Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
    Explanation: Both the quadruplets add up to the target.
    """
    arr.sort()
    quadruplets = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            k, l = j + 1, len(arr) - 1
            while k < l:
                ival, jval, kval, lval = arr[i], arr[j], arr[k], arr[l]
                sum_ = ival + jval + kval + lval
                if sum_ == target:
                    quadruplets.append([ival, jval, kval, lval])
                    while k < l and arr[k] == kval: k += 1
                    while l > k and arr[l] == lval: l -= 1
                elif sum_ > target:
                    l -= 1
                else:
                    k += 1

    return quadruplets



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to search_quadruplets
    print(search_quadruplets([]))
