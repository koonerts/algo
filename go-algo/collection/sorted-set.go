package collection

import "container/list"

type (
	sortedSetNode struct {
		key, val int
	}

	SortedSet struct {
		set map[int]sortedSetNode
		ll *list.List
	}
)

func newSortedSetNode(key, val int) sortedSetNode {
	return sortedSetNode{key: key, val: val}
}

func NewSortedSet() *SortedSet {
	ll := list.New()
	ll.PushFront(nil)
	ll.PushBack(nil)
	return &SortedSet{map[int]sortedSetNode{}, ll}
}

func (ss SortedSet) Len() int { return len(ss.set) }

func (ss *SortedSet) Add(key, val int) {
	if _, ok := ss.set[key]; ok {
		node := ss.set[key]
		(&node).val = val
		return
	}
	ss.set[key] = newSortedSetNode(key, val)
}