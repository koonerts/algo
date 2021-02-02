class MinHeap:
    def __init__(self, lst):
        self.heap = lst
        self.heapify()

    def heapify(self):
        for i in reversed(range(self.length())):
            self.siftUp(i)

    def siftUp(self, start_idx):
        swap_idx, node = start_idx, self.heap[start_idx]
        left_idx = 2*start_idx + 1

        while left_idx < self.length():
            right_idx = left_idx + 1
            if right_idx < self.length() and self.heap[left_idx] >= self.heap[right_idx]:
                left_idx = right_idx

            self.heap[swap_idx] = self.heap[left_idx]
            swap_idx = left_idx
            left_idx = 2*left_idx + 1

        # swap_idx is now a leaf node - place the node we're working with there
        # and sift it's parent nodes down if need be
        self.heap[swap_idx] = node
        self.siftDown(start_idx, swap_idx)

    def siftDown(self, start_idx, swap_idx):
        node = self.heap[swap_idx]
        while swap_idx > start_idx:
            parent_idx = (swap_idx-1)//2
            if node < self.heap[parent_idx]:
                self.heap[swap_idx] = self.heap[parent_idx]
                swap_idx = parent_idx
            else:
                break
        self.heap[swap_idx] = node

    def length(self):
        return len(self.heap)

    def insert(self, value):
        self.heap.append(value)
        self.siftDown(0, self.length() - 1)

    def pop(self):
        last_item = self.heap.pop()
        if self.heap:
            first_item = self.heap[0]
            self.heap[0] = last_item
            self.siftUp(0)
            return first_item
        return last_item


def heapSort(array):
    min_heap = MinHeap(array)
    result = []
    while min_heap:
        result.append(min_heap.pop())
    return result

mh = MinHeap([8, 5, 2, 9, 5, 6, 3])
print(mh.heap)