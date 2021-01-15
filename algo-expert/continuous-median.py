from heapq import *

# Do not edit the class below except for
# the insert method. Feel free to add new
# properties and methods to the class.
from typing import List, Any


class ContinuousMedianHandler:
    def __init__(self):
        self.minh = []
        self.maxh = []
        self.median = None

    def insert(self, number):
        if not self.maxh:
            self.maxh.append(-number)
        elif number <= -self.maxh[0]:
            heappush(self.maxh, -number)
        else:
            heappush(self.minh, number)

        self.try_resize()
        self.set_median()
        print(self.median)

    def set_median(self):
        if (len(self.minh) + len(self.maxh)) % 2 == 0:
            self.median = (self.minh[0] + -self.maxh[0])/2
        else:
            self.median = -self.maxh[0]

    def getMedian(self):
        return self.median

    # Resize heaps if either is true:
    #   a) size diff is greater than 1
    #   b) min heap is larger than max
    def try_resize(self):
        if abs(len(self.maxh) - len(self.minh)) > 1 or len(self.minh) > len(self.maxh):
            if len(self.maxh) > len(self.minh):
                heappush(self.minh, -heappop(self.maxh))
            else:
                heappush(self.maxh, -heappop(self.minh))


cmh = ContinuousMedianHandler()
cmh.insert(5)
cmh.insert(10)
cmh.insert(100)
cmh.getMedian()
cmh.insert(200)
cmh.getMedian()