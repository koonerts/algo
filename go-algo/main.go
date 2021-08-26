package main

import (
	"fmt"
	"go-algo/arr"
)

func main() {
	pln(arr.DecodeString("3[a]2[bc]"))
	pln(arr.DecodeString("3[a2[c]]"))
	pln(arr.DecodeString("2[abc]3[cd]ef"))
	pln(arr.DecodeString("abc3[cd]xyz"))
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
