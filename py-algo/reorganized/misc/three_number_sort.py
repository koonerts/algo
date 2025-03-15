"""
Number Sort

"""
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



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to threeNumberSort
    print(threeNumberSort([]))
