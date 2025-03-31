"""
For Range

"""
def searchForRange(array, target):
def binary_search_direction(lo, hi, direction):
        idx = -1
        while lo <= hi:
            mid = (lo+hi)//2
            if array[mid] == target:
                idx = mid
                if direction == 'LEFT':
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif array[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return idx

    left, right = -1, -1
    left = binary_search_direction(0, len(array)-1, 'LEFT')
    if left != -1:
        right = binary_search_direction(0, len(array)-1, 'RIGHT')
    return [left, right]


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to searchForRange
    print(searchForRange([]))
