"""
Sort

"""


def selectionSort(array):
    if len(array) <= 1:
        return array

    for i in range(len(array) - 1):
        min_idx = i + 1
        for j in range(min_idx + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j

        if array[i] > array[min_idx]:
            array[i], array[min_idx] = array[min_idx], array[i]
    return array


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to selectionSort
    print(selectionSort([]))
