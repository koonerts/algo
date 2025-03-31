"""
Merge_sort

"""


def merge_sort(arr, lo, hi):
    if lo < hi:
        mid = (lo + hi) // 2
        merge_sort(arr, lo, mid)
        merge_sort(arr, mid + 1, hi)
        merge(arr, lo, mid, hi)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to merge_sort
    print(merge_sort([]))
