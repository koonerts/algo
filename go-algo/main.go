package main

import (
	"encoding/json"
	"fmt"
	"math"
	"reflect"
	"unsafe"
)


func main() {
	calendar1 := []StringMeeting{{"9:00", "10:30"}, StringMeeting{"12:00", "13:00"}, StringMeeting{"16:00", "18:00"}}
	bounds1 := StringMeeting{"9:00", "20:00"}
	calendar2 := []StringMeeting{{"10:00", "11:30"}, {"12:30", "14:30"}, {"14:30", "15:00"}, {"16:00", "17:00"}}
	bounds2 := StringMeeting{"10:00", "18:30"}
	fmt.Println(CalendarMatching(calendar1, bounds1, calendar2, bounds2, 30))
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
	case []bool:
		fmt.Println(slice)
	case []string:
		fmt.Println(slice)
	case []int:
		fmt.Println(slice)
	}
}

func reverseSlice(s interface{}) {
	n := reflect.ValueOf(s).Len()
	swap := reflect.Swapper(s)
	for i, j := 0, n-1; i < j; i, j = i+1, j-1 {
		swap(i, j)
	}
}

func reverseIntSlice(data []int) {
	for i, j := 0, len(data)-1; i < j; i, j = i+1, j-1 {
		data[i], data[j] = data[j], data[i]
	}
}

// ByteSliceToString is used when you really want to convert a slice // of bytes to a string without incurring overhead. It is only safe
// to use if you really know the byte slice is not going to change // in the lifetime of the string
func byteSliceToString(bs []byte) string {
	// This is copied from runtime. It relies on the string
	// header being a prefix of the slice header!
	return *(*string)(unsafe.Pointer(&bs))
}

