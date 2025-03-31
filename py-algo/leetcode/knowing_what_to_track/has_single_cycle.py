"""
Single Cycle

"""


def hasSingleCycle(array):
    curr_idx = 0
    for i in range(len(array)):
        curr_idx = (array[curr_idx] + curr_idx) % len(array)
        if curr_idx == 0 and i < len(array) - 1:
            return False
    return curr_idx == 0


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to hasSingleCycle
    print(hasSingleCycle([]))
