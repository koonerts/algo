package main

import (
	"fmt"
	"go-algo/linkedlist"
)

func main() {
	head := linkedlist.CreateLinkedList([]int{1,1,1,3,4,4,4,5,6,6})
	linkedlist.PrintLinkedList(head)
	res := linkedlist.RemoveDuplicatesFromLinkedList(head)
	linkedlist.PrintLinkedList(res)
}

func print(i interface {}) {
	fmt.Println(i)
}

