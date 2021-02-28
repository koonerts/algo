package collection

type MyMinHeap []int

func NewMyMinHeap(array []int) *MyMinHeap {
	heap := MyMinHeap(array)
	ptr := &heap
	ptr.BuildHeap(array)
	return ptr
}

func (h *MyMinHeap) BuildHeap(array []int) {
	for i := len(array)/2; i >= 0; i-- {
		h.siftUp(i)
	}
}

func (h *MyMinHeap) siftDown(startIdx, endIdx int) {
	node := (*h)[endIdx]
	for startIdx < endIdx {
		parentIdx := (endIdx-1)/2
		if node < (*h)[parentIdx] {
			(*h)[endIdx] = (*h)[parentIdx]
			endIdx = parentIdx
		} else {
			break
		}
	}
	(*h)[endIdx] = node
}

func (h *MyMinHeap) siftUp(startIndex int) {
	swapIdx, node := startIndex, (*h)[startIndex]
	leftIdx := 2*startIndex + 1
	for leftIdx < len(*h) {
		rightIdx := leftIdx + 1
		if rightIdx < len(*h) && (*h)[rightIdx] <= (*h)[leftIdx] {
			leftIdx = rightIdx
		}
		(*h)[swapIdx] = (*h)[leftIdx]
		swapIdx = leftIdx
		leftIdx = leftIdx*2 + 1
	}
	(*h)[swapIdx] = node
	h.siftDown(startIndex, swapIdx)
}

func (h *MyMinHeap) Peek() int {
	return (*h)[0]
}

func (h *MyMinHeap) Remove() int {
	lst := (*h)[len(*h)-1]
	*h = (*h)[:len(*h)-1]
	if len(*h) == 0 {
		return lst
	} else {
		fst := (*h)[0]
		(*h)[0] = lst
		h.siftUp(0)
		return fst
	}
}

func (h *MyMinHeap) Insert(value int) {
	*h = append(*h, value)
	h.siftDown(0, len(*h)-1)
}

func (h *MyMinHeap) Length() int {
	return len(*h)
}
