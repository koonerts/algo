package main

import (
	"fmt"
	"go-algo/arr"
)

func main() {
	result := arr.FullJustify([]string{"What", "must", "be", "acknowledgment", "shall", "be"}, 16)
	for _, line := range result {
		pln(line)
	}
}

func pln(i ...interface{}) {
	fmt.Println(i...)
}

func max(nums ...int) int {
	val := nums[0]
	for _, num := range nums {
		if num > val {
			val = num
		}
	}
	return val
}

func min(nums ...int) int {
	val := nums[0]
	for _, num := range nums {
		if num < val {
			val = num
		}
	}
	return val
}
