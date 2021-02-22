package main

import "fmt"

type ListNode struct {
	Val int
	Next *ListNode
}

type NodeRnd struct {
	Val int
	Next *NodeRnd
	Random *NodeRnd
}

func createListNodeList(vals []int) *ListNode {
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

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1.Val == 0 && l1.Next == nil {
		return l2
	} else if l2.Val == 0 && l2.Next == nil {
		return l1
	}

	var returnHead, prev *ListNode
	carry := 0
	n1, n2 := l1, l2
	for n1 != nil || n2 != nil {
		var n1Val, n2Val int
		if n1 != nil {
			n1Val = n1.Val
		}
		if n2 != nil {
			n2Val = n2.Val
		}

		sum := n1Val+n2Val+carry
		carry = sum/10
		node := &ListNode{sum%10, nil}
		if returnHead == nil {
			returnHead = node
		} else {
			prev.Next = node
		}

		prev = node
		if n1 != nil {
			n1 = n1.Next
		}
		if n2 != nil {
			n2 = n2.Next
		}
	}
	if carry == 1 {
		prev.Next = &ListNode{1, nil}
	}
	return returnHead
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
	var prev *ListNode
	node := head
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

