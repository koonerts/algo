package test

import (
	"errors"
	"go-algo"
	"reflect"
	"testing"
)

func BenchmarkSliceReverseSwap(b *testing.B) {
	x := getIntSlice()
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		main.reverseSlice(x)
	}
}

func BenchmarkSliceReverseUsingInterface(b *testing.B) {
	x := getIntSlice()
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		reverseUsingInterface(x)
	}
}

func BenchmarkSliceReverseIntSlice(b *testing.B) {
	x := getIntSlice()
	b.ResetTimer()

	for i := 0; i < b.N; i++ {
		main.reverseIntSlice(x)
	}
}

func getIntSlice() []int {
	var x []int
	for i := 0; i < 1000; i++ {
		x = append(x, i)
	}
	return x
}

func reverseUsingInterface(data interface{}) {
	value := reflect.ValueOf(data)
	if value.Kind() != reflect.Slice {
		panic(errors.New("data must be a slice type"))
	}
	valueLen := value.Len()
	for i := 0; i <= int((valueLen-1)/2); i++ {
		reverseIndex := valueLen - 1 - i
		tmp := value.Index(reverseIndex).Interface()
		value.Index(reverseIndex).Set(value.Index(i))
		value.Index(i).Set(reflect.ValueOf(tmp))
	}
}
