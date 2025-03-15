"""
Sort

"""
def heapSort(array):
    min_heap = MinHeap(array)
    result = []
    while min_heap:
        result.append(min_heap.pop())
    return result


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to heapSort
    print(heapSort([]))
