"""
Find_closest_elements

Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array.
    Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

    Example 1:
    Input: [5, 6, 7, 8, 9], K = 3, X = 7
    Output: [6, 7, 8]

    Example 2:
    Input: [2, 4, 5, 6, 9], K = 3, X = 6
    Output: [4, 5, 6]

    Example 3:
    Input: [2, 4, 5, 6, 9], K = 3, X = 10
    Output: [5, 6, 9]
"""
def find_closest_elements(arr, K, X):
    """
    Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array.
    Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

    Example 1:
    Input: [5, 6, 7, 8, 9], K = 3, X = 7
    Output: [6, 7, 8]

    Example 2:
    Input: [2, 4, 5, 6, 9], K = 3, X = 6
    Output: [4, 5, 6]

    Example 3:
    Input: [2, 4, 5, 6, 9], K = 3, X = 10
    Output: [5, 6, 9]
    """
    result = []

    # TODO: Can be improved by using binary search for finding the closest element
    #       and then 2 pointers expanding to either side of that element until reaching K
    for num in arr:
        diff = abs(num-X)

        if len(result) < K:
            heappush(result, (-diff, num))
        elif diff < -result[0][0]:
            heappushpop(result, (-diff, num))

    return [item[1] for item in result]



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_closest_elements
    print(find_closest_elements([]))
