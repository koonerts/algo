

def merge_sort(arr, lo, hi):
    if lo < hi:
        mid = (lo+hi)//2
        merge_sort(arr, lo, mid)
        merge_sort(arr, mid+1, hi)
        merge(arr, lo, mid, hi)


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


def quick_sort(arr):

    def quick_sort_recursive(lo, hi):
        if lo > hi:
            return

        mid = (lo+hi)//2
        arr[mid], arr[hi] = arr[hi], arr[mid]
        pivot = arr[hi]
        i, j = lo, hi-1

        while i <= j:
            if arr[i] > pivot > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            if arr[i] <= pivot:
                i += 1
            if arr[j] >= pivot:
                j -= 1
        arr[i], arr[hi] = arr[hi], arr[i]
        quick_sort_recursive(lo, i-1)
        quick_sort_recursive(i+1, hi)
    quick_sort_recursive(0, len(arr)-1)


x = [5,3,1,-1,-12,0,100,2,9]
quick_sort(x)
print(x)