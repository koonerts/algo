
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
    direction = 1
    x_bounds, y_bounds = len(array), len(array[0])

    result = []
    x, y = 0, 0
    while len(result) < len(array)*len(array[0]):
        if direction == 1:
            while x < x_bound:
                result.append(array[x][y])
                x += 1

        else:

        direction *= -1
    pass


print(smallestDifference([-1,5,10,20,28,3], [26,134,135,15,17]))