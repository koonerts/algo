package main

// Do not edit the class below except for the buildHeap,
// siftDown, siftUp, peek, remove, and insert methods.
// Feel free to add new properties and methods to the class.
type MinHeap []int

func NewMinHeap(array []int) *MinHeap {
	// Do not edit the lines below.
	heap := MinHeap(array)
	ptr := &heap
	ptr.BuildHeap(array)
	return ptr
}

func (h *MinHeap) BuildHeap(array []int) {
	for i := len(array)-1; i >= 0; i-- {
		h.siftUp(i)
	}
}

func (h *MinHeap) siftDown(startIdx, endIdx int) {
	node := (*h)[endIdx]
	for startIdx < endIdx {
		parentIdx := (endIdx-1)/2
		if node < (*h)[parentIdx] {
			(*h)[endIdx] = (*h)[parentIdx]
			endIdx = parentIdx
		} else{
			break
		}
	}
	(*h)[endIdx] = node
}

func (h *MinHeap) siftUp(startIndex int) {
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

func (h *MinHeap) Peek() int {
	if len(*h) > 0 { 
		return (*h)[0] 
	} else {
		return -1
	}
}

func (h *MinHeap) Remove() int {
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

func (h *MinHeap) Insert(value int) {
	*h = append(*h, value)
	h.siftDown(0, len(*h)-1)
}

func (h *MinHeap) Length() int {
	return len(*h)
}
