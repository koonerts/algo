"""
Three Largest Numbers

"""


def findThreeLargestNumbers(array):
    largest_nums = [array[0], array[1], array[2]]
    largest_nums.sort()

    if len(array) == 3:
        return largest_nums

    for i in range(3, len(array)):
        if array[i] >= largest_nums[2]:
            largest_nums[0], largest_nums[1], largest_nums[2] = (
                largest_nums[1],
                largest_nums[2],
                array[i],
            )
        elif array[i] >= largest_nums[1]:
            largest_nums[0], largest_nums[1] = largest_nums[1], array[i]
        elif array[i] > largest_nums[0]:
            largest_nums[0] = array[i]
    return largest_nums


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to findThreeLargestNumbers
    print(findThreeLargestNumbers([]))
