from heapq import *

class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = array
        self.buildHeap(array)

    def buildHeap(self, array):
        for i in reversed(range(len(array)//2)):
            self.siftUp(i)

    def siftDown(self, startpos, pos):
        newitem = self.heap[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1)//2
            parent = self.heap[parentpos]
            if newitem < parent:
                self.heap[pos] = parent
                pos = parentpos
                continue
            break
        self.heap[pos] = newitem

    def siftUp(self, pos):
        endpos = len(self.heap)
        startpos = pos
        newitem = self.heap[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not self.heap[childpos] < self.heap[rightpos]:
                childpos = rightpos
            # Move the smaller child up.
            self.heap[pos] = self.heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        self.heap[pos] = newitem
        self.siftDown(startpos, pos)

    def peek(self):
        if self.heap: return self.heap[0]
        else: return None

    def remove(self):
        lastelt = self.heap.pop()    # raises appropriate IndexError if heap is empty
        if self.heap:
            returnitem = self.heap[0]
            self.heap[0] = lastelt
            self.siftUp(0)
            return returnitem
        return lastelt

    def insert(self, value):
        self.heap.append(value)
        self.siftDown(0, len(self.heap)-1)


mh = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])