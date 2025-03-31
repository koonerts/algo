"""
Binary Search

"""


def shiftedBinarySearch(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (high + low) // 2
        if array[mid] == target:
            return mid
        else:
            # left side sorted
            if array[low] <= array[mid]:
                if array[low] <= target < array[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if array[mid] < target <= array[high]:
                    low = mid + 1
                else:
                    high = mid - 1
    return -1


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to shiftedBinarySearch
    print(shiftedBinarySearch([]))
