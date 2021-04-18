package collection

import "fmt"

type (
	DNode struct {
		Val        interface{}
		prev, next *DNode
		dlist      *DoublyLinkedList
	}

	DoublyLinkedList struct {
		root *DNode
		size int
	}
)

func newDNode(val interface{}, list *DoublyLinkedList) *DNode {
	return &DNode{Val: val, dlist: list}
}

func (dn *DNode) Next() *DNode {
	return dn.next
}

func (dn *DNode) Prev() *DNode {
	return dn.prev
}

func NewDoublyLinkedList() *DoublyLinkedList {
	dl := &DoublyLinkedList{}
	root := newDNode(nil, dl)
	dl.root = root
	return dl
}

func (dl *DoublyLinkedList) Head() *DNode {
	return dl.root.next
}

func (dl *DoublyLinkedList) Tail() *DNode {
	head := dl.Head()
	if head == nil {
		return nil
	}
	return head.prev
}

func (dl DoublyLinkedList) Len() int {
	return dl.size
}

func (dl *DoublyLinkedList) InsertFront(val interface{}) *DNode {
	var newNode *DNode
	if dl.size == 0 {
		dl.size++
		newNode = newDNode(val, dl)
		dl.root.next = newNode
		dl.root.prev = newNode
		newNode.next = newNode
		newNode.prev = newNode
	} else {
		newNode = dl.InsertBefore(val, dl.Head())
		dl.root.next = newNode
	}
	return newNode
}

func (dl *DoublyLinkedList) InsertBack(val interface{}) *DNode {
	if dl.size == 0 {
		return dl.InsertFront(val)
	}
	dl.size++
	newNode := newDNode(val, dl)
	head, tail := dl.Head(), dl.Tail()
	newNode.next, newNode.prev = head, tail
	head.prev = newNode
	tail.next = newNode
	return newNode
}

func (dl *DoublyLinkedList) InsertBefore(val interface{}, node *DNode) *DNode {
	if node == nil || node.dlist != dl {
		return nil
	}
	dl.size++
	newNode := newDNode(val, dl)
	prev := node.prev
	prev.next, newNode.prev = newNode, prev
	node.prev, newNode.next = newNode, node
	return newNode
}

func (dl *DoublyLinkedList) InsertAfter(val interface{}, node *DNode) *DNode {
	if node == nil || node.dlist != dl {
		return nil
	}
	if node == dl.Tail() {
		return dl.InsertBack(val)
	}
	return dl.InsertBefore(val, node.next)
}

func (dl *DoublyLinkedList) Remove(node *DNode) interface{} {
	if node.dlist == dl {
		dl.size--
		if dl.size == 0 {
			dl.root.next = nil
		} else {
			prev, next := node.prev, node.next
			prev.next, next.prev = next, prev
			if node == dl.Head() {
				dl.root.next = next
			}
		}
	}
	return node.Val
}

func (dl DoublyLinkedList) PrintForward() {
	node, head := dl.Head(), dl.Head()
	i := 0
	for node != nil {
		if i > 0 && node == head {
			break
		}
		fmt.Printf("%v ", node.Val)
		node = node.next
		i++
	}
	fmt.Println()
}

func (dl DoublyLinkedList) PrintBackward() {
	node, tail := dl.Tail(), dl.Tail()
	i := 0
	for node != nil {
		if i > 0 && node == tail {
			break
		}
		fmt.Printf("%v ", node.Val)
		node = node.prev
		i++
	}
	fmt.Println()
}
