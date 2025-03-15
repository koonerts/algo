"""
Monotonic

"""
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



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to isMonotonic
    print(isMonotonic([]))
