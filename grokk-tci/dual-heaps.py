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
            return (-self.max_heap[0] + self.min_heap[0])/2


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
                return (-max_h[0] + min_h[0])/2
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


def main():

    sliding_window_median = SlidingWindowMedian()
    result = sliding_window_median.find_sliding_window_median([1, 2, -1, 3, 5], 2)
    print("Sliding window medians are: " + str(result))

    sliding_window_median = SlidingWindowMedian()
    result = sliding_window_median.find_sliding_window_median([1, 2, -1, 3, 5], 3)
    print("Sliding window medians are: " + str(result))


main()