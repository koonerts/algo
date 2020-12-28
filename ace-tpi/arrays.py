from collections import deque, OrderedDict, defaultdict
from heapq import *
import math


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def find_max_sliding_window(arr, window_size):
    if len(arr) <= window_size: return max(arr)

    result = []
    left, right = 0, window_size - 1
    curr_max = float('-inf')
    while right < len(arr) - 1:
        window_max = max(arr[left:right+1])

    # TODO: come back to


def binary_search_rotated(arr: list[int], key):
    if not arr: return -1

    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l+r)//2

        # found
        if arr[mid] == key:
            return mid

        # left hand sorted
        elif arr[l] <= arr[mid]:
            if arr[l] <= key < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1

        # right hand sorted
        else:
            if arr[mid] < key <= arr[r]:
                l = mid + 1
            else:
                r = mid - 1

    return -1


def find_least_common_number(a: list[int], b: list[int], c: list[int]) -> int:
    if not a or not b or not c: return -1

    def binary_search(start, end, nums, target):
        while start <= end:
            mid = (start + end)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    for i in range(len(a)):
        if binary_search(0, len(b)-1, b, a[i]) != -1 and binary_search(0, len(c)-1, c, a[i]) != -1:
            return a[i]
    return -1


def find_low_index(arr: list[int], key):
    start, end = 0, len(arr) - 1
    low_index = -1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == key:
            low_index = mid
            end = mid - 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return low_index


def find_high_index(arr: list[int], key):
    start, end = 0, len(arr) - 1
    high_index = -1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == key:
            high_index = mid
            start = mid + 1
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return high_index


def move_zeros_to_left(A: list[int]):
    zero_idx, right = len(A) - 1, len(A) - 1
    while right >= 0:
        if A[zero_idx] == 0 and A[right] != 0:
            A[zero_idx], A[right] = A[right], A[zero_idx]
            zero_idx -= 1
            right -= 1
        else:
            if zero_idx >= 0 and A[zero_idx] != 0:
                zero_idx -= 1

            if right >= zero_idx:
                right = zero_idx - 1
            if right >= 0 and A[right] == 0:
                right -= 1


def find_buy_sell_stock_prices(array):
    pass


def merge_intervals(v: list[Pair]):
    if not v: return []

    result = [v[0]]
    for i in range(1, len(v)):
        if result[-1].second < v[i].first:
            result.append(v[i])
        else:
            result[-1].second = max(result[-1].second, v[i].second)
    return result


def cyclic_sort(nums):
    i = 0
    while i < len(nums):
        while nums[i] != i + 1:
            v1 = nums[i]
            v2 = nums[nums[i]-1]
            nums[i], nums[v1-1] = v2, v1
        i += 1
    return nums


def max_sub_array_of_size_k(k, arr):
    max_sum, curr_sum, left = 0, 0, 0
    for i in range(len(arr)):
        if i >= k:
            curr_sum -= arr[left]
            left += 1

        curr_sum += arr[i]
        max_sum = max(max_sum, curr_sum)
    return max_sum


def smallest_subarray_with_given_sum(s, arr):
    left, curr_sum, min_len = 0, 0, float('inf')
    for i in range(len(arr)):
        if arr[i] >= s:
            return 1
        else:
            curr_sum += arr[i]

            if curr_sum - arr[left] >= s:
                while curr_sum - arr[left] >= s:
                    curr_sum -= arr[left]
                    left += 1
                min_len = min(i-left+1, min_len)
    return 0 if min_len == float('inf') else min_len


def make_squares(arr):
    result = []
    i = 0
    while arr[i] < 0:
        i += 1
    j = i - 1

    while len(result) != len(arr):
        i_val = float('inf') if i >= len(arr) else arr[i]**2
        j_val = float('inf') if j < 0 else arr[j]**2

        if i_val <= j_val:
            result.append(i_val)
            i += 1
        else:
            result.append(j_val)
            j -= 1
    return result


def find_subsets(nums):
    subsets = [[]]
    pass


def find_max_in_bitonic_array(arr):
    if not arr: return float('-inf')

    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l+r)//2

        # increasing
        if arr[l] <= arr[mid]:
            if mid + 1 > r or arr[mid] > arr[mid+1]:
                return arr[mid]
            else:
                l = mid + 1
        # decreasing
        else:
            if mid - 1 < l or arr[mid] > arr[mid-1]:
                return arr[mid]
            else:
                r = mid - 1

def find_max_in_bitonic_array2(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = (start+end) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    # at the end of the while loop, 'start == end'
    return arr[start]


def find_permutations(nums):
    if not nums: return []
    pass


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))

main()
