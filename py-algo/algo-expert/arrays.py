from collections import deque
from heapq import *
import functools


def print_matrix(matrix):
    for row in matrix:
        print(row)


def getNthFib(n):
    if n <= 1: return 1

    memo = [-1 for _ in range(n)]
    memo[0], memo[1] = 0, 1

    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[-1]


@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    else: return fib(n-1) + fib(n-2)


def findThreeLargestNumbers(array):
    largest_nums = [array[0], array[1], array[2]]
    largest_nums.sort()

    if len(array) == 3:
        return largest_nums

    for i in range(3, len(array)):
        if array[i] >= largest_nums[2]:
            largest_nums[0], largest_nums[1], largest_nums[2] = largest_nums[1], largest_nums[2], array[i]
        elif array[i] >= largest_nums[1]:
            largest_nums[0], largest_nums[1] = largest_nums[1], array[i]
        elif array[i] > largest_nums[0]:
            largest_nums[0] = array[i]
    return largest_nums


def bubbleSort(array):
    if len(array) <= 1: return array

    swap_cnt = 0
    while True:
        for i in range(1, len(array)):
            if array[i] < array[i-1]:
                swap_cnt += 1
                array[i], array[i-1] = array[i-1], array[i]

        if swap_cnt == 0:
            break
        else:
            swap_cnt = 0
    return array


def insertionSort(array):
    if len(array) <= 1: return array

    for i in range(1, len(array)):
        j, k = i, i - 1
        while k >= 0 and array[j] < array[k]:
            array[j], array[k] = array[k], array[j]
            j -= 1
            k -= 1
    return array


def selectionSort(array):
    if len(array) <= 1: return array

    for i in range(len(array) - 1):
        min_idx = i + 1
        for j in range(min_idx + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j

        if array[i] > array[min_idx]:
            array[i], array[min_idx] = array[min_idx], array[i]
    return array


def threeNumberSum(array, targetSum):
    array.sort()

    res = []
    for i in range(len(array) - 1):
        j = i + 1
        k = len(array) - 1
        while j < k:
            sum_val = array[i] + array[j] + array[k]
            if sum_val == targetSum:
                res.append([array[i], array[j], array[k]])
                j += 1
                k -= 1
            elif sum_val < targetSum:
                j += 1
            else:
                k -= 1
    return res


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    p1, p2 = 0, 0
    result = [float('inf'), float('-inf')]
    while True:
        abs_diff = abs(arrayOne[p1] - arrayTwo[p2])
        if abs_diff < abs(result[0] - result[1]):
            result[0], result[1] = arrayOne[p1], arrayTwo[p2]

        if p1 + 1 >= len(arrayOne) and p2 + 1 >= len(arrayTwo):
            return result
        elif p1 + 1 >= len(arrayOne):
            p2 += 1
        elif p2 + 1 >= len(arrayTwo):
            p1 += 1
        else:
            if arrayOne[p1+1] < arrayTwo[p2+1]:
                p1 += 1
            else:
                p2 += 1


def moveElementToEnd(array, toMove):
    l, r = 0, len(array) - 1
    while l < r:
        if array[l] == toMove:
            array[l], array[r] = array[r], array[l]
            r -= 1
        else:
            l += 1
    return array


def isMonotonic(array):
    if len(array) <= 1: return True

    is_increasing, i = None, 0
    while is_increasing is None and i < len(array) - 1:
        if array[i] < array[i+1]:
            is_increasing = True
        elif array[i] > array[i+1]:
            is_increasing = False

    if is_increasing is None:
        return True
    else:
        for j in range(i+1, len(array)):
            if is_increasing and array[j] < array[j-1]:
                return False
            elif (not is_increasing) and array[j] > array[j-1]:
                return False
        return True


def spiralTraverse(array):
    RIGHT, DOWN, LEFT, UP = 0, 1, 2, 3
    direction = RIGHT
    y_left, y_right = 0, len(array[0]) - 1
    x_top, x_bot = 0, len(array) - 1

    result = []
    x, y = 0, 0
    while len(result) < len(array)*len(array[0]):
        if direction == RIGHT:
            y = y_left
            while y_left <= y <= y_right:
                result.append(array[x][y])
                y += 1
            y -= 1
            x_top += 1
        elif direction == DOWN:
            x = x_top
            while x_top <= x <= x_bot:
                result.append(array[x][y])
                x += 1
            x -= 1
            y_right -= 1
        elif direction == LEFT:
            y = y_right
            while y_left <= y <= y_right:
                result.append(array[x][y])
                y -= 1
            y += 1
            x_bot -= 1
        elif direction == UP:
            x = x_bot
            while x_top <= x <= x_bot:
                result.append(array[x][y])
                x -= 1
            x += 1
            y_left += 1
        direction = (direction+1) % 4
    return result


def longestPeak(array):
    if len(array) <= 2: return False

    longest_peak = 0
    i = 1
    while i < len(array) - 1:
        if array[i-1] < array[i] > array[i+1]:
            l, r = i-1, i+1
            while l-1 >= 0 and array[l-1] < array[l]:
                l -= 1
            while r+1 < len(array) and array[r] > array[r+1]:
                r += 1
            longest_peak = max(longest_peak, r-l+1)
            i = r
        else:
            i += 1
    return longest_peak


def firstDuplicateValue(array):
    for i in range(len(array)):
        val = abs(array[i])
        if array[val-1] < 0:
            return val

        array[val-1] *= -1
    return -1


def hasSingleCycle(array):
    curr_idx = 0
    for i in range(len(array)):
        curr_idx = (array[curr_idx] + curr_idx) % len(array)
        if curr_idx == 0 and i < len(array)-1:
            return False
    return curr_idx == 0


def kadanesAlgorithm(array):
    if not array: return 0
    elif len(array) == 1: return array[0]

    max_sum, curr_sum = 0, 0
    for i in range(len(array)):
        curr_sum += array[i]
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum


def riverSizes(matrix):
    results = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if matrix[i][j] == 1:
                q = deque([(i,j)])
                size = 0

                while q:
                    r, c = q.popleft()
                    if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] == 1:
                        size += 1
                        matrix[r][c] = 0
                        q.append((r,c+1))
                        q.append((r,c-1))
                        q.append((r+1,c))
                        q.append((r-1,c))
                results.append(size)
    return results


def removeIslands(matrix):
    visited = set()
    non_islands = set()
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    for i in [0, len(matrix)-1]:
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                q = deque([(i,j)])
                while q:
                    r, c = q.popleft()
                    visited.add((r,c))
                    non_islands.add((r,c))

                    for d in directions:
                        new_r = r + d[0]
                        new_c = c + d[1]
                        if (new_r, new_c) not in visited and 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]) and matrix[new_r][new_c] == 1:
                            q.append((new_r, new_c))

    for i in range(len(matrix)):
        for j in [0, len(matrix[0])-1]:
            if (i,j) not in visited and matrix[i][j] == 1:
                q = deque([(i,j)])
                while q:
                    r, c = q.popleft()
                    visited.add((r,c))
                    non_islands.add((r,c))

                    for d in directions:
                        new_r = r + d[0]
                        new_c = c + d[1]
                        if (new_r, new_c) not in visited and 0 <= new_r < len(matrix) and 0 <= new_c < len(matrix[0]) and matrix[new_r][new_c] == 1:
                            q.append((new_r, new_c))

    for i in range(1, len(matrix)-1):
        for j in range(1, len(matrix[0])-1):
            if (i,j) not in non_islands and matrix[i][j] == 1:
                matrix[i][j] = 0
    return matrix


def getPermutations(array):
    result = []
    if not array: return result

    q = deque([[]])
    for num in array:
        for i in range(len(q)):
            p = q.popleft()
            for j in range(len(p)+1):
                p_copy = p.copy()
                p_copy.insert(j, num)

                if len(p_copy) == len(array):
                    result.append(list(p_copy))
                else:
                    q.append(p_copy)
    return result


def powerset(array):
    q = [[]]
    for num in array:
        for i in range(len(q)):
            item = q[i].copy()
            item.append(num)
            q.append(item)
    return q


def threeNumberSort(array, order):
    low, high = 0, len(array) - 1
    i = 0
    while i <= high:
        if array[i] == order[0]:
            array[i], array[low] = array[low], array[i]
            # increment 'i' and 'low'
            i += 1
            low += 1
        elif array[i] == order[1]:
            i += 1
        else:  # the case for array[i] == 2
            array[i], array[high] = array[high], array[i]
            # decrement 'high' only, after the swap the number at index 'i' could be 0, 1 or 2
            high -= 1
    return array


def sunsetViews(buildings, direction):
    iterator = range(len(buildings)) if direction == 'WEST' else reversed(range(len(buildings)))
    stk = []
    result = []
    for i in iterator:
        if (direction == 'EAST' and i == len(buildings) - 1) or (direction == 'WEST' and i == 0):
            result.append(i)
            stk.append(buildings[i])
        else:
            while stk and stk[-1] < buildings[i]:
                stk.pop()

            if not stk:
                result.append(i)
                stk.append(buildings[i])
    return list(reversed(result)) if direction == 'EAST' else result


def fourNumberSum(array, targetSum):
    if len(array) < 4: return []

    result = []
    array.sort()
    for i in range(len(array)-3):
        for j in range(i+1, len(array)-2):
            k, l = j+1, len(array)-1
            
            while k < l:
                val = array[i] + array[j] + array[k] + array[l]
                if val == targetSum:
                    result.append([array[i], array[j], array[k], array[l]])
                    k += 1
                    l -= 1
                elif val < targetSum:
                    k += 1
                else:
                    l -= 1
    return result


def subarraySort(array):
    l, r = float('inf'), float('inf')
    min_val, max_val = float('inf'), float('-inf')
    for i in range(len(array)-1):
        if array[i] > array[i+1]:
            l = i+1
            break

    if l == float('inf'): return [-1, -1]

    for i in reversed(range(len(array))):
        if array[i] < array[l-1]:
            r = i
            break

    min_val = min(array[l:r+1])
    max_val = max(array[l:r+1])
    low, high = 0, len(array)-1
    while True:
        if (array[low] > min_val or low == l) and (array[high] < max_val or high == r):
            break

        if not (array[low] > min_val or low == l):
            low += 1

        if not (array[high] < max_val or high == r):
            high -= 1
    return [low, high]


def largestRange(array):
    num_set = set(array)
    max_range = [array[0], array[0]]
    for i in range(len(array)):
        if not max_range[0] or not (max_range[0] <= array[i] <= max_range[1]):
            low, high = array[i], array[i]
            while True:
                if low-1 not in num_set and high+1 not in num_set:
                    break
                else:
                    if low-1 in num_set:
                        low -= 1
                    if high+1 in num_set:
                        high += 1
            if high-low+1 > max_range[1]-max_range[0]+1:
                max_range[0], max_range[1] = low, high
    return max_range


def searchInSortedMatrix(matrix, target):
    row, col = len(matrix)-1, 0
    while row >= 0 and col < len(matrix[0]):
        if matrix[row][col] > target: row -= 1
        elif matrix[row][col] < target: col += 1
        else: return [row, col]
    return [-1,-1]


def zigzagTraverse(array):
    pass


def shiftedBinarySearch(array, target):
    low, high = 0, len(array)-1

    while low <= high:
        mid = (high+low)//2
        if array[mid] == target:
            return mid
        else:
            # left side sorted
            if array[low] <= array[mid]:
                if array[low] <= target < array[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if array[mid] < target <= array[high]:
                    low = mid + 1
                else:
                    high = mid - 1
    return -1


def calendarMatching(calendar1, dailyBounds1, calendar2, dailyBounds2, meetingDuration):

    def convert_to_minutes(lst_intervals):
        for intervals in lst_intervals:
            for i in range(len(intervals)):
                start, end = intervals[i]
                start_hrs, start_mins = start.split(':')
                end_hrs, end_mins = end.split(':')

                intervals[i][0] = 60*int(start_hrs) + int(start_mins)
                intervals[i][1] = 60*int(end_hrs) + int(end_mins)

    def convert_to_military(lst_intervals):
        for intervals in lst_intervals:
            for i in range(len(intervals)):
                start_hrs, start_mins = intervals[i][0]//60, "00" if intervals[i][0] % 60 == 0 else intervals[i][0] % 60
                end_hrs, end_mins = intervals[i][1]//60, "00" if intervals[i][1] % 60 == 0 else intervals[i][1] % 60

                intervals[i][0] = f'{start_hrs}:{start_mins}'
                intervals[i][1] = f'{end_hrs}:{end_mins}'

    def merge_overlaps(intervals):
        result = [intervals[0]]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[i-1][1]:
                result.append(intervals[i])
            else:
                intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
        return result

    def get_free_openings(booked_times):
        bounds = [max(dailyBounds1[0], dailyBounds2[0]), min(dailyBounds1[1], dailyBounds2[1])]
        if not booked_times:
            return [bounds]

        openings = []
        if bounds[0] < booked_times[0][0] and booked_times[0][0] - bounds[0] >= meetingDuration:
            openings.append([bounds[0], booked_times[0]])

        prev = booked_times[0]
        for i in range(1, len(booked_times)):
            open_slot = [prev[1], booked_times[i][0]]
            if open_slot[0] >= bounds[0] and open_slot[1] <= bounds[1] and \
                    open_slot[1]-open_slot[0] >= meetingDuration:
                openings.append(open_slot)
            prev = booked_times[i]

        if bounds[1] > booked_times[-1][1] and bounds[1] - booked_times[-1][1] >= meetingDuration:
            openings.append([booked_times[-1][1], bounds[1]])
        return openings

    convert_to_minutes([calendar1, [dailyBounds1], calendar2, [dailyBounds2]])
    booked_times = sorted(calendar1 + calendar2, key=lambda x:x[0])
    booked_times = merge_overlaps(booked_times)
    openings = get_free_openings(booked_times)
    convert_to_military([openings])
    return openings


def mergeSortedArrays(arrays):
    min_heap = []
    for i in range(len(arrays)):
        min_heap.append((arrays[i][0], 0, i))
    heapify(min_heap)

    result = []
    while min_heap:
        num, idx, list_id = heappop(min_heap)
        result.append(num)

        if idx < len(arrays[list_id]) - 1:
            heappush(min_heap, (arrays[list_id][idx+1], idx+1, list_id))
    return result


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


def indexEqualsValue(array):
    lo, hi = 0, len(array) - 1

    while lo <= hi:
        mid = (lo+hi)//2
        if array[mid] == mid:
            return mid
        # elif


def searchForRange(array, target):
    def binary_search_direction(lo, hi, direction):
        idx = -1
        while lo <= hi:
            mid = (lo+hi)//2
            if array[mid] == target:
                idx = mid
                if direction == 'LEFT':
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif array[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1
        return idx

    left, right = -1, -1
    left = binary_search_direction(0, len(array)-1, 'LEFT')
    if left != -1:
        right = binary_search_direction(0, len(array)-1, 'RIGHT')
    return [left, right]


def quickselect(array, k):
    max_heap = []

    for i in range(len(array)):
        if len(max_heap) < k:
            heappush(max_heap, -array[i])
        elif array[i] < -max_heap[0]:
            heappushpop(max_heap, -array[i])
    return -max_heap[0]


def minRewards(scores):
    rewards = [0]*len(scores)
    rewards[0] = 1
    min_reward = 1

    for i, val in enumerate(scores):
        if val < scores[i-1]:
            rewards[i] = rewards[i-1] - 1
            min_reward = min(min_reward, rewards[i])
        else:
            rewards[i] = rewards[i-1] + 1
    print(rewards)
    print([r+abs(min_reward)+1 for r in rewards])



def minimumWaitingTime(queries):
    if not queries: return 0

    queries.sort()
    wait_time = queries[0]
    wait_sum = wait_time
    for i in range(1, len(queries)-1):
        wait_time += queries[i]
        wait_sum += wait_time
    return wait_sum


def taskAssignment(k, tasks):
    idx_map = {}
    for i, v in enumerate(tasks):
        if v not in idx_map:
            idx_map[v] = [i]
        else:
            idx_map[v].append(i)

    tasks.sort()
    lo, hi = 0, len(tasks)-1

    results = []
    while lo < hi:
        v1 = idx_map[tasks[lo]][-1]
        idx_map[tasks[lo]].pop()

        v2 = idx_map[tasks[hi]][-1]
        idx_map[tasks[hi]].pop()

        results.append([v1, v2])

        lo += 1
        hi -= 1
    return results


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


print(mergeSort([8, 5, 2, 9, 5, 6, 3]))
# result = calendarMatching([["9:00", "10:30"], ["12:00", "13:00"], ["16:00", "18:00"]], ["9:00", "20:00"],
#                           [["10:00", "11:30"], ["12:30", "14:30"], ["14:30", "15:00"], ["16:00", "17:00"]], ["10:00", "18:30"],
#                           45)
# print(result)
