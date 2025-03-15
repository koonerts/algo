"""
Quick_sort

"""
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



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to quick_sort
    print(quick_sort([]))
