"""
Range

"""


def largestRange(array):
    num_set = set(array)
    max_range = [array[0], array[0]]
    for i in range(len(array)):
        if not max_range[0] or not (max_range[0] <= array[i] <= max_range[1]):
            low, high = array[i], array[i]
            while True:
                if low - 1 not in num_set and high + 1 not in num_set:
                    break
                else:
                    if low - 1 in num_set:
                        low -= 1
                    if high + 1 in num_set:
                        high += 1
            if high - low + 1 > max_range[1] - max_range[0] + 1:
                max_range[0], max_range[1] = low, high
    return max_range


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to largestRange
    print(largestRange([]))
