package main

import (
	"encoding/json"
	"fmt"
	"math"
	"reflect"
	"strconv"
	"unsafe"
)

func main() {
	root := createTreeNode([]int{37,-34,-48,-1<<31,-100,-101,48,-1<<31,-1<<31,-1<<31,-1<<31,-54,-1<<31,-71,-22,-1<<31,-1<<31,-1<<31,8})
	p := getTreeNode(root, -71)
	q := getTreeNode(root, 8)
	fmt.Println(lowestCommonAncestor(root, p, q))
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

func IsNumeric(s string) bool {
	_, err := strconv.ParseFloat(s, 64)
	return err == nil
}

func printSlice(iSlice interface{}) {
	switch slice := iSlice.(type) {
	case [][]bool:
		for _, value := range slice {
			fmt.Println(value)
		}
	case [][]string:
		for _, value := range slice {
			fmt.Println(value)
		}
	case [][]int:
		for _, value := range slice {
			fmt.Println(value)
		}
	case [][]float64:
		for _, value := range slice {
			fmt.Println(value)
		}
	case []bool:
		fmt.Println(slice)
	case []string:
		fmt.Println(slice)
	case []int:
		fmt.Println(slice)
	case []float64:
		fmt.Println(slice)
	}
}


func ReverseSlice(s interface{}) {
	n := reflect.ValueOf(s).Len()
	swap := reflect.Swapper(s)
	for i, j := 0, n-1; i < j; i, j = i+1, j-1 {
		swap(i, j)
	}
}

func ReverseIntSlice(data []int) {
	for i, j := 0, len(data)-1; i < j; i, j = i+1, j-1 {
		data[i], data[j] = data[j], data[i]
	}
}

// ByteSliceToString is used when you really want to convert a slice of bytes to a string without incurring overhead.
// It is only safe to use if you really know the byte slice is not going to change in the lifetime of the string
func byteSliceToString(bs []byte) string {
	// This is copied from runtime. It relies on the string
	// header being a prefix of the slice header!
	return *(*string)(unsafe.Pointer(&bs))
}