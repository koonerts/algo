"""
Merge

"""
def merge(arr, lo, mid, hi):
    i, j = lo, mid+1
    result = []
    while i <= mid and j <= hi:
        if arr[i] <= arr[j]:
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j += 1

    while i <= mid:
        result.append(arr[i])
        i += 1
    while j <= hi:
        result.append(arr[j])
        j += 1

    for i in range(lo, hi+1):
        arr[i] = result[i-lo]



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to merge
    print(merge([]))
