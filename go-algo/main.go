package main

import (
	"fmt"
)

func main() {
	a := &Test{1}
	b := *a
	b.x = 2
	pln(a.x, b.x)
}

func pln(i ...interface{}) {
	if len(i) == 1 {
		fmt.Println(i[0])
	} else {
		fmt.Println(i)
	}
}

type Test struct {
	x int
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