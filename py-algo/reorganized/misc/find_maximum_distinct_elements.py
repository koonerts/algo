"""
Find_maximum_distinct_elements

Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array
    such that we are left with maximum distinct numbers.

    Example 1:
    Input: [7, 3, 5, 8, 5, 3, 3], and K=2
    Output: 3
    Explanation: We can remove two occurrences of 3 to be left with 3 distinct numbers [7, 3, 8], we have
    to skip 5 because it is not distinct and occurred twice.
    Another solution could be to remove one instance of '5' and '3' each to be left with three
    distinct numbers [7, 5, 8], in this case, we have to skip 3 because it occurred twice.

    Example 2:
    Input: [3, 5, 12, 11, 12], and K=3
    Output: 2
    Explanation: We can remove one occurrence of 12, after which all numbers will become distinct. Then
    we can delete any two numbers which will leave us 2 distinct numbers in the result.

    Example 3:
    Input: [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], and K=2
    Output: 3
    Explanation: We can remove one occurrence of '4' to get three distinct numbers.
"""
def find_maximum_distinct_elements(nums, k):
    """
    Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array
    such that we are left with maximum distinct numbers.

    Example 1:
    Input: [7, 3, 5, 8, 5, 3, 3], and K=2
    Output: 3
    Explanation: We can remove two occurrences of 3 to be left with 3 distinct numbers [7, 3, 8], we have
    to skip 5 because it is not distinct and occurred twice.
    Another solution could be to remove one instance of '5' and '3' each to be left with three
    distinct numbers [7, 5, 8], in this case, we have to skip 3 because it occurred twice.

    Example 2:
    Input: [3, 5, 12, 11, 12], and K=3
    Output: 2
    Explanation: We can remove one occurrence of 12, after which all numbers will become distinct. Then
    we can delete any two numbers which will leave us 2 distinct numbers in the result.

    Example 3:
    Input: [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], and K=2
    Output: 3
    Explanation: We can remove one occurrence of '4' to get three distinct numbers.
    """
    freq_map = {}
    for num in nums:
        freq_map[num] = freq_map.get(num, 0) + 1

    distinct_cnt = 0
    heap = []
    for num, freq in freq_map.items():
        if freq == 1:
            distinct_cnt += 1
        else:
            heappush(heap, (freq, num))

    while k > 0:
        if heap:
            freq, num = heappop(heap)
            k -= freq - 1
            if k >= 0:
                distinct_cnt += 1
            else:
                break
        else:
            distinct_cnt -= k
            break

    return distinct_cnt



# Example usage
if __name__ == "__main__":
    # TODO: Add example calls to find_maximum_distinct_elements
    print(find_maximum_distinct_elements([]))
