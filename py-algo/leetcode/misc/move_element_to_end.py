"""
Element To End

"""


def moveElementToEnd(array, toMove):
    l, r = 0, len(array) - 1
    while l < r:
        if array[l] == toMove:
            array[l], array[r] = array[r], array[l]
            r -= 1
        else:
            l += 1
    return array


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to moveElementToEnd
    print(moveElementToEnd([]))
