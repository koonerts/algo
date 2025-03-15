"""
Search_triplets

Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

    Example 1:
    Input: [-3, 0, 1, 2, -1, 1, -2]
    Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
    Explanation: There are four unique triplets whose sum is equal to zero.

    Example 2:
    Input: [-5, 2, -1, -2, 3]
    Output: [[-5, 2, 3], [-2, -1, 3]]
    Explanation: There are two unique triplets whose sum is equal to zero.
"""
def search_triplets(arr: list[int]) -> list[list[int]]:
    """
    Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

    Example 1:
    Input: [-3, 0, 1, 2, -1, 1, -2]
    Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
    Explanation: There are four unique triplets whose sum is equal to zero.

    Example 2:
    Input: [-5, 2, -1, -2, 3]
    Output: [[-5, 2, 3], [-2, -1, 3]]
    Explanation: There are two unique triplets whose sum is equal to zero.
    """
    triplets = []

    # time: O(nlog(n))
    # space: O(n)
    arr.sort()

    # time: O(n^2) -> loop through each index and nested loop through i+i..i+n-1 to n
    # space: O(n) -> triplets
    for i, val in enumerate(arr):
        start = i + 1
        end = len(arr) - 1
        while start < end:
            sum_ = arr[start] + arr[end] + val
            if sum_ == 0:
                triplets.append([val, arr[start], arr[end]])
                # end = len(arr) - 1

                # handle duplicates in the array by incrementing start by 1 until we get a non-duplicate start
                while True:
                    start += 1
                    if start > len(arr) or arr[start] != arr[start - 1]:
                        break

            elif sum_ > 0:
                end -= 1
            else:
                start += 1
    """
    Overall time complexity is O(nlogn + n^2) -> O(n^2)
    Overall space complexity is O(n + n) -> O(n)
    """
    return triplets



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to search_triplets
    print(search_triplets([]))
