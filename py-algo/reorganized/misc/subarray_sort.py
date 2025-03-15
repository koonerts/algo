"""
Sort

"""
def subarraySort(array):
    l, r = float('inf'), float('inf')
    min_val, max_val = float('inf'), float('-inf')
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            l = i+1
            break

    if l == float('inf'): return [-1, -1]

    for i in reversed(range(len(array))):
        if array[i] < array[l-1]:
            r = i
            break

    min_val = min(array[l:r+1])
    max_val = max(array[l:r+1])
    low, high = 0, len(array)-1
    while True:
        if (array[low] > min_val or low == l) and (array[high] < max_val or high == r):
            break

        if not (array[low] > min_val or low == l):
            low += 1

        if not (array[high] < max_val or high == r):
            high -= 1
    return [low, high]



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to subarraySort
    print(subarraySort([]))
