"""
Sort

"""


def bubbleSort(array):
    if len(array) <= 1:
        return array

    swap_cnt = 0
    while True:
        for i in range(1, len(array)):
            if array[i] < array[i - 1]:
                swap_cnt += 1
                array[i], array[i - 1] = array[i - 1], array[i]

        if swap_cnt == 0:
            break
        else:
            swap_cnt = 0
    return array


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to bubbleSort
    print(bubbleSort([]))
