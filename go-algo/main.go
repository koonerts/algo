package main

import (
	"fmt"
	"go-algo/arr"
)

func main() {
	print(arr.SubarraySum2([]int{-1,-1,1}, 2))
}

func print(i interface {}) {
	fmt.Println(i)
}

