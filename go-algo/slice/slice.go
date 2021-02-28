package slice

import (
	"fmt"
	"reflect"
	"unsafe"
)

func PrintSlice(iSlice interface{}) {
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

func ContainsString(s []string, val string) bool {
	for i := range s {
		if s[i] == val {
			return true
		}
	}
	return false
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
func ByteSliceToString(bs []byte) string {
	// This is copied from runtime. It relies on the string
	// header being a prefix of the slice header!
	return *(*string)(unsafe.Pointer(&bs))
}

