package main

import (
	"encoding/json"
	"fmt"
	"math"
)

func main() {
	blocks := []Block {
		{"gym": false, "school": true, "store": false},
		{"gym": true, "school": false, "store": false},
		{"gym": true, "school": true, "store": false},
		{"gym": false, "school": true, "store": false},
		{"gym": false, "school": true, "store": true},
	}
	fmt.Println(ApartmentHunting(blocks, []string{"gym", "school", "store"}))
}


func PrettyPrint(v interface{}) (err error) {
	b, err := json.MarshalIndent(v, "", "  ")
	if err == nil {
		fmt.Println(string(b))
	}
	return
}


func max(nums ...int) int {
	maxInt := math.MinInt32
	for i := range nums {
		if nums[i] > maxInt {
			maxInt = nums[i]
		}
	}
	return maxInt
}

func min(nums ...int) int {
	minInt := math.MaxInt32
	for i := range nums {
		if nums[i] < minInt {
			minInt = nums[i]
		}
	}
	return minInt
}

func printSlice(iMatrix interface{}) {
	switch matrix := iMatrix.(type) {
	case [][]bool:
		for _, value := range matrix {
			fmt.Println(value)
		}
	case [][]string:
		for _, value := range matrix {
			fmt.Println(value)
		}
	case [][]int:
		for _, value := range matrix {
			fmt.Println(value)
		}
	case []bool:
		fmt.Println(matrix)
	case []string:
		fmt.Println(matrix)
	case []int:
		fmt.Println(matrix)
	}

}