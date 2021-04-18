package main

import (
	"fmt"
	"go-algo/linkedlist"
)

func main() {
	head := linkedlist.CreateListNodeList([]int{3,2,0,-4})
	node := head
	for node.Val != -4 {
		node = node.Next
	}
	node.Next = head.Next
	fmt.Println(linkedlist.FindCycleNode(head))
}

