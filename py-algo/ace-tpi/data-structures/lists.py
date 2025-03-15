from heapq import *


def remove_even(list):
    return [num for num in list if num % 2 == 1]


def merge_lists(lst1, lst2):
    result = []
    min_heap = []
    if lst1:
        heappush(min_heap, (lst1[0], 0, 1))
    if lst1:
        heappush(min_heap, (lst2[0], 0, 2))

    while min_heap:
        num, i, list_id = heappop(min_heap)
        result.append(num)

        if list_id == 1 and i + 1 < len(lst1):
            heappush(min_heap, (lst1[i + 1], i + 1, 1))

        if list_id == 2 and i + 1 < len(lst2):
            heappush(min_heap, (lst2[i + 1], i + 1, 2))

    return result


def find_product(lst):
    product = 1
    for num in lst:
        product *= num

    return [product // num for num in lst]


def find_second_maximum(lst):
    if not lst:
        return None
    min_heap = []

    for num in lst:
        if len(min_heap) < 2:
            heappush(min_heap, num)
        else:
            if num > min_heap[0]:
                heappushpop(min_heap, num)
    return min_heap[0]


def right_rotate(lst, n):
    # get rotation index
    n = n % len(lst)
    return lst[-n:] + lst[:-n]


def rearrange(lst):
    start, end = 0, len(lst) - 1

    while start < end:
        if lst[start] < 0:
            start += 1
        else:
            lst[start], lst[end] = lst[end], lst[start]
            end -= 1
    return lst


def max_min(lst):
    start, end = 0, len(lst) - 1
    ret_arr = []
    while start <= end:
        ret_arr.append(lst[end])
        if start != end:
            ret_arr.append(lst[start])
        start += 1
        end -= 1
    return ret_arr


def max_min_no_extra_space(lst):
    # Return empty list for empty list
    if len(lst) == 0:
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1

    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    return lst


def find_max_sum_subarray(lst):
    start, curr_sum, max_sum = 0, 0, 0

    for i, v in enumerate(lst):
        curr_sum += v

        while v > curr_sum:
            curr_sum -= lst[start]
            start += 1

        max_sum = max(max_sum, curr_sum)
    return max_sum


def find_max_sum_subarray2(lst):
    if len(lst) < 1:
        return 0

    curr_max = lst[0]
    global_max = lst[0]
    length_array = len(lst)
    for i in range(1, length_array):
        if curr_max < 0:
            curr_max = lst[i]
        else:
            curr_max += lst[i]
        if global_max < curr_max:
            global_max = curr_max

    return global_max


lst = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
print("Sum of largest subarray: ", find_max_sum_subarray2(lst))
