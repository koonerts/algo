"""
Duplicate Value

"""


def firstDuplicateValue(array):
    for i in range(len(array)):
        val = abs(array[i])
        if array[val - 1] < 0:
            return val

        array[val - 1] *= -1
    return -1


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to firstDuplicateValue
    print(firstDuplicateValue([]))
