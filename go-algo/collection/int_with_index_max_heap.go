package collection

import "container/heap"

type IntWithIndex struct {
	Idx, Val int
}
type IntWithIndexMaxHeap []IntWithIndex

func (imh IntWithIndexMaxHeap) Len() int           { return len(imh) }
func (imh IntWithIndexMaxHeap) Less(i, j int) bool { return imh[i].Val >= imh[j].Val }
func (imh IntWithIndexMaxHeap) Swap(i, j int)      { imh[i], imh[j] = imh[j], imh[i] }

func (imh *IntWithIndexMaxHeap) Push(val interface{}) {
	*imh = append(*imh, val.(IntWithIndex))
}

func (imh *IntWithIndexMaxHeap) Pop() interface{} {
	n := len(*imh)-1
	val := (*imh)[n]
	*imh = (*imh)[:n]
	return val
}

func (imh *IntWithIndexMaxHeap) HeapPush(val IntWithIndex) {
	heap.Push(imh, val)
}

func (imh *IntWithIndexMaxHeap) HeapPop() IntWithIndex {
	return heap.Pop(imh).(IntWithIndex)
}