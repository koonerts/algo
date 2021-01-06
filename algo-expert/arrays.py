
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


print(selectionSort([0,5,4,3,7,6]))