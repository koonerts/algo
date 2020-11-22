import random


def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) < 2:
        return arr
    else:
        # grab random value and use it as a partition to get lte & gt list
        # recursively quick_sort those sub arrays
        # return the concatenation of answers
        pivot_val = arr[random.randrange(len(arr))]
        lt, et, gt = [], [], []
        for n in arr:
            if n < pivot_val:
                lt.append(n)
            elif n == pivot_val:
                et.append(n)
            else:
                gt.append(n)
        return quick_sort(lt) + et + quick_sort(gt)


print(quick_sort([10, 2, -1, -1, 12, 3, -1]))
