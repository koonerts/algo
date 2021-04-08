package linkedlist

import (
	"fmt"
	"go-algo/ext/mathext"
)

type ListNode struct {
	Val int
	Next *ListNode
}

type NodeRnd struct {
	Val int
	Next *NodeRnd
	Random *NodeRnd
}

type LinkedList struct {
	Value int
	Next  *LinkedList
}

func CreateListNodeList(vals []int) *ListNode {
	var head, prev *ListNode
	for _, val := range vals {
		node := &ListNode{val, nil}
		if head == nil {
			head = node
		} else {
			prev.Next = node
		}
		prev = node
	}
	return head
}

func CreateLinkedList(vals []int) *LinkedList {
	var head, prev *LinkedList
	for _, val := range vals {
		node := &LinkedList{val, nil}
		if head == nil {
			head = node
		} else {
			prev.Next = node
		}
		prev = node
	}
	return head
}

func PrintLinkedList(head *LinkedList) {
	node := head
	for node != nil {
		fmt.Print(node.Value)
		node = node.Next
		if node != nil {
			fmt.Print("->")
		} else {
			fmt.Println()
		}
	}
}

func PrintListNodeList(head *ListNode) {
	fmt.Print(SprintListNodeList(head))
}

func SprintListNodeList(head *ListNode) string {
	node := head
	str := ""
	for node != nil {
		str += fmt.Sprint(node.Val)
		node = node.Next
		if node != nil {
			str += "->"
		} else {
			str += fmt.Sprintln()
		}
	}
	return str
}

func printNodeList(head *NodeRnd) {
	node := head
	for node != nil {
		fmt.Print(node.Val)
		node = node.Next
		if node != nil {
			fmt.Print("->")
		} else {
			fmt.Println()
		}
	}
}


func OddEvenList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil || head.Next.Next == nil {return head}

	even, evenHead := head, head
	odd, oddHead := even.Next, even.Next

	var prevEven, prevOdd *ListNode
	for even != nil || odd != nil {
		if prevEven != nil {prevEven.Next = even}
		if prevOdd != nil {prevOdd.Next = odd}

		prevEven = even
		prevOdd = odd
		for i := 0; i < 2; i ++ {
			if even != nil {even = even.Next}
			if odd != nil {odd = odd.Next}
		}
	}
	if prevEven != nil {prevEven.Next = oddHead}
	return evenHead
}


func insertBefore(nodePtr, newNode *ListNode) {
	// deep-copy nodePtr and beyond to nodePtrCopy
	var nodePtrCopy, prev *ListNode
	iterPtr := nodePtr // copy pointer to iter so we don't alter original pointer
	for iterPtr != nil {
		node := &ListNode{Val: iterPtr.Val}
		if nodePtrCopy == nil {
			nodePtrCopy = node
		}
		if prev != nil {
			prev.Next = node
		}
		prev = node
		iterPtr = iterPtr.Next
	}

	// replace underlying node value at *nodePtr to requested node
	*nodePtr = *newNode

	// have nodePtr now point to our nodePtrCopy
	nodePtr.Next = nodePtrCopy
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil || (l1.Val == 0 && l1.Next == nil) {return l2}
	if l2 == nil || (l2.Val == 0 && l2.Next == nil) {return l1}

	var head, prev *ListNode
	n1, n2 := l1, l2
	carry := 0
	for n1 != nil || n2 != nil {
		n1val, n2val := 0, 0
		if n1 != nil {n1val = n1.Val}
		if n2 != nil {n2val = n2.Val}
		val := n1val + n2val + carry
		carry = val/10
		val %= 10
		node := &ListNode{Val:val}
		if head == nil {
			head = node
		}
		if prev != nil {
			prev.Next = node
		}
		prev = node
	}
	if carry == 1 {
		prev.Next = &ListNode{Val:1}
	}
	return head
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	} else if l2 == nil {
		return l1
	}

	var returnHead, prev *ListNode
	n1, n2 := l1, l2

	if n1.Val <= n2.Val {
		returnHead = n1
		prev = n1
		n1 = n1.Next
	} else {
		returnHead = n2
		prev = n2
		n2 = n2.Next
	}

	for n1 != nil || n2 != nil {
		if n1 == nil {
			prev.Next = n2
			break
		} else if n2 == nil {
			prev.Next = n1
			break
		}

		if n1.Val <= n2.Val {
			prev.Next = n1
			prev = n1
			n1 = n1.Next
		} else {
			prev.Next = n2
			prev = n2
			n2 = n2.Next
		}
	}
	return returnHead
}

func copyRandomList(head *NodeRnd) *NodeRnd {
	if head == nil {
		return nil
	}

	nodeSet := map[*NodeRnd]*NodeRnd{}
	returnHead := &NodeRnd{head.Val, nil, nil}
	nodeSet[head] = returnHead
	if head.Random != nil {
		if head.Random == head {
			returnHead.Random = returnHead
		} else {
			returnHead.Random = &NodeRnd{head.Random.Val, nil, nil}
		}
		nodeSet[head.Random] = returnHead.Random
	}

	node, prev := head.Next, returnHead
	for node != nil {
		var copy *NodeRnd
		if nodeSet[node] != nil {
			copy = nodeSet[node]
		} else {
			copy = &NodeRnd{node.Val, nil, nil}
		}
		nodeSet[node] = copy

		if node.Random != nil {
			if nodeSet[node.Random] != nil {
				copy.Random = nodeSet[node.Random]
			} else {
				copy.Random = &NodeRnd{node.Random.Val, nil, nil}
			}
			nodeSet[node.Random] = copy.Random
		}


		prev.Next = copy
		prev = copy
		node = node.Next
	}

	/*printNodeList(head)
	printNodeList(returnHead)*/
	return returnHead
}

func reorderList(head *ListNode)  {
	node := head
	copied, len := copyList(node)
	reversed := reverseList(copied)
	mid := len/2

	var prev *ListNode
	for i := 0; i < mid; i++ {
		if prev != nil {
			prev.Next = node
		}
		tmp := node.Next
		node.Next = reversed
		prev = reversed
		node = tmp
		if i+1 < mid {
			reversed = reversed.Next
		} else if len%2 == 1 {
			if reversed.Next != nil {
				reversed.Next.Next = nil
			}
		} else {
			reversed.Next = nil
		}
	}
}

func reverseList(head *ListNode) *ListNode {
	var node, prev *ListNode = head, nil
	for node != nil {
		node.Next, prev, node = prev, node, node.Next
	}
	return prev
}

func copyList(head *ListNode) (newHead *ListNode, length int) {
	var prev *ListNode
	newHead = &ListNode{head.Val, nil}
	prev = newHead
	node := head.Next
	length++

	for node != nil {
		newNode := &ListNode{node.Val, nil}
		prev.Next = newNode
		prev = newNode
		node = node.Next
		length++
	}
	return
}

func SumOfLinkedLists(l1 *LinkedList, l2 *LinkedList) *LinkedList {
	if l1 == nil {return l2}
	if l2 == nil {return l1}

	var head *LinkedList
	var prev *LinkedList
	carryOver := 0
	for l1 != nil || l2 != nil {
		l1Val, l2Val := 0, 0
		if l1 != nil {
			l1Val = l1.Value
			l1 = l1.Next
		}
		if l2 != nil {
			l2Val = l2.Value
			l2 = l2.Next
		}

		sum := l1Val+l2Val+carryOver
		carryOver = sum/10
		node := &LinkedList{Value: sum%10}
		if head == nil {
			head = node
		}
		if prev != nil {
			prev.Next = node
		}
		prev = node
	}
	if carryOver != 0 {
		prev.Next = &LinkedList{Value: 1}
	}
	return head
}

func RemoveDuplicatesFromLinkedList(linkedList *LinkedList) *LinkedList {
	if linkedList == nil { return linkedList }

	head := linkedList
	vis := map[int]bool{head.Value:true}
	node, prev := head.Next, head
	for node != nil {
		if vis[node.Value] {
			prev.Next = node.Next
		} else {
			prev = node
		}
		vis[node.Value] = true
		node = node.Next
	}

	return head
}

func ZipLinkedList(linkedList *LinkedList) *LinkedList {
	if linkedList == nil || linkedList.Next == nil || linkedList.Next.Next == nil {
		return linkedList
	}

	head := linkedList
	node := head
	llLen := 0
	for node != nil {
		llLen++
		node = node.Next
	}
	k := llLen/2

	node = head
	for i := 0; i < k; i++ {
		node = node.Next
	}

	var secondList, prev *LinkedList = node.Next, nil
	node.Next = nil
	for secondList != nil {
		tmp := secondList.Next
		secondList.Next = prev
		prev = secondList
		secondList = tmp
	}

	node, secondList = head, prev
	for secondList != nil {
		tmp := node.Next
		tmp2 := secondList.Next
		node.Next = secondList
		secondList.Next = tmp
		node = tmp
		secondList = tmp2
	}
	return head
}

func FindCycleNode(head *ListNode) *ListNode {
	if head == nil {
		return nil
	} else if head.Next == head {
		return head
	} else if head.Next == nil {
		return nil
	}

	slow, fast := head, head
	var intersectNode *ListNode
	for fast.Next != nil && fast.Next.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if fast == slow {
			intersectNode = slow
			break
		}
	}
	if intersectNode == nil {
		return nil
	}

	node := head
	for slow != node {
		slow = slow.Next
		node = node.Next
	}
	return node
}

func GetIntersectionNode(headA, headB *ListNode) *ListNode {
	if headA == nil || headB == nil || headA.Next == nil || headB.Next == nil {
		return nil
	}
	aLen, bLen := 0, 0
	nodeA, nodeB := headA, headB
	for nodeA != nil || nodeB != nil {
		if nodeA != nil {
			aLen++
			nodeA = nodeA.Next
		}
		if nodeB != nil {
			bLen++
			nodeB = nodeB.Next
		}
	}

	var small, large *ListNode
	if aLen >= bLen {
		small, large = headB, headA
	} else {
		small, large = headA, headB
	}

	for i := 0; i < mathext.AbsInt(aLen-bLen); i++ {
		large = large.Next
	}

	for small != nil {
		if small.Next == large.Next {
			return small.Next
		}
		small = small.Next
		large = large.Next
	}
	return nil
}

/*func MergeKLists(lists []*ListNode) *ListNode {
	lnh := collection.ListNodeHeap{}
	for i := range lists {
		lnh.HeapPush(lists[i])
	}

	var node, prev, head *ListNode
	for lnh.Len() > 0 {
		node = lnh.HeapPop()
		if head == nil {
			head = node
		}
		if prev != nil {
			prev.Next = node
		}
		prev = node
		if node.Next != nil {
			lnh.HeapPush(node.Next)
		}
	}
	return head
}*/