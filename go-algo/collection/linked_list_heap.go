package collection

/*import (
	"container/heap"
	"go-algo/linkedlist"
)

type ListNodeHeap []*linkedlist.ListNode
func (lnh ListNodeHeap) Len() int              { return len(lnh) }
func (lnh ListNodeHeap) Swap(i, j int)         { lnh[i], lnh[j] = lnh[j], lnh[i] }
func (lnh ListNodeHeap) Less(i, j int) bool    { return lnh[i].Val < lnh[j].Val }
func (lnh *ListNodeHeap) Push(val interface{}) { *lnh = append(*lnh, val.(*linkedlist.ListNode)) }
func (lnh *ListNodeHeap) Pop() interface{}     {
	item := (*lnh)[lnh.Len()-1]
	*lnh = (*lnh)[:lnh.Len()-1]
	return item
}
func (lnh *ListNodeHeap) Heapify() { heap.Init(lnh)}
func (lnh *ListNodeHeap) HeapPush(node *linkedlist.ListNode) { heap.Push(lnh, node)}
func (lnh *ListNodeHeap) HeapPop() *linkedlist.ListNode { return heap.Pop(lnh).(*linkedlist.ListNode)}
*/