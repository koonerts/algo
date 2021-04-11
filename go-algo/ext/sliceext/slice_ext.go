package sliceext

import (
	"reflect"
	"unsafe"
)

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

// Is used when you really want to convert a sliceext of bytes to a string without incurring overhead.
// It is only safe to use if you really know the byte sliceext is not going to change in the lifetime of the string.
type ByteSlice []byte
func (bs ByteSlice) StringNoAlloc() string {
	// This is copied from runtime. It relies on the string
	// header being a prefix of the sliceext header!
	return *(*string)(unsafe.Pointer(&bs))
}