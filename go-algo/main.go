package main

import (
	"fmt"
)

func main() {

}

func pln(i ...interface{}) {
	fmt.Println(i...)
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
