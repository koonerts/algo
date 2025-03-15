import heapq
from heapq import *


class MedianOfAStream:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def insert_num(self, num):
        if not self.max_heap:
            heappush(self.max_heap, -num)
        else:
            if num < -self.max_heap[0]:
                heappush(self.max_heap, -num)
            else:
                heappush(self.min_heap, num)

            len_diff = abs(len(self.min_heap) - len(self.max_heap))
            is_min_larger = len(self.min_heap) > len(self.max_heap)

            if len_diff > 1 or is_min_larger:
                if is_min_larger:
                    heappush(self.max_heap, -heappop(self.min_heap))
                else:
                    heappush(self.min_heap, -heappop(self.max_heap))

    def find_median(self):
        heap_len = len(self.min_heap) + len(self.max_heap)
        if heap_len % 2 == 1:
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


class SlidingWindowMedian:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def find_sliding_window_median(self, nums: list[int], k: int):
        """
        Given an array of numbers and a number ‘k’,
        find the median of all the ‘k’ sized sub-arrays (or windows) of the array.

        Example 1:
        Input: nums=[1, 2, -1, 3, 5], k = 2
        Output: [1.5, 0.5, 1.0, 4.0]
        Explanation: Lets consider all windows of size ‘2’:

        [1, 2, -1, 3, 5] -> median is 1.5
        [1, 2, -1, 3, 5] -> median is 0.5
        [1, 2, -1, 3, 5] -> median is 1.0
        [1, 2, -1, 3, 5] -> median is 4.0

        Example 2:
        Input: nums=[1, 2, -1, 3, 5], k = 3
        Output: [1.0, 2.0, 3.0]
        Explanation: Lets consider all windows of size ‘3’:

        [1, 2, -1, 3, 5] -> median is 1.0
        [1, 2, -1, 3, 5] -> median is 2.0
        [1, 2, -1, 3, 5] -> median is 3.0
        """

        """
        Steps: 1) Increase window size until size k while maintaining min/max heaps
                    - Heap rules: if nums[i] < -max_heap[0] -> insert into max_heap
                                  else insert into min_heap
                                  
                                  Resize heaps if difference in heap lengths > 1 or length of min_heap > length of max_heap
               2) If i == k:
                      - insert median (either -max_heap[0] or avg(-max_heap[0] + min_heap[0]))
                      - reduce sliding window and pop from appropriate heap
               3) Repeat for all remaining i
        """
        start, min_h, max_h, result = 0, [], [], []

        def insert_num(num: int):
            if not max_h or num <= -max_h[0]:
                heappush(max_h, -num)
            else:
                heappush(min_h, num)

            heap_length_diff = abs(len(min_h) - len(max_h))
            is_min_heap_larger = len(min_h) > len(max_h)

            while heap_length_diff > 1 or is_min_heap_larger:
                if is_min_heap_larger:
                    heappush(max_h, -heappop(min_h))
                else:
                    heappush(min_h, -heappop(max_h))

                heap_length_diff = abs(len(min_h) - len(max_h))
                is_min_heap_larger = len(min_h) > len(max_h)

        def get_median() -> float:
            heap_len = len(min_h) + len(max_h)
            if heap_len % 2 == 0:
                return (-max_h[0] + min_h[0]) / 2
            else:
                return -max_h[0]

        def pop_num(num: int):
            def remove(heap, num):
                ind = heap.index(num)  # find the element
                # move the element to the end and delete it
                heap[ind] = heap[-1]
                del heap[-1]
                # we can use heapify to readjust the elements but that would be O(N),
                # instead, we will adjust only one element which will O(logN)
                if ind < len(heap):
                    heapq._siftup(heap, ind)
                    heapq._siftdown(heap, 0, ind)

            if num <= -max_h[0]:
                remove(max_h, -num)
            else:
                remove(min_h, num)

        for i, num in enumerate(nums):
            insert_num(num)
            window_len = i - start + 1
            if window_len == k:
                result.append(get_median())
                if i < len(nums) - 1:
                    pop_num(nums[start])
                    start += 1

        return result


def find_maximum_capital(
    capital: list[int], profits: list[int], numberOfProjects: int, initialCapital: int
) -> int:
    """
    Given a set of investment projects with their respective profits, we need to find the most profitable projects.
    We are given an initial capital and are allowed to invest only in a fixed number of projects.
    Our goal is to choose projects that give us the maximum profit.

    Write a function that returns the maximum total capital after selecting the most profitable projects.
    We can start an investment project only when we have the required capital.
    Once a project is selected, we can assume that its profit has become our capital.

    Example 1:
    Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial Capital=1, Number of Projects=2
    Output: 6
    Explanation:
    With initial capital of ‘1’, we will start the second project which will give us profit of ‘2’. Once we selected our first project, our total capital will become 3 (profit + initial capital).
    With ‘3’ capital, we will select the third project, which will give us ‘3’ profit.
    After the completion of the two projects, our total capital will be 6 (1+2+3).

    Example 2:
    Input: Project Capitals=[0,1,2,3], Project Profits=[1,2,3,5], Initial Capital=0, Number of Projects=3
    Output: 8
    Explanation:
    With ‘0’ capital, we can only select the first project, bringing out capital to 1.
    Next, we will select the second project, which will bring our capital to 3.
    Next, we will select the fourth project, giving us a profit of 5.
    After selecting the three projects, our total capital will be 8 (1+2+5).
    """
    # TODO: Come back to
    return -1


class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def find_next_interval(intervals: list[Interval]):
    """
    Given an array of intervals, find the next interval of each interval.
    In a list of intervals, for an interval ‘i’ its next interval ‘j’ will have the
    smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.

    Write a function to return an array containing indices of the next interval of each input interval.
    If there is no next interval of a given interval, return -1.
    It is given that none of the intervals have the same start point.

    Example 1:
    Input: Intervals [[2,3], [3,4], [5,6]]
    Output: [1, 2, -1]
    Explanation:
    The next interval of [2,3] is [3,4] having index ‘1’.
    Similarly, the next interval of [3,4] is [5,6] having index ‘2’.
    There is no next interval for [5,6] hence we have ‘-1’.

    Example 2:
    Input: Intervals [[3,4], [1,5], [4,6]]
    Output: [2, -1, -1]
    Explanation: The next interval of [3,4] is [4,6] which has index ‘2’. There is no next interval for [1,5] and [4,6].
    """
    # TODO: Come back to
    result = []
    return result


def main():
    result = find_next_interval([Interval(2, 3), Interval(3, 4), Interval(5, 6)])
    print("Next interval indices are: " + str(result))

    result = find_next_interval([Interval(3, 4), Interval(1, 5), Interval(4, 6)])
    print("Next interval indices are: " + str(result))


main()
