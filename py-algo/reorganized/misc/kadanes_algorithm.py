"""
Algorithm

"""
def kadanesAlgorithm(array):
    if not array: return 0
    elif len(array) == 1: return array[0]

    max_sum, curr_sum = 0, 0
    for i in range(len(array)):
        curr_sum += array[i]
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
    return max_sum



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to kadanesAlgorithm
    print(kadanesAlgorithm([]))
