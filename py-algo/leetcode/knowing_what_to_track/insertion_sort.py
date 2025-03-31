"""
Sort

"""


def insertionSort(array):
    if len(array) <= 1:
        return array

    for i in range(1, len(array)):
        j, k = i, i - 1
        while k >= 0 and array[j] < array[k]:
            array[j], array[k] = array[k], array[j]
            j -= 1
            k -= 1
    return array


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to insertionSort
    print(insertionSort([]))
