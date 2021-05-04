package collection

import "container/heap"

type IntMaxHeap []int
func NewIntMaxHeap(vals []int) *IntMaxHeap {
	imh := IntMaxHeap(vals)
	(&imh).Heapify()
	return &imh
}
func (imh IntMaxHeap) Len() int           { return len(imh) }
func (imh IntMaxHeap) Less(i, j int) bool { return imh[i] >= imh[j] }
func (imh IntMaxHeap) Swap(i, j int)      { imh[i], imh[j] = imh[j], imh[i] }

func (imh *IntMaxHeap) Push(val interface{}) {
	*imh = append(*imh, val.(int))
}

func (imh *IntMaxHeap) Pop() interface{} {
	n := len(*imh)-1
	val := (*imh)[n]
	*imh = (*imh)[:n]
	return val
}

func (imh IntMaxHeap) Peek() int {
	return imh[0]
}

func (imh *IntMaxHeap) HeapPush(val int) {
	heap.Push(imh, val)
}

func (imh *IntMaxHeap) HeapPop() int {
	return heap.Pop(imh).(int)
}

func (imh *IntMaxHeap) Heapify() {
	heap.Init(imh)
}