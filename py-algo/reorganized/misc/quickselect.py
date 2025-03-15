"""
Quickselect

"""
def quickselect(array, k):
    max_heap = []

    for i in range(len(array)):
        if len(max_heap) < k:
            heappush(max_heap, -array[i])
        elif array[i] < -max_heap[0]:
            heappushpop(max_heap, -array[i])
    return -max_heap[0]



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to quickselect
    print(quickselect([]))
