"""
Difference

"""


def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()

    p1, p2 = 0, 0
    result = [float("inf"), float("-inf")]
    while True:
        abs_diff = abs(arrayOne[p1] - arrayTwo[p2])
        if abs_diff < abs(result[0] - result[1]):
            result[0], result[1] = arrayOne[p1], arrayTwo[p2]

        if p1 + 1 >= len(arrayOne) and p2 + 1 >= len(arrayTwo):
            return result
        elif p1 + 1 >= len(arrayOne):
            p2 += 1
        elif p2 + 1 >= len(arrayTwo):
            p1 += 1
        else:
            if arrayOne[p1 + 1] < arrayTwo[p2 + 1]:
                p1 += 1
            else:
                p2 += 1


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to smallestDifference
    print(smallestDifference([]))
