package collection

//type MyListNodeHeap []*ListNode
//
//func NewMyLinkedListHeap(nodes []*ListNode) *MyListNodeHeap {
//	mlnh := MyListNodeHeap(nodes)
//	mlnh.heapify()
//	return &mlnh
//}
//
//func (mlnh *MyListNodeHeap) heapify() {
//	for i := len(*mlnh)/2; i >= 0; i-- {
//		mlnh.siftUp(i)
//	}
//}
//
//func (mlnh *MyListNodeHeap) siftDown(startIdx, swapIdx int) {
//	node := (*mlnh)[swapIdx]
//	for startIdx < swapIdx {
//		parentIdx := (swapIdx-1)/2
//		parentNode := (*mlnh)[parentIdx]
//		if node.Val < parentNode.Val {
//			(*mlnh)[swapIdx] = (*mlnh)[parentIdx]
//			swapIdx = parentIdx
//		} else {
//			break
//		}
//	}
//	(*mlnh)[swapIdx] = node
//}
//
//func (mlnh *MyListNodeHeap) siftUp(swapIdx int) {
//	node, startIdx := (*mlnh)[swapIdx], swapIdx
//	leftIdx := 2*swapIdx + 1
//	heapLen := len(*mlnh)
//	for leftIdx < heapLen {
//		rightIdx := leftIdx+1
//		if rightIdx < heapLen && (*mlnh)[rightIdx].Val <= (*mlnh)[leftIdx].Val {
//			leftIdx = rightIdx
//		}
//		(*mlnh)[swapIdx] = (*mlnh)[leftIdx]
//		swapIdx = leftIdx
//		leftIdx = leftIdx*2 + 1
//	}
//	(*mlnh)[swapIdx] = node
//	mlnh.siftDown(startIdx, swapIdx)
//}
//
//func (mlnh *MyListNodeHeap) Push(node *ListNode)  {
//	*mlnh = append(*mlnh, node)
//	mlnh.siftDown(0, len(*mlnh)-1)
//}
//
//func (mlnh *MyListNodeHeap) Pop() *ListNode {
//	n := len(*mlnh)
//	last := (*mlnh)[n-1]
//	*mlnh = (*mlnh)[:n-1]
//
//	if n == 1 {
//		return last
//	}
//
//	first := (*mlnh)[0]
//	(*mlnh)[0] = last
//	mlnh.siftUp(0)
//	return first
//}
//
//func (mlnh *MyListNodeHeap) Peek() *ListNode {
//	if len(*mlnh) == 0 {return nil}
//	return (*mlnh)[0]
//}