from heapq import *
import math


def find_k_largest_numbers(nums, k):
    min_heap = []
    for num in nums:
        if len(min_heap) < k:
            heappush(min_heap, num)
        elif num > min_heap[0]:
            heappushpop(min_heap, num)
    return min_heap


def find_Kth_smallest_number(nums, k):
    """
    Given an unsorted array of numbers, find Kth smallest number in it.
    Please note that it is the Kth smallest number in the sorted order, not the Kth distinct element.

    Example 1:
    Input: [1, 5, 12, 2, 11, 5], K = 3
    Output: 5
    Explanation: The 3rd smallest number is '5', as the first two smaller numbers are [1, 2].

    Example 2:
    Input: [1, 5, 12, 2, 11, 5], K = 4
    Output: 5
    Explanation: The 4th smallest number is '5', as the first three small numbers are [1, 2, 5].

    Example 3:
    Input: [5, 12, 11, -1, 12], K = 3
    Output: 11
    Explanation: The 3rd smallest number is '11', as the first two small numbers are [5, -1].
    """
    min_heap = []
    for num in nums:
        if len(min_heap) < k:
            heappush(min_heap, num)
        elif num > min_heap[0]:
            heappushpop(min_heap, num)
    return min_heap[0]


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.euclidean_dist = math.sqrt(self.x**2 + self.y**2)

    def __lt__(self, other):
        return self.euclidean_dist > other.euclidean_dist

    def is_closer_to_origin_than(self, other):
        return not self < other

    def print_point(self):
        print("[" + str(self.x) + ", " + str(self.y) + "] ", end="")


def find_closest_points(points: list[Point], k: int):
    """
    Given an array of points in the a 2D plane, find ‘K’ closest points to the origin.

    Example 1:
    Input: points = [[1,2],[1,3]], K = 1
    Output: [[1,2]]
    Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
    The Euclidean distance between (1, 3) and the origin is sqrt(10).
    Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

    Example 2:
    Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
    Output: [[1, 3], [2, -1]]
    """
    result = []
    for point in points:
        if len(result) < k:
            heappush(result, point)
        elif point.is_closer_to_origin_than(result[0]):
            heappushpop(result, point)

    return result


def minimum_cost_to_connect_ropes(ropeLengths) -> int:
    """
    Given ‘N’ ropes with different lengths, we need to connect these ropes into one big rope with minimum cost.
    The cost of connecting two ropes is equal to the sum of their lengths.

    Example 1:
    Input: [1, 3, 11, 5]
    Output: 33
    Explanation: First connect 1+3(=4), then 4+5(=9), and then 9+11(=20). So the total cost is 33 (4+9+20)

    Example 2:
    Input: [3, 4, 5, 6]
    Output: 36
    Explanation: First connect 3+4(=7), then 5+6(=11), 7+11(=18). Total cost is 36 (7+11+18)

    Example 3:
    Input: [1, 3, 11, 5, 2]
    Output: 42
    Explanation: First connect 1+2(=3), then 3+3(=6), 6+5(=11), 11+11(=22). Total cost is 42 (3+6+11+22)
    """
    cost = 0
    heapify(ropeLengths)

    while len(ropeLengths) > 1:
        temp_cost = heappop(ropeLengths) + heappop(ropeLengths)
        cost += temp_cost
        heappush(ropeLengths, temp_cost)

    return cost


def find_k_frequent_numbers(nums, k):
    """
    Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

    Example 1:
    Input: [1, 3, 5, 12, 11, 12, 11], K = 2
    Output: [12, 11]
    Explanation: Both '11' and '12' appeared twice.

    Example 2:
    Input: [5, 12, 11, 3, 11], K = 2
    Output: [11, 5] or [11, 12] or [11, 3]
    Explanation: Only '11' appeared twice, all other numbers appeared once.
    """
    freq_map = {}
    heap = []

    for num in nums:
        if num not in freq_map:
            freq_map[num] = 1
        else:
            freq_map[num] += 1

    for num, freq in freq_map.items():
        if len(heap) < k:
            heappush(heap, (freq, num))
        elif freq > heap[0][0]:
            heappushpop(heap, (freq, num))

    return [item[1] for item in heap]


def sort_character_by_frequency(str):
    """
    Given a string, sort it based on the decreasing frequency of its characters.

    Example 1:
    Input: "Programming"
    Output: "rrggmmPiano"
    Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.

    Example 2:
    Input: "abcbab"
    Output: "bbbaac"
    Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
    """
    freq_map = {}

    for c in str:
        freq_map[c] = freq_map.get(c, 0) + 1

    max_heap = []
    for c, freq in freq_map.items():
        heappush(max_heap, (-freq, c))

    ret_list = []
    while max_heap:
        freq, c = heappop(max_heap)
        ret_list += c * -freq

    return "".join(ret_list)


class KthLargestNumberInStream:
    def __init__(self, nums, k):
        self.k = k
        self.min_heap = []

        for num in nums:
            self.add(num)

    def add(self, num) -> int:
        if len(self.min_heap) < self.k:
            heappush(self.min_heap, num)
        elif num > self.min_heap[0]:
            heappushpop(self.min_heap, num)

        return self.min_heap[0]


def find_closest_elements(arr, K, X):
    """
    Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array.
    Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.

    Example 1:
    Input: [5, 6, 7, 8, 9], K = 3, X = 7
    Output: [6, 7, 8]

    Example 2:
    Input: [2, 4, 5, 6, 9], K = 3, X = 6
    Output: [4, 5, 6]

    Example 3:
    Input: [2, 4, 5, 6, 9], K = 3, X = 10
    Output: [5, 6, 9]
    """
    result = []

    # TODO: Can be improved by using binary search for finding the closest element
    #       and then 2 pointers expanding to either side of that element until reaching K
    for num in arr:
        diff = abs(num - X)

        if len(result) < K:
            heappush(result, (-diff, num))
        elif diff < -result[0][0]:
            heappushpop(result, (-diff, num))

    return [item[1] for item in result]


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


def find_sum_of_elements(nums, k1, k2):
    """
    Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

    Example 1:
    Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6
    Output: 23
    Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
                 between 5 and 15 is 23 (11+12).

    Example 2:
    Input: [3, 5, 8, 7], and K1=1, K2=4
    Output: 12
    Explanation: The sum of the numbers between the 1st smallest number (3) and the 4th smallest
                 number (8) is 12 (5+7).
    """
    # TODO: Come back to
    return -1


def rearrange_string(str):
    """
    Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

    Example 1:
    Input: "aappp"
    Output: "papap"
    Explanation: In "papap", none of the repeating characters come next to each other.

    Example 2:
    Input: "Programming"
    Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
    Explanation: None of the repeating characters come next to each other.

    Example 3:
    Input: "aapa"
    Output: ""
    Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".
    """
    # TODO: Come back to
    return ""


def reorganize_string(str, k):
    """
    Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are
    at least ‘K’ distance apart from each other.

    Example 1:
    Input: "mmpp", K=2
    Output: "mpmp" or "pmpm"
    Explanation: All same characters are 2 distance apart.

    Example 2:
    Input: "Programming", K=3
    Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more
    Explanation: All same characters are 3 distance apart.

    Example 3:
    Input: "aab", K=2
    Output: "aba"
    Explanation: All same characters are 2 distance apart.

    Example 4:
    Input: "aappa", K=3
    Output: ""
    Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.
    """
    # TODO: Come back to
    return ""


def schedule_tasks(tasks, k):
    """
    You are given a list of tasks that need to be run, in any order, on a server.
    Each task will take one CPU interval to execute but once a task has finished, it has a cooling period
    during which it can’t be run again.

    If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that
    the server needs to finish all tasks. If at any time the server can’t execute any task then it must stay idle.

    Example 1:
    Input: [a, a, a, b, c, c], K=2
    Output: 7
    Explanation: a -> c -> b -> a -> c -> idle -> a

    Example 2:
    Input: [a, b, a], K=3
    Output: 5
    Explanation: a -> b -> idle -> idle -> a
    """
    # TODO: Come back to
    interval_count = 0
    return interval_count


class FrequencyStack:
    """
    Design a class that simulates a Stack data structure, implementing the following two operations:
        push(int num): Pushes the number ‘num’ on the stack.
        pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.

    Example:
    After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)
    1. pop() should return 2, as it is the most frequent number
    2. Next pop() should return 1
    3. Next pop() should return 2
    """

    # TODO: Come back to
    def push(self, num):
        return 0

    def pop(self):
        return -1
