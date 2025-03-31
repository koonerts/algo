"""
Find_k_largest_numbers

"""


def find_k_largest_numbers(nums, k):
    min_heap = []
    for num in nums:
        if len(min_heap) < k:
            heappush(min_heap, num)
        elif num > min_heap[0]:
            heappushpop(min_heap, num)
    return min_heap


# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_k_largest_numbers
    print(find_k_largest_numbers([]))
