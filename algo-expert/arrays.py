from collections import deque


def getNthFib(n):
    if n <= 1: return 1

    memo = [-1 for _ in range(n)]
    memo[0], memo[1] = 0, 1

    for i in range(2, n):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[-1]


def productSum(array):
    # Write your code here.
    pass


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
    i = 0
    while i < len(array):
        pass


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


print(largestRange([1,1]))
print(largestRange([1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]))
