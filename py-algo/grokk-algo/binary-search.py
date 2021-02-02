

def binary_search(arr: list[int], target: int) -> int:
    if not arr: return -1

    start, end = 0, len(arr) - 1
    while start <= end:
        mid = int((start + end)/2)

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return -1


"""
Time Complexity -> O(log n)
"""