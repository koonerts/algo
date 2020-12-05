from heapq import *

def remove_even(list):
    return [num for num in list if num % 2 == 1]


def merge_lists(lst1, lst2):
    result = []
    min_heap = []
    if lst1: heappush(min_heap, (lst1[0], 0, 1))
    if lst1: heappush(min_heap, (lst2[0], 0, 2))

    while min_heap:
        num, i, list_id = heappop(min_heap)
        result.append(num)

        if list_id == 1 and i+1 < len(lst1):
            heappush(min_heap, (lst1[i+1], i+1, 1))

        if list_id == 2 and i+1 < len(lst2):
            heappush(min_heap, (lst2[i+1], i+1, 2))

    return result


def find_product(lst):
    product = 1
    for num in lst:
        product *= num

    return [product//num for num in lst]


def find_second_maximum(lst):
    if not lst: return None
    min_heap = []

    for num in lst:
        if len(min_heap) < 2:
            heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heappushpop(min_heap, num)
    return min_heap[0]


def right_rotate(lst, n):
    left_shift_cnt = abs(len(lst)-n)
    for i in range(len(lst)-1, -1, -1):


    pass