"""
Sort

"""
def quickSort(array):
def qs_rec(lo, hi):
        if lo >= hi:
            return
        else:
            mid = (lo+hi)//2
            array[mid], array[hi] = array[hi], array[mid]
            pivot = array[hi]
            i, left, right = 0, lo, hi-1

            while left <= right:
                if array[left] < pivot:
                    left += 1
                if array[right] > pivot:
                    right -= 1
                if array[left] > pivot > array[right]:
                    array[left], array[right] = array[right], array[left]
                    left += 1
                    right -= 1
            array[hi], array[left] = array[left], array[hi]

            qs_rec(lo, left-1)
            qs_rec(left+1, hi)
    qs_rec(0, len(array)-1)


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to quickSort
    print(quickSort([]))
