"""
Find_range

Given an array of numbers sorted in ascending order, find the range of a given number ‘key’.
    The range of the ‘key’ will be the first and last position of the ‘key’ in the array.
    Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

    Example 1:
    Input: [4, 6, 6, 6, 9], key = 6
    Output: [1, 3]

    Example 2:
    Input: [1, 3, 8, 10, 15], key = 10
    Output: [3, 3]

    Example 3:
    Input: [1, 3, 8, 10, 15], key = 12
    Output: [-1, -1]
"""
def find_range(arr: list[int], key: int) -> list[int]:
    """
    Given an array of numbers sorted in ascending order, find the range of a given number ‘key’.
    The range of the ‘key’ will be the first and last position of the ‘key’ in the array.
    Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

    Example 1:
    Input: [4, 6, 6, 6, 9], key = 6
    Output: [1, 3]

    Example 2:
    Input: [1, 3, 8, 10, 15], key = 10
    Output: [3, 3]

    Example 3:
    Input: [1, 3, 8, 10, 15], key = 12
    Output: [-1, -1]
    """
    if not arr: return [- 1, -1]

    start, end = 0, len(arr)-1

    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key:
            break
        elif arr[mid] < key:
            start = mid+1
        else:
            end = mid-1

    if start > end: return [-1, -1]



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_range
    print(find_range([]))
