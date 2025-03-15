"""
Sort

"""
def mergeSort(array):
def partition(lo, hi):
        if lo < hi:
            mid = (lo+hi)//2
            partition(lo,mid)
            partition(mid+1, hi)
            merge(lo, mid, hi)
def merge(lo, mid, hi):
        i, j = lo, mid+1

        result = []
        while i <= mid or j <= hi:
            if j > hi or (i <= mid and array[i] <= array[j]):
                result.append(array[i])
                i += 1
            else:
                result.append(array[j])
                j += 1

        for i in range(lo, hi+1):
            array[i] = result[i-lo]
    partition(0, len(array)-1)
    return array



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to mergeSort
    print(mergeSort([]))
