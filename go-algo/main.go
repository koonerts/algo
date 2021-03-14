package main

import (
	"fmt"
	"go-algo/arr"
)

func main() {
	print(arr.ValidStartingCity([]int{5, 25, 15, 10, 15}, []int{1, 2, 1, 0, 3}, 10))
	print(arr.ValidStartingCity([]int{10, 20, 10, 15, 5, 15, 25}, []int{0, 2, 1, 0, 0, 1, 1}, 20))
}

func print(i ...interface{}) {
	fmt.Println(i...)
}
