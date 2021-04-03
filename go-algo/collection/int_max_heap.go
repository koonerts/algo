package collection


type IntMaxHeap []int

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