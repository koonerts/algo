from heapq import *


class Pair:
    def __init__(self, first, second):
        self.first = first
        self.second = second


def find_max_sliding_window(arr, window_size):
    if len(arr) <= window_size:
        return max(arr)

    result = []
    left, right = 0, window_size - 1
    curr_max = float("-inf")
    while right < len(arr) - 1:
        window_max = max(arr[left : right + 1])

    # TODO: come back to


def binary_search_rotated(arr: list[int], key):
    if not arr:
        return -1

    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2

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
    if not a or not b or not c:
        return -1

    def binary_search(start, end, nums, target):
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                end = mid - 1
        return -1

    for i in range(len(a)):
        if (
            binary_search(0, len(b) - 1, b, a[i]) != -1
            and binary_search(0, len(c) - 1, c, a[i]) != -1
        ):
            return a[i]
    return -1


def find_low_index(arr: list[int], key):
    start, end = 0, len(arr) - 1
    low_index = -1
    while start <= end:
        mid = (start + end) // 2
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
        mid = (start + end) // 2
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
    if not v:
        return []

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
            v2 = nums[nums[i] - 1]
            nums[i], nums[v1 - 1] = v2, v1
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
    left, curr_sum, min_len = 0, 0, float("inf")
    for i in range(len(arr)):
        if arr[i] >= s:
            return 1
        else:
            curr_sum += arr[i]

            if curr_sum - arr[left] >= s:
                while curr_sum - arr[left] >= s:
                    curr_sum -= arr[left]
                    left += 1
                min_len = min(i - left + 1, min_len)
    return 0 if min_len == float("inf") else min_len


def make_squares(arr):
    result = []
    i = 0
    while arr[i] < 0:
        i += 1
    j = i - 1

    while len(result) != len(arr):
        i_val = float("inf") if i >= len(arr) else arr[i] ** 2
        j_val = float("inf") if j < 0 else arr[j] ** 2

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
    if not arr:
        return float("-inf")

    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l + r) // 2

        # increasing
        if arr[l] <= arr[mid]:
            if mid + 1 > r or arr[mid] > arr[mid + 1]:
                return arr[mid]
            else:
                l = mid + 1
        # decreasing
        else:
            if mid - 1 < l or arr[mid] > arr[mid - 1]:
                return arr[mid]
            else:
                r = mid - 1


def find_max_in_bitonic_array2(arr):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid + 1]:
            end = mid
        else:
            start = mid + 1

    # at the end of the while loop, 'start == end'
    return arr[start]


def find_permutations(nums):
    if not nums:
        return []
    pass


def search_triplets(arr: list[int]):
    if not arr:
        return []

    arr.sort()
    triplets = []

    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum == 0:
                triplets.append([arr[i], arr[left], arr[right]])
                left += 1
                while left <= right and arr[left] == arr[left - 1]:
                    left += 1
            elif sum < 0:
                left += 1
            else:
                right -= 1
    return triplets


def triplet_sum_close_to_target(arr, target_sum):
    if not arr:
        return []

    arr.sort()
    min_closest_sum = float("inf")

    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum == target_sum:
                return target_sum
            elif sum < target_sum:
                left += 1
            else:
                right -= 1

            diff = abs(target_sum - sum)
            closest_diff = abs(min_closest_sum - target_sum)
            if diff == closest_diff:
                min_closest_sum = min(min_closest_sum, sum)
            elif diff < closest_diff:
                min_closest_sum = sum
    return min_closest_sum


def triplet_with_smaller_sum(arr, target):
    if not arr:
        return []

    arr.sort()
    cntr = 0

    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1
        while left < right:
            sum = arr[i] + arr[left] + arr[right]
            if sum < target:
                cntr += right - left
                left += 1
            else:
                right -= 1

    return cntr


def find_subarrays_with_product_less_than_target(arr, target):
    if not arr:
        return []

    result = []
    left, curr_product = 0, 1
    for i in range(1, len(arr)):
        pass


def can_attend_all_appointments(intervals):
    if not intervals or len(intervals) == 1:
        return True
    start, end = 0, 1
    intervals.sort(key=lambda i: i[start])

    for i in range(1, len(intervals)):
        if intervals[i][start] < intervals[i - 1][end]:
            return False
    return True


def find_key_range(arr, key):
    result = [-1, -1]
    if not arr:
        return result

    def binary_search(l, r):
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] == key:
                return mid
            elif arr[mid] < key:
                l = mid + 1
            else:
                r = mid - 1
        return -1

    idx = binary_search(0, len(arr) - 1)
    if idx == -1:
        return result

    low, high = idx, idx
    result = [low, high]
    while low != -1:
        low = binary_search(0, low - 1)
        if low != -1:
            result[0] = low
    while high != -1:
        high = binary_search(high + 1, len(arr) - 1)
        if high != -1:
            result[1] = high
    return result


def search_min_diff_element(arr, key):
    l, r = 0, len(arr) - 1
    min_diff_element_val = float("inf")
    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == key:
            return arr[mid]
        elif arr[mid] < key:
            l = mid + 1
        else:
            r = mid - 1

        min_diff = abs(key - min_diff_element_val)
        curr_diff = abs(key - arr[mid])
        if curr_diff < min_diff:
            min_diff_element_val = arr[mid]
    return min_diff_element_val


def main():
    print(search_min_diff_element([4, 6, 10], 7))
    print(search_min_diff_element([4, 6, 10], 4))
    print(search_min_diff_element([1, 3, 8, 10, 15], 12))
    print(search_min_diff_element([4, 6, 10], 17))


main()
