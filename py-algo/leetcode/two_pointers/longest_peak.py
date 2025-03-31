"""
Peak

"""


def longestPeak(array):
    if len(array) <= 2:
        return False

    longest_peak = 0
    i = 1
    while i < len(array) - 1:
        if array[i - 1] < array[i] > array[i + 1]:
            l, r = i - 1, i + 1
            while l - 1 >= 0 and array[l - 1] < array[l]:
                l -= 1
            while r + 1 < len(array) and array[r] > array[r + 1]:
                r += 1
            longest_peak = max(longest_peak, r - l + 1)
            i = r
        else:
            i += 1
    return longest_peak


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to longestPeak
    print(longestPeak([]))
